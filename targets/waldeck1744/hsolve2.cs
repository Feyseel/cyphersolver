// hsolve2.cs - homophonic annealer (code type -> letter) on a combined objective:
//   wN * (5-gram log-prob of the letters) + wS * (best unigram-word segmentation of the letters),
// the segmentation from a 1740s German word list (Viterbi over a reversed trie; unknown words of 1-3 letters
// allowed at a cost). The word term is what separates real text from n-gram gibberish at 2.4 tokens per type.
// usage: hsolve2.exe lm.bin words.tsv ct.txt threads restarts iters T0 T1 wN wS seed out.txt [fix.tsv]
//   fix.tsv: code<TAB>letter lines held fixed (cribs).
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Threading;

class HSolve2
{
    const int A = 26, O = 5, MAXL = 16;
    static float[] LP;
    static int N, T;
    static int[] seq; static bool[] win; static int[][] aff; static string[] names; static int[] tcount;
    static int[] segStart, segEnd;
    static int[] child; static float[] wlp; static int nodes;
    static float UNK1, UNK2, UNK3;
    static double wN, wS;
    static int[] fixedL;

    static void Main(string[] a)
    {
        var ci = CultureInfo.InvariantCulture;
        var bytes = File.ReadAllBytes(a[0]); LP = new float[bytes.Length / 4]; Buffer.BlockCopy(bytes, 0, LP, 0, bytes.Length);
        LoadWords(a[1]);
        var toks = File.ReadAllText(a[2]).Split(new[] { ' ', '\n', '\r', '\t' }, StringSplitOptions.RemoveEmptyEntries);
        int threads = int.Parse(a[3]), restarts = int.Parse(a[4]); long iters = long.Parse(a[5]);
        double T0 = double.Parse(a[6], ci), T1 = double.Parse(a[7], ci);
        wN = double.Parse(a[8], ci); wS = double.Parse(a[9], ci);
        int seed0 = int.Parse(a[10]); string outPath = a[11];
        var map = new Dictionary<string, int>(); var nl = new List<string>(); var s = new List<int>();
        foreach (var t in toks) { if (t == "|") { s.Add(-1); continue; } if (!map.ContainsKey(t)) { map[t] = nl.Count; nl.Add(t); } s.Add(map[t]); }
        seq = s.ToArray(); N = seq.Length; T = nl.Count; names = nl.ToArray();
        tcount = new int[T]; foreach (var x in seq) if (x >= 0) tcount[x]++;
        win = new bool[N];
        for (int i = O - 1; i < N; i++) { bool ok = true; for (int j = i - O + 1; j <= i; j++) if (seq[j] < 0) ok = false; win[i] = ok; }
        var affl = new List<int>[T]; for (int t = 0; t < T; t++) affl[t] = new List<int>();
        for (int i = 0; i < N; i++) if (seq[i] >= 0) for (int e = i; e < Math.Min(N, i + O); e++) if (win[e]) affl[seq[i]].Add(e);
        aff = affl.Select(l => l.Distinct().ToArray()).ToArray();
        var ss = new List<int>(); var se = new List<int>(); int st = 0;
        for (int i = 0; i <= N; i++) if (i == N || seq[i] < 0) { if (i > st) { ss.Add(st); se.Add(i); } st = i + 1; }
        segStart = ss.ToArray(); segEnd = se.ToArray();
        fixedL = Enumerable.Repeat(-1, T).ToArray();
        if (a.Length > 12)
            foreach (var l in File.ReadAllLines(a[12])) { var p = l.Split('\t'); if (p.Length >= 2 && map.ContainsKey(p[0])) fixedL[map[p[0]]] = p[1][0] - 'a'; }
        Console.Error.WriteLine("positions {0} types {1} trie nodes {2} fixed {3}", N, T, nodes, fixedL.Count(x => x >= 0));
        var results = new List<Tuple<double, double, double, string, int[]>>(); var lk = new object(); int next = 0;
        var ths = new List<Thread>();
        for (int th = 0; th < threads; th++)
        {
            var thr = new Thread(() =>
            {
                var sw = System.Diagnostics.Stopwatch.StartNew();
                while (true)
                {
                    int r; lock (lk) { r = next++; }
                    if (r >= restarts) break;
                    var res = Anneal(new Random(seed0 * 100003 + r * 7919 + 17), iters, T0, T1);
                    lock (lk) { results.Add(res); Console.Error.WriteLine("restart {0}: {1:F1} ng {2:F3} seg {3:F3} {4}s  {5}", r, res.Item1, res.Item2, res.Item3, (int)sw.Elapsed.TotalSeconds, Seg(res.Item5).Substring(0, Math.Min(140, Seg(res.Item5).Length))); }
                }
            });
            thr.Start(); ths.Add(thr);
        }
        foreach (var t in ths) t.Join();
        using (var w = new StreamWriter(outPath))
            foreach (var r in results.OrderByDescending(z => z.Item1))
            {
                w.WriteLine("{0:F2}\t{1:F4}\t{2:F4}\t{3}", r.Item1, r.Item2, r.Item3, Seg(r.Item5));
                w.WriteLine("KEY\t" + string.Join(" ", Enumerable.Range(0, T).Select(t => names[t] + "=" + (char)('a' + r.Item5[t]))));
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
            for (int i = w.Length - 1; i >= 0; i--)   // reversed: Viterbi walks backward from each end
            {
                int c = w[i] - 'a'; int nx = ch[node * A + c];
                if (nx < 0) { nx = newNode(); ch[node * A + c] = nx; }
                node = nx;
            }
            lp[node] = (float)Math.Log(double.Parse(p[1]) / tot);
        }
        child = ch.ToArray(); wlp = lp.ToArray(); nodes = wlp.Length;
        UNK1 = (float)(Math.Log(1e-6) + Math.Log(0.05)); UNK2 = (float)(Math.Log(1e-6) + 2 * Math.Log(0.05)); UNK3 = (float)(Math.Log(1e-6) + 3 * Math.Log(0.05));
    }

