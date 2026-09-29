// gsolve.cs - heat-bath (Gibbs) sampler for a one-part code: sorted codes map non-decreasingly into a sorted
// inventory of letters, syllables and words; for one code at a time every admissible unit between its
// neighbours' values is scored exactly on the n-gram windows round its occurrences and one is drawn from
// exp(delta / T). Codes below FREE are free single letters. Objective: 5-gram log-prob + bonus per letter
// - length penalty per code. usage:
//   gsolve.exe lm.bin inv.txt ct.txt threads restarts sweeps T0 T1 bonus maxmult FREE seed out.txt [init.tsv]
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Threading;

class GSolve
{
    const int A = 26, O = 5;
    static float[] LP; static string[] INV; static int[][] INVC; static int K;
    static int[] seq, segOf; static int N; static int[] codes; static int n; static bool[] free; static int[] ordi, posOf;
    static int[][] occ; static double BONUS; static int MAXM; static int[] letters;

    static void Main(string[] a)
    {
        var ci = CultureInfo.InvariantCulture;
        var bytes = File.ReadAllBytes(a[0]); LP = new float[bytes.Length / 4]; Buffer.BlockCopy(bytes, 0, LP, 0, bytes.Length);
        INV = File.ReadAllLines(a[1]).Select(s => s.Trim()).Where(s => s.Length > 0).ToArray(); K = INV.Length;
        INVC = INV.Select(s => s.Select(c => c - 'a').ToArray()).ToArray();
        letters = Enumerable.Range(0, K).Where(k => INV[k].Length == 1).ToArray();
        var toks = File.ReadAllText(a[2]).Split(new[] { ' ', '\n', '\r', '\t' }, StringSplitOptions.RemoveEmptyEntries);
        int threads = int.Parse(a[3]), restarts = int.Parse(a[4]), sweeps = int.Parse(a[5]);
        double T0 = double.Parse(a[6], ci), T1 = double.Parse(a[7], ci); BONUS = double.Parse(a[8], ci); MAXM = int.Parse(a[9]);
        int FREE = int.Parse(a[10]); int seed0 = int.Parse(a[11]); string outPath = a[12]; string init = a.Length > 13 ? a[13] : null;
        codes = toks.Where(t => t != "|").Select(int.Parse).Distinct().OrderBy(x => x).ToArray(); n = codes.Length;
        var idx = new Dictionary<int, int>(); for (int i = 0; i < n; i++) idx[codes[i]] = i;
        var sq = new List<int>(); var sg = new List<int>(); int seg = 0;
        foreach (var t in toks) { if (t == "|") { seg++; continue; } sq.Add(idx[int.Parse(t)]); sg.Add(seg); }
        seq = sq.ToArray(); segOf = sg.ToArray(); N = seq.Length;
        occ = new int[n][]; var ol = new List<int>[n]; for (int i = 0; i < n; i++) ol[i] = new List<int>();
        for (int p = 0; p < N; p++) ol[seq[p]].Add(p); for (int i = 0; i < n; i++) occ[i] = ol[i].ToArray();
        free = codes.Select(c => c < FREE).ToArray();
        ordi = Enumerable.Range(0, n).Where(i => !free[i]).ToArray();
        posOf = Enumerable.Repeat(-1, n).ToArray(); for (int k = 0; k < ordi.Length; k++) posOf[ordi[k]] = k;
        Console.Error.WriteLine("tokens {0} codes {1} free {2} inventory {3}", N, n, n - ordi.Length, K);
        int[] initG = null;
        if (init != null)
        {
            var m = File.ReadAllLines(init).Select(l => l.Split('\t')).Where(p => p.Length >= 2).ToDictionary(p => int.Parse(p[0]), p => p[1]);
            initG = new int[n];
            for (int i = 0; i < n; i++) initG[i] = m.ContainsKey(codes[i]) ? Math.Max(0, Array.IndexOf(INV, m[codes[i]])) : 0;
        }
        var results = new List<Tuple<double, string, int[]>>(); var lk = new object(); int next = 0; var ths = new List<Thread>();
        for (int th = 0; th < threads; th++)
        {
            var thr = new Thread(() =>
            {
                while (true)
                {
                    int r; lock (lk) { r = next++; }
                    if (r >= restarts) break;
                    var res = Run(new Random(seed0 * 1000003 + r * 7919 + 1), sweeps, T0, T1, initG);
                    lock (lk) { results.Add(res); Console.Error.WriteLine("restart {0}: {1:F1} {2}", r, res.Item1, res.Item2.Substring(0, Math.Min(160, res.Item2.Length))); }
                }
            });
            thr.Start(); ths.Add(thr);
        }
        foreach (var t in ths) t.Join();
        using (var w = new StreamWriter(outPath))
            foreach (var r in results.OrderByDescending(z => z.Item1))
            {
                w.WriteLine("{0:F2}\t{1}", r.Item1, r.Item2);
                w.WriteLine("KEY\t" + string.Join(" ", Enumerable.Range(0, n).Select(i => codes[i] + "=" + INV[r.Item3[i]])));
            }
    }

    static double Pen(int len) { return len <= 1 ? 0 : len == 2 ? 0.15 : len == 3 ? 0.6 : 1.0 + 0.3 * (len - 4); }

