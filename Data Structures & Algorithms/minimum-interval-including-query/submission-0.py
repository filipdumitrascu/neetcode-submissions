import heapq


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        """Brute Force

        Pentru fiecare valoare de interogare q, dorim să găsim cea mai mică
        lungime dintre toate intervalele [l, r] care conțin q (adică l <= q <= r).
        Dacă niciun interval nu conține q, returnăm -1.

        Ideea metodei forței brute este foarte simplă:
        - procesăm interogările una câte una
        - pentru fiecare interogare, parcurgem fiecare interval
        - ori de câte ori un interval acoperă interogarea, calculăm lungimea
        acestuia r - l + 1
        - păstrăm cea mai mică lungime întâlnită

        m - len(queries), n - len(intervals)
        T = O(m * n), S = O(1)
        """
        # res = []
        # for q in queries:
        #     cur = -1
        #     for l, r in intervals:
        #         if l <= q <= r:
        #             if cur == -1 or (r - l + 1) < cur:
        #                 cur = r - l + 1
        #     res.append(cur)
        # return res



        """Min Heap

        Pentru fiecare interogare q, dorim să aflăm lungimea celui mai mic
        interval [l, r] astfel încât l ≤ q ≤ r. Dacă niciun interval nu
        acoperă valoarea q, răspunsul este -1.

        O metodă foarte eficientă de a face acest lucru este:
        - procesăm interogările în ordine sortată
        - pe măsură ce interogările cresc, adăugăm intervale al căror
        început ≤ q
        - dintre intervalele active, eliminăm orice interval care se termină
        înainte de q
        - cel mai mic interval valid se află întotdeauna în vârful unui heap minim

        Heap-ul este ordonat după lungimea intervalului, astfel încât cel mai
        mic interval care acoperă valoarea este ușor de găsit.

        m - len(queries), n - len(intervals)
        T = O(n log n  + m log m), S = O(n + m)
        """
        intervals.sort()
        min_heap = []

        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(min_heap, (r - l + 1, r))
                i += 1

            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            res[q] = min_heap[0][0] if min_heap else -1

        return [res[q] for q in queries]
