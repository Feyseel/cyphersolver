// msolve.cs - monotone-table annealer (after targets/swieten1757/msolve.py): for a one-part (alphabetical) code,
// every observed code maps to a unit of a sorted inventory and the map is non-decreasing in the code value.
// usage: msolve.exe lm.bin inv.txt ct.txt threads restarts iters T0 T1 bonus maxmult seed out.txt [init.tsv]
//   lm.bin  float32 log P(c5|c1..c4), 26^5, letters only;  inv.txt one unit per line, sorted;
//   ct.txt  code groups, "|" = break;  bonus = score per decrypted letter;  maxmult = codes allowed per unit.
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Threading;

class MSolve
{
    const int A = 26, O = 5;
    static float[] LP;
    static string[] INV; static int[][] INVC; static int K;
    static int[] seq; static int N; static int[] codes; static int n;
    static int[] cnt;
    static double BONUS; static int MAXM;

    static void Main(string[] a)
    {
        var ci = CultureInfo.InvariantCulture;
        var bytes = File.ReadAllBytes(a[0]); LP = new float[bytes.Length / 4]; Buffer.BlockCopy(bytes, 0, LP, 0, bytes.Length);
        INV = File.ReadAllLines(a[1]).Select(s => s.Trim()).Where(s => s.Length > 0).ToArray(); K = INV.Length;
        INVC = INV.Select(s => s.Select(c => c - 'a').ToArray()).ToArray();
        var toks = File.ReadAllText(a[2]).Split(new[] { ' ', '\n', '\r', '\t' }, StringSplitOptions.RemoveEmptyEntries);
        int threads = int.Parse(a[3]), restarts = int.Parse(a[4]); long iters = long.Parse(a[5]);
        double T0 = double.Parse(a[6], ci), T1 = double.Parse(a[7], ci); BONUS = double.Parse(a[8], ci); MAXM = int.Parse(a[9]);
        int seed0 = int.Parse(a[10]); string outPath = a[11]; string init = a.Length > 12 ? a[12] : null;
        codes = toks.Where(t => t != "|").Select(int.Parse).Distinct().OrderBy(x => x).ToArray(); n = codes.Length;
        var idx = new Dictionary<int, int>(); for (int i = 0; i < n; i++) idx[codes[i]] = i;
        seq = toks.Select(t => t == "|" ? -1 : idx[int.Parse(t)]).ToArray(); N = seq.Length;
        cnt = new int[n]; foreach (var x in seq) if (x >= 0) cnt[x]++;
        Console.Error.WriteLine("tokens {0} codes {1} inventory {2}", seq.Count(x => x >= 0), n, K);
        int[] initG = null;
        if (init != null)
        {
            var m = File.ReadAllLines(init).Select(l => l.Split('\t')).Where(p => p.Length >= 2).ToDictionary(p => int.Parse(p[0]), p => p[1]);
            initG = new int[n];
            for (int i = 0; i < n; i++) { int k = m.ContainsKey(codes[i]) ? Array.IndexOf(INV, m[codes[i]]) : -1; initG[i] = k; }
            int last = 0; for (int i = 0; i < n; i++) { if (initG[i] < last) initG[i] = last; last = initG[i]; }
        }
        var results = new List<Tuple<double, string, int[]>>(); var lk = new object(); int next = 0;
        var ths = new List<Thread>();
        for (int th = 0; th < threads; th++)
        {
            var thr = new Thread(() =>
            {
                while (true)
                {
                    int r; lock (lk) { r = next++; }
                    if (r >= restarts) break;
                    var rnd = new Random(seed0 * 1000003 + r * 7919 + 1);
                    var res = Anneal(rnd, iters, T0, T1, initG);
                    lock (lk) { results.Add(res); Console.Error.WriteLine("restart {0}: {1:F1} {2}", r, res.Item1, res.Item2.Substring(0, Math.Min(110, res.Item2.Length))); }
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

    // full score of a key
    static double Score(int[] g, int[] buf)
    {
        double tot = 0; int L = 0; int bl = 0;
        for (int p = 0; p <= N; p++)
        {
            if (p == N || seq[p] < 0)
            {
                for (int e = O - 1; e < bl; e++) { int c = 0; for (int j = e - O + 1; j <= e; j++) c = c * A + buf[j]; tot += LP[c]; }
                L += bl; bl = 0; continue;
            }
            foreach (var ch in INVC[g[seq[p]]]) buf[bl++] = ch;
        }
        double pen = 0; for (int i = 0; i < n; i++) pen += Pen(INV[g[i]].Length);
        return tot + BONUS * L - pen;
    }

    static bool MultOk(int[] g, int lo, int hi)
    {
        int a = Math.Max(0, lo - MAXM), b = Math.Min(n - 1, hi + MAXM); int run = 1;
        for (int k = a + 1; k <= b; k++) { run = g[k] == g[k - 1] ? run + 1 : 1; if (run > MAXM) return false; }
        return true;
    }

    static Tuple<double, string, int[]> Anneal(Random rnd, long iters, double T0, double T1, int[] initG)
    {
        var g = new int[n]; var buf = new int[N * 12];
        if (initG != null) Array.Copy(initG, g, n);
        else
        {
            // random non-decreasing start respecting the multiplicity cap: sample n distinct sorted indices
            var set = new SortedSet<int>(); while (set.Count < Math.Min(n, K)) set.Add(rnd.Next(K));
            var arr = set.ToArray(); for (int i = 0; i < n; i++) g[i] = arr[Math.Min(i, arr.Length - 1)];
        }
        double cur = Score(g, buf), best = cur; var bg = (int[])g.Clone(); var ng = new int[n];
        for (long it = 0; it < iters; it++)
        {
            double T = T0 * Math.Pow(T1 / T0, (double)it / iters);
            Array.Copy(g, ng, n);
            int lo, hi;
            if (rnd.NextDouble() < 0.7)
            {
                int i = rnd.Next(n); int a = i > 0 ? ng[i - 1] : 0, b = i < n - 1 ? ng[i + 1] : K - 1;
                if (a == b && ng[i] == a) continue;
                ng[i] = rnd.Next(a, b + 1); lo = hi = i;
            }
            else
            {
                int i = rnd.Next(n), j = Math.Min(n, i + rnd.Next(2, 21)); int d = (rnd.Next(2) == 0 ? -1 : 1) * rnd.Next(1, 5);
                bool ok = true;
                for (int k = i; k < j; k++) { ng[k] += d; if (ng[k] < 0 || ng[k] >= K) ok = false; }
                if (!ok) continue;
                if (i > 0 && ng[i - 1] > ng[i]) continue;
                if (j < n && ng[j - 1] > ng[j]) continue;
                lo = i; hi = j - 1;
            }
            if (!MultOk(ng, lo, hi)) continue;
            double s = Score(ng, buf);
            if (s >= cur || rnd.NextDouble() < Math.Exp((s - cur) / T))
            {
                var tmp = g; g = ng; ng = tmp; cur = s;
                if (cur > best) { best = cur; Array.Copy(g, bg, n); }
            }
        }
        var sb = new System.Text.StringBuilder();
        foreach (var x in seq) sb.Append(x < 0 ? " | " : INV[bg[x]] + ".");
        return Tuple.Create(best, sb.ToString(), bg);
    }
}