    static double SegScore(int[] key, float[] best, int[] txt)
    {
        double tot = 0;
        for (int g = 0; g < segStart.Length; g++)
        {
            int a = segStart[g], b = segEnd[g], n = b - a;
            for (int i = 0; i < n; i++) txt[i] = key[seq[a + i]];
            best[0] = 0;
            for (int j = 1; j <= n; j++)
            {
                float bj = float.NegativeInfinity; int node = 0;
                for (int i = j - 1; i >= 0 && i >= j - MAXL; i--)
                {
                    int L = j - i;
                    node = node >= 0 ? child[node * A + txt[i]] : -1;
                    float p;
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

    static string Seg(int[] key)
    {
        var sb = new System.Text.StringBuilder();
        for (int g = 0; g < segStart.Length; g++)
        {
            int a = segStart[g], b = segEnd[g], n = b - a;
            var txt = new int[n]; for (int i = 0; i < n; i++) txt[i] = key[seq[a + i]];
            var best = new float[n + 1]; var bp = new int[n + 1]; best[0] = 0;
            for (int j = 1; j <= n; j++)
            {
                best[j] = float.NegativeInfinity; int node = 0;
                for (int i = j - 1; i >= 0 && i >= j - MAXL; i--)
                {
                    int L = j - i; node = node >= 0 ? child[node * A + txt[i]] : -1; float p;
                    if (node >= 0 && !float.IsNegativeInfinity(wlp[node])) p = wlp[node];
                    else if (L == 1) p = UNK1; else if (L == 2) p = UNK2; else if (L == 3) p = UNK3;
                    else { if (node < 0) break; continue; }
                    if (best[i] + p > best[j]) { best[j] = best[i] + p; bp[j] = i; }
                }
            }
            var parts = new List<string>(); int k = n;
            while (k > 0) { int i = bp[k]; parts.Add(new string(txt.Skip(i).Take(k - i).Select(c => (char)('a' + c)).ToArray())); k = i; }
            parts.Reverse(); if (g > 0) sb.Append(" | "); sb.Append(string.Join(" ", parts));
        }
        return sb.ToString();
    }

    static int Ctx(int[] key, int e) { int c = 0; for (int j = e - O + 1; j <= e; j++) c = c * A + key[seq[j]]; return c; }

    static Tuple<double, double, double, string, int[]> Anneal(Random rnd, long iters, double T0, double T1)
    {
        double[] F = { 6.5, 1.9, 2.9, 5.1, 17.0, 1.7, 3.0, 4.8, 7.6, 0.3, 1.2, 3.4, 2.5, 9.8, 2.6, 0.8, 0.02, 7.0, 7.3, 6.2, 4.4, 0.9, 1.9, 0.03, 0.04, 1.1 };
        double[] cum = new double[A]; double acc = 0; for (int l = 0; l < A; l++) { acc += F[l]; cum[l] = acc; }
        var key = new int[T];
        for (int t = 0; t < T; t++) { if (fixedL[t] >= 0) { key[t] = fixedL[t]; continue; } double u = rnd.NextDouble() * acc; int l = 0; while (cum[l] < u) l++; key[t] = l; }
        var best = new float[N + 1]; var txt = new int[N + 1];
        double ng = 0; int nw = 0; for (int e = 0; e < N; e++) if (win[e]) { ng += LP[Ctx(key, e)]; nw++; }
        double sg = SegScore(key, best, txt);
        double cur = wN * ng + wS * sg, bestS = cur; var bk = (int[])key.Clone();
        var mark = new int[N]; int stamp = 0; var list = new List<int>(64);
        var free = Enumerable.Range(0, T).Where(t => fixedL[t] < 0).ToArray();
        for (long it = 0; it < iters; it++)
        {
            double Tm = T0 * Math.Pow(T1 / T0, (double)it / iters);
            int t1 = free[rnd.Next(free.Length)], t2 = -1, n1 = rnd.Next(A), o1 = key[t1], o2 = 0;
            if (rnd.NextDouble() < 0.2) { t2 = free[rnd.Next(free.Length)]; if (t2 == t1 || key[t2] == o1) continue; o2 = key[t2]; n1 = o2; }
            else if (n1 == o1) continue;
            stamp++; list.Clear();
            foreach (var e in aff[t1]) { mark[e] = stamp; list.Add(e); }
            if (t2 >= 0) foreach (var e in aff[t2]) if (mark[e] != stamp) { mark[e] = stamp; list.Add(e); }
            double before = 0; foreach (var e in list) before += LP[Ctx(key, e)];
            key[t1] = n1; if (t2 >= 0) key[t2] = o1;
            double after = 0; foreach (var e in list) after += LP[Ctx(key, e)];
            double ng2 = ng + after - before;
            double sg2 = wS != 0 ? SegScore(key, best, txt) : 0;
            double sc = wN * ng2 + wS * sg2;
            if (sc >= cur || rnd.NextDouble() < Math.Exp((sc - cur) / Tm))
            {
                cur = sc; ng = ng2; sg = sg2;
                if (cur > bestS) { bestS = cur; Array.Copy(key, bk, T); }
            }
            else { key[t1] = o1; if (t2 >= 0) key[t2] = o2; }
        }
        double bng = 0; for (int e = 0; e < N; e++) if (win[e]) bng += LP[Ctx(bk, e)];
        double bsg = SegScore(bk, best, txt);
        int L = seq.Count(x => x >= 0);
        var sb = new char[N]; for (int i = 0; i < N; i++) sb[i] = seq[i] < 0 ? '|' : (char)('a' + bk[seq[i]]);
        return Tuple.Create(bestS, bng / nw, bsg / L, new string(sb), bk);
    }
}
