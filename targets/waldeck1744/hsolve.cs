// hsolve.cs - homophonic substitution annealer: every code type -> one letter, scored by a 5-gram
// letters-only model exported from lang/ (float32 table of log P(c5 | c1..c4), 26^5 entries).
// usage: hsolve.exe lm.bin ct.txt threads restarts iters T0 T1 chiW seed out.txt
//   ct.txt: whitespace-separated code groups; "|" breaks the text (no n-gram window crosses it).
//   chiW: weight of a chi-square penalty tying the letter counts to German frequencies (0 = off).
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading;

class HSolve
{
    const int A = 26, O = 5;
    static float[] LP;
    static int N, T;
    static int[] seq;          // type per position, -1 = break
    static bool[] win;         // a 5-window ends here, all inside one segment
    static int[][] aff;        // per type: window ends touched by its occurrences
    static string[] names;
    static int[] tcount;
    // German letter frequencies (per cent), umlauts folded
    static double[] FREQ = {6.5,1.9,2.9,5.1,17.0,1.7,3.0,4.8,7.6,0.3,1.2,3.4,2.5,9.8,2.6,0.8,0.02,7.0,7.3,6.2,4.4,0.9,1.9,0.03,0.04,1.1};

    static void Main(string[] a)
    {
        var lmPath = a[0]; var ctPath = a[1];
        int threads = int.Parse(a[2]), restarts = int.Parse(a[3]); long iters = long.Parse(a[4]);
        double T0 = double.Parse(a[5], System.Globalization.CultureInfo.InvariantCulture);
        double T1 = double.Parse(a[6], System.Globalization.CultureInfo.InvariantCulture);
        double chiW = double.Parse(a[7], System.Globalization.CultureInfo.InvariantCulture);
        int seed0 = int.Parse(a[8]); string outPath = a[9];

        var bytes = File.ReadAllBytes(lmPath);
        LP = new float[bytes.Length / 4];
        Buffer.BlockCopy(bytes, 0, LP, 0, bytes.Length);

        var toks = File.ReadAllText(ctPath).Split(new[] { ' ', '\n', '\r', '\t' }, StringSplitOptions.RemoveEmptyEntries);
        var map = new Dictionary<string, int>(); var nl = new List<string>();
        var s = new List<int>();
        foreach (var t in toks)
        {
            if (t == "|") { s.Add(-1); continue; }
            if (!map.ContainsKey(t)) { map[t] = nl.Count; nl.Add(t); }
            s.Add(map[t]);
        }
        seq = s.ToArray(); N = seq.Length; T = nl.Count; names = nl.ToArray();
        tcount = new int[T]; foreach (var x in seq) if (x >= 0) tcount[x]++;
        win = new bool[N];
        for (int i = O - 1; i < N; i++) { bool ok = true; for (int j = i - O + 1; j <= i; j++) if (seq[j] < 0) ok = false; win[i] = ok; }
        var affl = new List<int>[T]; for (int t = 0; t < T; t++) affl[t] = new List<int>();
        for (int i = 0; i < N; i++) if (seq[i] >= 0) for (int e = i; e < Math.Min(N, i + O); e++) if (win[e]) affl[seq[i]].Add(e);
        aff = affl.Select(l => l.Distinct().OrderBy(z => z).ToArray()).ToArray();
        int nLetters = seq.Count(z => z >= 0);
        Console.Error.WriteLine("positions {0} letters {1} types {2}", N, nLetters, T);

        var results = new List<Tuple<double, double, string, int[]>>();
        var lk = new object();
        int next = 0;
        var ths = new List<Thread>();
        for (int th = 0; th < threads; th++)
        {
            var thr = new Thread(() =>
            {
                while (true)
                {
                    int r; lock (lk) { r = next++; }
                    if (r >= restarts) break;
                    var rnd = new Random(seed0 * 100003 + r * 7919 + 17);
                    var res = Anneal(rnd, iters, T0, T1, chiW, nLetters);
                    lock (lk)
                    {
                        results.Add(res);
                        Console.Error.WriteLine("restart {0}: {1:F1} ({2:F3}/win) {3}", r, res.Item1, res.Item2, res.Item3.Substring(0, Math.Min(90, res.Item3.Length)));
                    }
                }
            });
            thr.Start(); ths.Add(thr);
        }
        foreach (var thr in ths) thr.Join();
        using (var w = new StreamWriter(outPath))
        {
            foreach (var r in results.OrderByDescending(z => z.Item1))
            {
                w.WriteLine("{0:F2}	{1:F4}	{2}", r.Item1, r.Item2, r.Item3);
                w.WriteLine("KEY\t" + string.Join(" ", Enumerable.Range(0, T).Select(t => names[t] + "=" + (char)('a' + r.Item4[t]))));
            }
        }
    }

