class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """Sorting

        Ni se oferă o listă de intervale, iar unele dintre ele se pot suprapune.
        Scopul este de a uni toate intervalele care se suprapun, astfel încât
        lista finală să conțină doar intervale care nu se suprapun, acoperind
        aceleași intervale de timp.

        O abordare firească este următoarea:
        - dacă intervalele sunt procesate în ordine sortată după ora de
        începere, 
        - atunci orice suprapunere poate avea loc doar cu intervalul
        adăugat cel mai recent

        Așadar, după sortare:
        - ținem evidența ultimului interval fuzionat
        - dacă intervalul curent se suprapune cu acesta, le fuzionăm
        - în caz contrar, începem un interval nou

        T = O(n log n), S = O(n)
        """
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            last_end = output[-1][1]

            if start <= last_end:
                output[-1][1] = max(last_end, end)
            else:
                output.append([start, end])
        return output



        """Greedy

        Vrem să fuzionăm toate intervalele care se suprapun, astfel încât
        rezultatul să conțină doar intervale care nu se suprapun.

        Această soluție folosește o abordare de tip „greedy” cu un tablou auxiliar:

        - Pentru fiecare punct de început posibil, start, înregistrăm capătul
        cel mai îndepărtat al oricărui interval care începe la start.
        - Apoi scanăm de la stânga la dreapta, păstrând punctul cel mai
        îndepărtat pe care trebuie încă să îl acoperim (să îl avem).

        În timpul scanării:
        - dacă observăm un interval care începe la poziția i, s-ar putea să fie
        necesar să extindem capătul intervalului fuzionat curent pentru a-l
        include 
        - odată ce indexul de scanare ajunge la cel mai îndepărtat capăt
        necesar, putem închide în siguranță intervalul fuzionat curent

        Astfel, scanarea se comportă astfel:
        - „începe un interval fuzionat când observăm pentru prima dată acoperire”
        - „continuă să-i extindă capătul atâta timp cât există suprapuneri”
        - „închide-l când terminăm acoperirea”

        n - len(intervals), m - max(start value)
        T = O(n + m), S = O(n)
        """
        # max_val = max(interval[0] for interval in intervals)

        # mp = [0] * (max_val + 1)
        # for start, end in intervals:
        #     mp[start] = max(end + 1, mp[start])

        # res = []
        # have = -1
        # interval_start = -1

        # for i in range(len(mp)):
        #     if mp[i] != 0:
        #         if interval_start == -1:
        #             interval_start = i
        #         have = max(mp[i] - 1, have)

        #     if have == i:
        #         res.append([interval_start, have])
        #         have = -1
        #         interval_start = -1

        # if interval_start != -1:
        #     res.append([interval_start, have])

        # return res
