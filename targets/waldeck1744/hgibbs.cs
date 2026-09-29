// hgibbs.cs - heat-bath sampler for a homophonic cipher (code type -> letter). For one code at a time all 26
// letters are scored: exact change of the 5-gram windows round its occurrences (wN) plus the unigram-word
// segmentation of the whole text (wS, Viterbi over a reversed trie of 1740s words); one letter is drawn from
// exp(score / T). usage:
//   hgibbs.exe lm.bin words.tsv ct.txt threads restarts sweeps T0 T1 wN wS seed out.txt [fix.tsv] [init_key.txt]
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Threading;

class HGibbs
{
    const int A = 26, O = 5, MAXL = 16;
    static float[] LP; static int[] child; static float[] wlp; static float UNK1, UNK2, UNK3;
    static int N, T; static int[] seq; static bool[] win; static int[][] aff; static string[] names; static int[] segS, segE;
    static int[] fixedL; static double wN, wS;

    static void Main(string[] a)
    {
        var ci = CultureInfo.InvariantCulture;
        var bytes = File.ReadAllBytes(a[0]); LP = new float[bytes.Length / 4]; Buffer.BlockCopy(bytes, 0, LP, 0, bytes.Length);
        LoadWords(a[1]);
        var toks = File.ReadAllText(a[2]).Split(new[] { ' ', '\n', '\r', '\t' }, StringSplitOptions.RemoveEmptyEntries);
        int threads = int.Parse(a[3]), restarts = int.Parse(a[4]), sweeps = int.Parse(a[5]);
        double T0 = double.Parse(a[6], ci), T1 = double.Parse(a[7], ci); wN = double.Parse(a[8], ci); wS = double.Parse(a[9], ci);
        int seed0 = int.Parse(a[10]); string outPath = a[11];
        var map = new Dictionary<string, int>(); var nl = new List<string>(); var s = new List<int>();
        foreach (var t in toks) { if (t == "|") { s.Add(-1); continue; } if (!map.ContainsKey(t)) { map[t] = nl.Count; nl.Add(t); } s.Add(map[t]); }
        seq = s.ToArray(); N = seq.Length; T = nl.Count; names = nl.ToArray();
        win = new bool[N];
        for (int i = O - 1; i < N; i++) { bool ok = true; for (int j = i - O + 1; j <= i; j++) if (seq[j] < 0) ok = false; win[i] = ok; }
        var affl = new List<int>[T]; for (int t = 0; t < T; t++) affl[t] = new List<int>();
        for (int i = 0; i < N; i++) if (seq[i] >= 0) for (int e = i; e < Math.Min(N, i + O); e++) if (win[e]) affl[seq[i]].Add(e);
        aff = affl.Select(l => l.Distinct().ToArray()).ToArray();
        var ss = new List<int>(); var se = new List<int>(); int st = 0;
        for (int i = 0; i <= N; i++) if (i == N || seq[i] < 0) { if (i > st) { ss.Add(st); se.Add(i); } st = i + 1; }
        segS = ss.ToArray(); segE = se.ToArray();
        fixedL = Enumerable.Repeat(-1, T).ToArray();
        if (a.Length > 12 && a[12] != "-")
            foreach (var l in File.ReadAllLines(a[12])) { var p = l.Split('\t'); if (p.Length >= 2 && map.ContainsKey(p[0])) fixedL[map[p[0]]] = p[1][0] - 'a'; }
        int[] initK = null;
        if (a.Length > 13)
        {
            initK = new int[T];
            var kl = File.ReadAllLines(a[13]).First(l => l.StartsWith("KEY")).Split('\t')[1].Split(' ');
            foreach (var kv in kl) { var p = kv.Split('='); if (map.ContainsKey(p[0])) initK[map[p[0]]] = p[1][0] - 'a'; }
        }
        Console.Error.WriteLine("positions {0} types {1} fixed {2}", N, T, fixedL.Count(x => x >= 0));
        var results = new List<Tuple<double, string, int[]>>(); var lk = new object(); int next = 0; var ths = new List<Thread>();
        for (int th = 0; th < threads; th++)
        {
            var thr = new Thread(() =>
            {
                while (true)
                {
                    int r; lock (lk) { r = next++; }
                    if (r >= restarts) break;
                    var res = Run(new Random(seed0 * 100003 + r * 7919 + 17), sweeps, T0, T1, initK);
                    lock (lk) { results.Add(res); Console.Error.WriteLine("restart {0}: {1:F1} {2}", r, res.Item1, res.Item2.Substring(0, Math.Min(150, res.Item2.Length))); }
                }
            });
            thr.Start(); ths.Add(thr);
        }
        foreach (var t in ths) t.Join();
        using (var w = new StreamWriter(outPath))
            foreach (var r in results.OrderByDescending(z => z.Item1))
            {
                w.WriteLine("{0:F2}\t{1}", r.Item1, r.Item2);
                w.WriteLine("KEY\t" + string.Join(" ", Enumerable.Range(0, T).Select(t => names[t] + "=" + (char)('a' + r.Item3[t]))));
            }
    }

