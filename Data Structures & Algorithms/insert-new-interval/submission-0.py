class Solution:
    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        """Linear Search

        Ni se oferă o listă de intervale care nu se suprapun, sortate după ora
        de începere, și trebuie să inserăm "new_interval" în listă, menținând
        în același timp rezultatul sortat și fără suprapuneri.

        Deoarece intervalele sunt deja sortate, le putem procesa într-o singură
        trecere și putem împărți operațiunea în trei părți simple:

        - Intervale situate în întregime înainte de "new_interval"
            Acestea nu se suprapun, așa că le putem adăuga direct la rezultat.

        - Intervale care se suprapun cu "new_interval"
            În cazul în care există suprapunere, le îmbinăm prin extinderea
            intervalului "new_interval":
                nou început = minimul dintre începuturi
                nou sfârșit = maximul dintre sfârșituri

        - Intervale situate complet după intervalul "new_interval" îmbinat
            Nici acestea nu se suprapun, așa că le adăugăm direct.

        În acest fel, scanăm lista o singură dată și îmbinăm intervalele exact
        atunci când este necesar.

        T = O(n), S = O(1)
        """
        # n = len(intervals)
        # i = 0
        # res = []

        # while i < n and intervals[i][1] < new_interval[0]:
        #     res.append(intervals[i])
        #     i += 1

        # while i < n and new_interval[1] >= intervals[i][0]:
        #     new_interval[0] = min(new_interval[0], intervals[i][0])
        #     new_interval[1] = max(new_interval[1], intervals[i][1])
        #     i += 1
        # res.append(new_interval)

        # while i < n:
        #     res.append(intervals[i])
        #     i += 1

        # return res



        """Binary Search

        Ni se oferă o listă de intervale care nu se suprapun, sortate după ora
        de începere, și dorim să inserăm "new_interval", menținând în același
        timp lista finală sortată și fuzionată.

        O idee simplă este următoarea:
        - Folosim căutarea binară pentru a găsi poziția corectă în care ar
        trebui inserat "new_interval", pe baza orei sale de începere.

        - După inserare, lista rămâne sortată în funcție de ora de începere.

        - Apoi efectuăm o trecere normală de îmbinare a intervalelor:
            - dacă intervalul curent nu se suprapune cu ultimul interval din
            rezultat, îl adăugăm la sfârșit;
            - în caz contrar, le îmbinăm prin extinderea sfârșitului.

        Căutarea binară ne ajută să evităm scanarea de la început doar pentru
        a găsi poziția de inserare.

        T = O(n), S = O(1)
        """
        # if not intervals:
        #     return [new_interval]

        # n = len(intervals)
        # target = new_interval[0]
        # left, right = 0, n - 1

        # while left <= right:
        #     mid = left + (right - left) // 2
        #     if intervals[mid][0] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1

        # intervals.insert(left, new_interval)

        # res = []
        # for interval in intervals:
        #     if not res or res[-1][1] < interval[0]:
        #         res.append(interval)
        #     else:
        #         res[-1][1] = max(res[-1][1], interval[1])
        # return res



        """Greedy

        Introducem "new_interval" într-o listă de intervale sortate, care nu se
        suprapun, și dorim ca rezultatul final să rămână sortat și fără suprapuneri.

        O abordare de tip „greedy” funcționează deoarece, pe măsură ce
        parcurgem lista de la stânga la dreapta, fiecare interval se încadrează
        într-unul dintre cele trei cazuri în raport cu "new_interval":

        - Complet după "new_interval"
            - Dacă "new_interval" se termină înainte ca intervalul curent să
            înceapă, nu va exista nicio suprapunere nici cu vreun interval
            ulterior.
            - Așadar, putem plasa "new_interval" aici fără probleme și putem
            returna răspunsul imediat.

        - Complet înainte de "new_interval"
            - Dacă intervalul curent se termină înainte ca "new_interval" să
            înceapă, acesta poate fi adăugat la rezultat fără modificări.

        - Se suprapune cu "new_interval"
            - Dacă se suprapun, le îmbinăm extinzând "new_interval" pentru a
            acoperi ambele intervale.

        Prin îmbinarea continuă atunci când este necesar și oprirea timpurie
        atunci când "new_interval” este plasat, rezolvăm problema într-o
        singură trecere.

        T = O(n), S = O(1)
        """
        res = []

        for i in range(len(intervals)):
            if new_interval[1] < intervals[i][0]:
                res.append(new_interval)
                return res + intervals[i:]

            if new_interval[0] > intervals[i][1]:
                res.append(intervals[i])

            else:
                new_interval = [
                    min(new_interval[0], intervals[i][0]),
                    max(new_interval[1], intervals[i][1]),
                ]

        res.append(new_interval)

        return res
