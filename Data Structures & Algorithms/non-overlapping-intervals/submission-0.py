class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        """Brute Force

        Vrem să eliminăm un număr minim de intervale, astfel încât intervalele
        rămase să nu se suprapună.

        O modalitate utilă de a aborda această problemă este următoarea:
        - în loc să numărăm direct eliminările, putem încerca să păstrăm cât
        mai multe intervale care nu se suprapun
        - dacă știm numărul maxim de intervale pe care le putem păstra fără
        suprapunere, atunci:
            numărul minim de eliminări = numărul total de intervale - numărul
            maxim de intervale păstrate

        Pentru a lua decizii, sortăm intervalele după ora de începere și
        folosim recursivitatea pentru a explora două opțiuni la fiecare interval:
        - Sărim peste intervalul curent
        - Păstrăm intervalul curent (numai dacă nu se suprapune cu intervalul
        ales anterior)

        Funcția recursivă reprezintă:
        „Care este numărul maxim de intervale care nu se suprapun pe care le
        putem păstra începând de la indexul i, având în vedere că ultimul
        interval ales este prev?”

        T = O(2^n), S = O(n)
        """
        # intervals.sort()

        # def dfs(i, prev):
        #     if i == len(intervals):
        #         return 0

        #     res = dfs(i + 1, prev)
        #     if prev == -1 or intervals[prev][1] <= intervals[i][0]:
        #         res = max(res, 1 + dfs(i + 1, i))

        #     return res

        # return len(intervals) - dfs(0, -1)



        """Greedy (Sort By Start)

        Vrem să eliminăm numărul minim de intervale, astfel încât intervalele
        rămase să nu se suprapună.

        O strategie de tip „greedy” funcționează bine în acest caz. După
        sortarea intervalelor în funcție de ora de începere, le procesăm de la
        stânga la dreapta și, atunci când apare o suprapunere, îl păstrăm 
        intotdeauna pe cel care se termină mai devreme.

        De ce funcționează acest lucru:
        - Când două intervale se suprapun, păstrarea celui cu ora de încheiere
        mai mică lasă mai mult spațiu pentru intervalele viitoare.
        - Eliminarea intervalului cu ora de încheiere mai mare este întotdeauna
        cea mai bună alegere, deoarece păstrarea acestuia ar bloca mai multe
        intervale viitoare.

        Așadar, în loc să alegem global ce interval să păstrăm, luăm o decizie
        lacomă locală de fiecare dată când apare o suprapunere.

        T = O(n log n), S = O(n)
        """
        # intervals.sort()
        # res = 0
        # prev_end = intervals[0][1]

        # for start, end in intervals[1:]:
        #     if start >= prev_end:
        #         prev_end = end
        #     else:
        #         res += 1
        #         prev_end = min(end, prev_end)
        # return res



        """Greedy (Sort By End)

        Vrem să eliminăm numărul minim de intervale, astfel încât intervalele
        rămase să nu se suprapună.

        O idee „lacomă” foarte simplă este aceea de a păstra întotdeauna
        intervalul care se termină cel mai devreme.
        De ce? Pentru că un interval care se termină mai devreme lasă mai mult
        spațiu pentru intervalele viitoare, reducând astfel șansa unei
        suprapuneri ulterioare.

        Așadar, în loc să decidem direct ce intervale să eliminăm, procedăm astfel:
        - sortăm toate intervalele după ora de încheiere
        - le parcurgem de la stânga la dreapta
        - ținem evidența momentului de încheiere al ultimului interval pe care
        am decis să-l păstrăm

        Ori de câte ori observăm o suprapunere:
        - eliminăm intervalul curent
        - deoarece se încheie mai târziu decât cel pe care l-am păstrat deja
        (datorită sortării)

        Această alegere de tip „greedy” este optimă și asigură păstrarea unui
        număr maxim de intervale.

        T = O(n log n), S = O(1)
        """
        intervals.sort(key = lambda pair: pair[1])
        prev_end = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            if prev_end > intervals[i][0]:
                res += 1
            else:
                prev_end = intervals[i][1]

        return res