    static int Ctx(int[] key, int e)
    {
        int c = 0;
        for (int j = e - O + 1; j <= e; j++) c = c * A + key[seq[j]];
        return c;
    }

    static double Chi(int[] lc, int n)
    {
        double s = 0;
        for (int l = 0; l < A; l++) { double ex = Math.Max(0.05, FREQ[l]) / 100.0 * n; double d = lc[l] - ex; s += d * d / ex; }
        return s;
    }

    static Tuple<double, double, string, int[]> Anneal(Random rnd, long iters, double T0, double T1, double chiW, int nL)
    {
        var key = new int[T];
        // random start drawn from German frequencies
        double[] cum = new double[A]; double acc = 0; for (int l = 0; l < A; l++) { acc += FREQ[l]; cum[l] = acc; }
        for (int t = 0; t < T; t++) { double u = rnd.NextDouble() * acc; int l = 0; while (cum[l] < u) l++; key[t] = l; }
        var lc = new int[A]; for (int t = 0; t < T; t++) lc[key[t]] += tcount[t];
        double ng = 0; int nw = 0;
        for (int e = 0; e < N; e++) if (win[e]) { ng += LP[Ctx(key, e)]; nw++; }
        double cur = ng - chiW * Chi(lc, nL);
        double best = cur; var bestKey = (int[])key.Clone();
        var mark = new int[N]; int stamp = 0; var list = new List<int>(64);
        for (long it = 0; it < iters; it++)
        {
            double Tm = T0 * Math.Pow(T1 / T0, (double)it / iters);
            int t1 = rnd.Next(T), t2 = -1, n1 = rnd.Next(A), o1 = key[t1], o2 = 0;
            if (rnd.NextDouble() < 0.2) { t2 = rnd.Next(T); if (t2 == t1 || key[t2] == o1) continue; o2 = key[t2]; n1 = o2; }
            else if (n1 == o1) continue;
            stamp++; list.Clear();
            foreach (var e in aff[t1]) { mark[e] = stamp; list.Add(e); }
            if (t2 >= 0) foreach (var e in aff[t2]) if (mark[e] != stamp) { mark[e] = stamp; list.Add(e); }
            double before = 0; foreach (var e in list) before += LP[Ctx(key, e)];
            key[t1] = n1; if (t2 >= 0) key[t2] = o1;
            double after = 0; foreach (var e in list) after += LP[Ctx(key, e)];
            lc[o1] -= tcount[t1]; lc[n1] += tcount[t1];
            if (t2 >= 0) { lc[o2] -= tcount[t2]; lc[o1] += tcount[t2]; }
            double cand = ng + after - before;
            double sc = chiW > 0 ? cand - chiW * Chi(lc, nL) : cand;
            if (sc >= cur || rnd.NextDouble() < Math.Exp((sc - cur) / Tm))
            {
                cur = sc; ng = cand;
                if (cur > best) { best = cur; Array.Copy(key, bestKey, T); }
            }
            else
            {
                key[t1] = o1; if (t2 >= 0) key[t2] = o2;
                lc[n1] -= tcount[t1]; lc[o1] += tcount[t1];
                if (t2 >= 0) { lc[o1] -= tcount[t2]; lc[o2] += tcount[t2]; }
            }
        }
        double bng = 0; for (int e = 0; e < N; e++) if (win[e]) bng += LP[Ctx(bestKey, e)];
        var txt = new char[N];
        for (int i = 0; i < N; i++) txt[i] = seq[i] < 0 ? '|' : (char)('a' + bestKey[seq[i]]);
        return Tuple.Create(best, bng / nw, new string(txt), bestKey);
    }
}
