    import heapq


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        """Min Heap

        Vrem să găsim numărul minim de săli de ședințe necesare pentru ca nicio
        ședință să nu se suprapună cu alta.

        O modalitate utilă de a aborda această problemă este următoarea:
        - fiecare ședință are nevoie de o sală de la ora de începere până la
        ora de încheiere
        - dacă o ședință începe după sau în același timp cu încheierea unei alte
        ședințe, acestea pot împărți aceeași sală
        - în caz contrar, avem nevoie de o nouă sală

        Pentru a urmări eficient disponibilitatea sălilor, folosim un min-heap:
        - heap-ul stochează orele de încheiere ale întâlnirilor care ocupă în
        prezent sălile
        - ora de încheiere cea mai mică se află întotdeauna în vârf,
        reprezentând sala care se eliberează cel mai devreme

        Pe măsură ce procesăm întâlnirile în ordinea orelor de începere:
        - dacă întâlnirea care se încheie cel mai devreme se termină înainte ca
        cea curentă să înceapă, putem reutiliza acea sală
        - în caz contrar, trebuie să alocăm o nouă sală

        Dimensiunea maximă pe care o atinge heap-ul este numărul de săli necesare.

        T = O(n log n), S = O(n)
        """
        # intervals.sort(key=lambda x: x.start)
        # min_heap = []

        # for interval in intervals:
        #     if min_heap and min_heap[0] <= interval.start:
        #         heapq.heappop(min_heap)
        #     heapq.heappush(min_heap, interval.end)

        # return len(min_heap)



        """Two Pointers

        Vrem să găsim numărul minim de săli de ședințe necesare pentru ca nicio
        ședință să nu se suprapună cu alta.

        În loc să urmărim intervale întregi, putem împărți problema în două
        cronologii mai simple:
        - o listă cu toate orele de începere
        - o listă cu toate orele de încheiere

        Dacă procesăm aceste secvențe în ordine:
        - ori de câte ori o întâlnire începe înainte ca alta să se termine,
        avem nevoie de o nouă sală
        - ori de câte ori o întâlnire se termină înainte sau în același timp
        cu începerea alteia, o sală devine liberă

        Prin deplasarea a doi pointeri peste orele de începere și de încheiere
        sortate, putem urmări câte întâlniri au loc simultan.

        Numărul maxim de întâlniri simultane în orice moment este exact numărul
        de săli de care avem nevoie.

        T = O(n log n), S = O(n)
        """
        # start = sorted([i.start for i in intervals])
        # end = sorted([i.end for i in intervals])

        # res = count = 0
        # s = e = 0
        # while s < len(intervals):
        #     if start[s] < end[e]:
        #         s += 1
        #         count += 1
        #     else:
        #         e += 1
        #         count -= 1
        #     res = max(res, count)
        # return res



        """Greedy

        Vrem să găsim numărul minim de săli de ședințe necesare pentru ca nicio
        ședință să nu se suprapună cu alta.

        În loc să ne gândim direct la săli, putem privi lucrurile din
        perspectiva evenimentelor pe o linie temporală:
        - când începe o ședință, avem nevoie de încă o sală
        - când se termină o ședință, se eliberează o sală

        Astfel, problema se reduce la:
            Care este numărul maxim de ședințe care pot avea loc simultan?

        Dacă urmărim cum se modifică numărul de întâlniri active în timp,
        valoarea maximă pe care o atingem vreodată este exact numărul de săli
        de care avem nevoie.

        Această abordare de tip „greedy” funcționează astfel:
        - transformăm fiecare întâlnire în două evenimente (început și sfârșit)
        - sortăm toate evenimentele în funcție de timp
        - parcurgem lista de la stânga la dreapta, numărând între timp
        întâlnirile active

        T = O(n log n), S = O(n)
        """
        time = []
        for i in intervals:
            time.append((i.start, 1))
            time.append((i.end, -1))

        time.sort(key=lambda x: (x[0], x[1]))

        res = count = 0
        for t in time:
            count += t[1]
            res = max(res, count)
        return res
