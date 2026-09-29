// msolve2.cs - mixed-table annealer. Codes below FREE map freely to single letters (a letter alphabet with
// homophones); codes from FREE up map non-decreasingly into a sorted inventory of syllables and words (one-part).
// Objective: 5-gram log-prob + bonus per letter - length penalty per code + wS * unigram-word segmentation.
// usage: msolve2.exe lm.bin words.tsv inv.txt ct.txt threads restarts iters T0 T1 bonus maxmult FREE wS seed out.txt [init.tsv]
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Threading;

class MSolveFree
{
    const int A = 26, O = 5, MAXL = 16;
    static float[] LP; static int[] child; static float[] wlp;
    static float UNK1, UNK2, UNK3;
    static string[] INV; static int[][] INVC; static int K;
    static int[] seq; static int N; static int[] codes; static int n; static bool[] free; static int[] ordi; static int[] posOf;
    static double BONUS, wS; static int MAXM;

    static void Main(string[] a)
    {
        var ci = CultureInfo.InvariantCulture;
        var bytes = File.ReadAllBytes(a[0]); LP = new float[bytes.Length / 4]; Buffer.BlockCopy(bytes, 0, LP, 0, bytes.Length);
        LoadWords(a[1]);
        INV = File.ReadAllLines(a[2]).Select(s => s.Trim()).Where(s => s.Length > 0).ToArray(); K = INV.Length;
        INVC = INV.Select(s => s.Select(c => c - 'a').ToArray()).ToArray();
        var toks = File.ReadAllText(a[3]).Split(new[] { ' ', '\n', '\r', '\t' }, StringSplitOptions.RemoveEmptyEntries);
        int threads = int.Parse(a[4]), restarts = int.Parse(a[5]); long iters = long.Parse(a[6]);
        double T0 = double.Parse(a[7], ci), T1 = double.Parse(a[8], ci); BONUS = double.Parse(a[9], ci); MAXM = int.Parse(a[10]);
        int FREE = int.Parse(a[11]); wS = double.Parse(a[12], ci); int seed0 = int.Parse(a[13]); string outPath = a[14];
        string init = a.Length > 15 ? a[15] : null;
        codes = toks.Where(t => t != "|").Select(int.Parse).Distinct().OrderBy(x => x).ToArray(); n = codes.Length;
        var idx = new Dictionary<int, int>(); for (int i = 0; i < n; i++) idx[codes[i]] = i;
        seq = toks.Select(t => t == "|" ? -1 : idx[int.Parse(t)]).ToArray(); N = seq.Length;
        free = codes.Select(c => c < FREE).ToArray();
        ordi = Enumerable.Range(0, n).Where(i => !free[i]).ToArray();
        posOf = new int[n]; for (int k = 0; k < ordi.Length; k++) posOf[ordi[k]] = k;
        Console.Error.WriteLine("tokens {0} codes {1} free {2} inventory {3}", seq.Count(x => x >= 0), n, n - ordi.Length, K);
        int[] initG = null;
        if (init != null)
        {
            var m = File.ReadAllLines(init).Select(l => l.Split('\t')).Where(p => p.Length >= 2).ToDictionary(p => int.Parse(p[0]), p => p[1]);
            initG = new int[n];
            for (int i = 0; i < n; i++) initG[i] = m.ContainsKey(codes[i]) ? Math.Max(0, Array.IndexOf(INV, m[codes[i]])) : 0;
            Console.Error.WriteLine("init score {0:F1}", 0);
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
                    var res = Anneal(new Random(seed0 * 1000003 + r * 7919 + 1), iters, T0, T1, initG);
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
                w.WriteLine("KEY\t" + string.Join(" ", Enumerable.Range(0, n).Select(i => codes[i] + "=" + INV[r.Item3[i]])));
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

    static double SegRun(int[] txt, int n, float[] best)
    {
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
        return best[n];
    }

    static double Pen(int len) { return len <= 1 ? 0 : len == 2 ? 0.15 : len == 3 ? 0.6 : 1.0 + 0.3 * (len - 4); }

    static double Score(int[] g, int[] buf, float[] best)
    {
        double tot = 0, seg = 0; int L = 0, bl = 0;
        for (int p = 0; p <= N; p++)
        {
            if (p == N || seq[p] < 0)
            {
                for (int e = O - 1; e < bl; e++) { int c = 0; for (int j = e - O + 1; j <= e; j++) c = c * A + buf[j]; tot += LP[c]; }
                if (wS != 0 && bl > 0) seg += SegRun(buf, bl, best);
                L += bl; bl = 0; continue;
            }
            foreach (var ch in INVC[g[seq[p]]]) buf[bl++] = ch;
        }
        double pen = 0; for (int i = 0; i < n; i++) pen += Pen(INV[g[i]].Length);
        return tot + BONUS * L - pen + wS * seg;
    }

    static bool MultOk(int[] g, int k0, int k1)
    {
        int a = Math.Max(0, k0 - MAXM), b = Math.Min(ordi.Length - 1, k1 + MAXM); int run = 1;
        for (int k = a + 1; k <= b; k++) { run = g[ordi[k]] == g[ordi[k - 1]] ? run + 1 : 1; if (run > MAXM) return false; }
        return true;
    }

    static Tuple<double, string, int[]> Anneal(Random rnd, long iters, double T0, double T1, int[] initG)
    {
        var letters = Environment.GetEnvironmentVariable("FREEALL") == "1" ? Enumerable.Range(0, K).ToArray() : Enumerable.Range(0, K).Where(k => INV[k].Length == 1).ToArray();
        var g = new int[n]; var buf = new int[N * 14]; var best = new float[N * 14 + 1];
        if (initG != null) Array.Copy(initG, g, n);
        else
        {
            var set = new SortedSet<int>(); while (set.Count < Math.Min(ordi.Length, K)) set.Add(rnd.Next(K));
            var arr = set.ToArray(); for (int k = 0; k < ordi.Length; k++) g[ordi[k]] = arr[Math.Min(k, arr.Length - 1)];
            for (int i = 0; i < n; i++) if (free[i]) g[i] = letters[rnd.Next(letters.Length)];
        }
        int m = ordi.Length;
        double cur = Score(g, buf, best), bestS = cur; var bg = (int[])g.Clone(); var ng = new int[n];
        for (long it = 0; it < iters; it++)
        {
            double T = T0 * Math.Pow(T1 / T0, (double)it / iters);
            Array.Copy(g, ng, n);
            double r = rnd.NextDouble();
            if ((r < 0.25 || m == 0) && m < n)
            {
                int i; do { i = rnd.Next(n); } while (!free[i]);
                ng[i] = letters[rnd.Next(letters.Length)]; if (ng[i] == g[i]) continue;
            }
            else if (r < 0.75)
            {
                int k = rnd.Next(m), i = ordi[k];
                int lo = k > 0 ? ng[ordi[k - 1]] : 0, hi = k < m - 1 ? ng[ordi[k + 1]] : K - 1;
                if (lo == hi) continue;
                ng[i] = rnd.Next(lo, hi + 1); if (ng[i] == g[i]) continue;
                if (!MultOk(ng, k, k)) continue;
            }
            else
            {
                int k0 = rnd.Next(m), k1 = Math.Min(m, k0 + rnd.Next(2, 21)); int d = (rnd.Next(2) == 0 ? -1 : 1) * rnd.Next(1, 5);
                bool ok = true;
                for (int k = k0; k < k1; k++) { ng[ordi[k]] += d; if (ng[ordi[k]] < 0 || ng[ordi[k]] >= K) ok = false; }
                if (!ok) continue;
                if (k0 > 0 && ng[ordi[k0 - 1]] > ng[ordi[k0]]) continue;
                if (k1 < m && ng[ordi[k1 - 1]] > ng[ordi[k1]]) continue;
                if (!MultOk(ng, k0, k1 - 1)) continue;
            }
            double s = Score(ng, buf, best);
            if (s >= cur || rnd.NextDouble() < Math.Exp((s - cur) / T))
            {
                var tmp = g; g = ng; ng = tmp; cur = s;
                if (cur > bestS) { bestS = cur; Array.Copy(g, bg, n); }
            }
        }
        var sb = new System.Text.StringBuilder();
        foreach (var x in seq) sb.Append(x < 0 ? " | " : INV[bg[x]] + ".");
        return Tuple.Create(bestS, sb.ToString(), bg);
    }
}