    static double Full(int[] g)
    {
        double tot = 0; int L = 0; var buf = new List<int>(); int cs = -1;
        Action flush = () => { for (int e = O - 1; e < buf.Count; e++) { int c = 0; for (int j = e - O + 1; j <= e; j++) c = c * A + buf[j]; tot += LP[c]; } L += buf.Count; buf.Clear(); };
        for (int p = 0; p < N; p++) { if (segOf[p] != cs) { flush(); cs = segOf[p]; } buf.AddRange(INVC[g[seq[p]]]); }
        flush();
        double pen = 0; for (int i = 0; i < n; i++) pen += Pen(INV[g[i]].Length);
        return tot + BONUS * L - pen;
    }

    // n-gram score of the windows touching token p when it spells unit u (other tokens as in g)
    static double Local(int[] g, int p, int u, int[] buf)
    {
        int s = segOf[p]; int nl = 0;
        // left context, up to 4 chars
        var left = new int[4]; int have = 0;
        for (int q = p - 1; q >= 0 && segOf[q] == s && have < 4; q--)
        {
            var ch = INVC[g[seq[q]]];
            for (int k = ch.Length - 1; k >= 0 && have < 4; k--) left[have++] = ch[k];
        }
        for (int k = have - 1; k >= 0; k--) buf[nl++] = left[k];
        int start = nl;
        foreach (var c in INVC[u]) buf[nl++] = c;
        int uend = nl; int rh = 0;
        for (int q = p + 1; q < N && segOf[q] == s && rh < 4; q++)
            foreach (var c in INVC[g[seq[q]]]) { if (rh >= 4) break; buf[nl++] = c; rh++; }
        double tot = 0;
        for (int e = start; e < nl; e++)
        {
            if (e - O + 1 < 0) continue;
            int c = 0; for (int j = e - O + 1; j <= e; j++) c = c * A + buf[j]; tot += LP[c];
        }
        return tot;
    }

    static Tuple<double, string, int[]> Run(Random rnd, int sweeps, double T0, double T1, int[] initG)
    {
        var g = new int[n]; var buf = new int[64];
        if (initG != null) Array.Copy(initG, g, n);
        else
        {
            var vals = Enumerable.Range(0, ordi.Length).Select(_ => rnd.Next(K)).OrderBy(x => x).ToArray();
            for (int k = 0; k < ordi.Length; k++) g[ordi[k]] = vals[k];
            for (int i = 0; i < n; i++) if (free[i]) g[i] = letters[rnd.Next(letters.Length)];
        }
        double best = Full(g); var bg = (int[])g.Clone();
        var cand = new List<int>(); var sc = new List<double>();
        for (int sw = 0; sw < sweeps; sw++)
        {
            double T = T0 * Math.Pow(T1 / T0, (double)sw / Math.Max(1, sweeps - 1));
            foreach (var i in Enumerable.Range(0, n).OrderBy(_ => rnd.Next()))
            {
                cand.Clear(); sc.Clear();
                int lo, hi; IEnumerable<int> range;
                if (free[i]) range = letters;
                else
                {
                    int k = posOf[i];
                    lo = k > 0 ? g[ordi[k - 1]] : 0; hi = k < ordi.Length - 1 ? g[ordi[k + 1]] : K - 1;
                    range = Enumerable.Range(lo, hi - lo + 1);
                }
                int cur = g[i]; double baseL = 0;
                foreach (var p in occ[i]) baseL += Local(g, p, cur, buf);
                foreach (var u in range)
                {
                    if (!free[i] && MAXM < 99)
                    {   // multiplicity: count equal neighbours in the chain
                        int k = posOf[i], run = 1;
                        for (int q = k - 1; q >= 0 && g[ordi[q]] == u; q--) run++;
                        for (int q = k + 1; q < ordi.Length && g[ordi[q]] == u; q++) run++;
                        if (run > MAXM) continue;
                    }
                    double d = 0;
                    if (u != cur) { foreach (var p in occ[i]) d += Local(g, p, u, buf); d -= baseL; }
                    d += BONUS * (INV[u].Length - INV[cur].Length) * occ[i].Length - (Pen(INV[u].Length) - Pen(INV[cur].Length));
                    cand.Add(u); sc.Add(d);
                }
                if (cand.Count == 0) continue;
                double mx = sc.Max(); double z = 0;
                for (int c = 0; c < sc.Count; c++) { sc[c] = Math.Exp((sc[c] - mx) / T); z += sc[c]; }
                double r = rnd.NextDouble() * z; int pick = cand.Count - 1;
                for (int c = 0; c < sc.Count; c++) { r -= sc[c]; if (r <= 0) { pick = c; break; } }
                g[i] = cand[pick];
            }
            double f = Full(g);
            if (f > best) { best = f; Array.Copy(g, bg, n); }
        }
        var sb = new System.Text.StringBuilder(); int cs2 = segOf[0];
        for (int p = 0; p < N; p++) { if (segOf[p] != cs2) { sb.Append(" | "); cs2 = segOf[p]; } sb.Append(INV[bg[seq[p]]] + "."); }
        return Tuple.Create(best, sb.ToString(), bg);
    }
}