    static void LoadWords(string path)
    {
        var lines = File.ReadAllLines(path); double tot = double.Parse(lines[0]);
        var ch = new List<int>(); var lp = new List<float>();
        Func<int> newNode = () => { for (int k = 0; k < A; k++) ch.Add(-1); lp.Add(float.NegativeInfinity); return lp.Count - 1; };
        newNode();
        foreach (var l in lines.Skip(1))
        {
            var p = l.Split('\t'); var w = p[0]; if (w.Length > MAXL || w.Any(c => c < 'a' || c > 'z')) continue;
            int node = 0;
            for (int i = w.Length - 1; i >= 0; i--) { int c = w[i] - 'a'; int nx = ch[node * A + c]; if (nx < 0) { nx = newNode(); ch[node * A + c] = nx; } node = nx; }
            lp[node] = (float)Math.Log(double.Parse(p[1]) / tot);
        }
        child = ch.ToArray(); wlp = lp.ToArray();
        UNK1 = (float)(Math.Log(1e-6) + Math.Log(0.05)); UNK2 = (float)(Math.Log(1e-6) + 2 * Math.Log(0.05)); UNK3 = (float)(Math.Log(1e-6) + 3 * Math.Log(0.05));
    }

    static double Seg(int[] key, float[] best, int[] txt)
    {
        double tot = 0;
        for (int g = 0; g < segS.Length; g++)
        {
            int a = segS[g], n = segE[g] - a;
            for (int i = 0; i < n; i++) txt[i] = key[seq[a + i]];
            best[0] = 0;
            for (int j = 1; j <= n; j++)
            {
                float bj = float.NegativeInfinity; int node = 0;
                for (int i = j - 1; i >= 0 && i >= j - MAXL; i--)
                {
                    int L = j - i; node = node >= 0 ? child[node * A + txt[i]] : -1; float p;
                    if (node >= 0 && !float.IsNegativeInfinity(wlp[node])) p = wlp[node];
                    else if (L == 1) p = UNK1; else if (L == 2) p = UNK2; else if (L == 3) p = UNK3;
                    else { if (node < 0) break; continue; }
                    float v = best[i] + p; if (v > bj) bj = v;
                }
                best[j] = bj;
            }
            tot += best[n];
        }
        return tot;
    }

    static int Ctx(int[] key, int e) { int c = 0; for (int j = e - O + 1; j <= e; j++) c = c * A + key[seq[j]]; return c; }

    static double Full(int[] key, float[] best, int[] txt)
    {
        double ng = 0; for (int e = 0; e < N; e++) if (win[e]) ng += LP[Ctx(key, e)];
        return wN * ng + (wS != 0 ? wS * Seg(key, best, txt) : 0);
    }

    static Tuple<double, string, int[]> Run(Random rnd, int sweeps, double T0, double T1, int[] initK)
    {
        double[] F = { 6.5, 1.9, 2.9, 5.1, 17.0, 1.7, 3.0, 4.8, 7.6, 0.3, 1.2, 3.4, 2.5, 9.8, 2.6, 0.8, 0.02, 7.0, 7.3, 6.2, 4.4, 0.9, 1.9, 0.03, 0.04, 1.1 };
        double[] cum = new double[A]; double acc = 0; for (int l = 0; l < A; l++) { acc += F[l]; cum[l] = acc; }
        var key = new int[T];
        for (int t = 0; t < T; t++)
        {
            if (fixedL[t] >= 0) key[t] = fixedL[t];
            else if (initK != null) key[t] = initK[t];
            else { double u = rnd.NextDouble() * acc; int l = 0; while (cum[l] < u) l++; key[t] = l; }
        }
        var best = new float[N + 1]; var txt = new int[N + 1];
        double bestS = Full(key, best, txt); var bk = (int[])key.Clone();
        var sc = new double[A];
        var order = Enumerable.Range(0, T).Where(t => fixedL[t] < 0).ToArray();
        for (int sw = 0; sw < sweeps; sw++)
        {
            double Tm = T0 * Math.Pow(T1 / T0, (double)sw / Math.Max(1, sweeps - 1));
            for (int k = order.Length - 1; k > 0; k--) { int j = rnd.Next(k + 1); int tmp = order[k]; order[k] = order[j]; order[j] = tmp; }
            foreach (var t in order)
            {
                int cur = key[t];
                double baseNg = 0; foreach (var e in aff[t]) baseNg += LP[Ctx(key, e)];
                double mx = double.NegativeInfinity;
                for (int l = 0; l < A; l++)
                {
                    key[t] = l;
                    double ng = 0; foreach (var e in aff[t]) ng += LP[Ctx(key, e)];
                    double v = wN * (ng - baseNg);
                    if (wS != 0) v += wS * Seg(key, best, txt);
                    sc[l] = v; if (v > mx) mx = v;
                }
                double z = 0; for (int l = 0; l < A; l++) { sc[l] = Math.Exp((sc[l] - mx) / Tm); z += sc[l]; }
                double r = rnd.NextDouble() * z; int pick = A - 1;
                for (int l = 0; l < A; l++) { r -= sc[l]; if (r <= 0) { pick = l; break; } }
                key[t] = pick;
            }
            double f = Full(key, best, txt);
            if (f > bestS) { bestS = f; Array.Copy(key, bk, T); }
        }
        var sb = new char[N]; for (int i = 0; i < N; i++) sb[i] = seq[i] < 0 ? '|' : (char)('a' + bk[seq[i]]);
        return Tuple.Create(bestS, new string(sb), bk);
    }
}
