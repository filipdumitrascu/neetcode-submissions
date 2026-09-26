# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        """Brute Force

        Vrem să verificăm dacă o persoană poate participa la toate întâlnirile
        fără ca acestea să se suprapună.

        Două întâlniri se suprapun dacă au un interval de timp comun.
        Pentru două intervale A și B, acest lucru se întâmplă atunci când:
        - ora de încheiere a primului interval este mai târzie decât ora de
        începere a celui de-al doilea interval
        
        Într-o abordare de tip „forță brută”, pur și simplu:
        - comparăm fiecare pereche de întâlniri
        - dacă vreo pereche se suprapune, este imposibil să participi la toate
        întâlnirile

        Această abordare este foarte simplă și ușor de înțeles, ceea ce o face
        ideală ca soluție de pornire.

        T = O(n^2), S = O(1)
        """
        # n = len(intervals)
        # for i in range(n):
        #     a = intervals[i]
        #     for j in range(i + 1, n):
        #         b = intervals[j]
        #         if min(a.end, b.end) > max(a.start, b.start):
        #             return False

        # return True



        """Greedy (Sort by End)

        Vrem să stabilim dacă o persoană poate participa la toate întâlnirile
        fără ca acestea să se suprapună.

        O observație esențială este următoarea:
        - dacă întâlnirile sunt sortate după ora de începere, atunci
        - trebuie să verificăm doar dacă întâlnirile adiacente se suprapun

        De ce funcționează acest lucru:
        - dacă două întâlniri se suprapun, ele trebuie să apară una lângă
        cealaltă după sortarea după ora de începere
        - nu este nevoie să comparăm fiecare pereche

        Așadar, prin sortarea o singură dată și efectuarea unei singure treceri,
        putem detecta eficient orice conflict.

        T = O(n log n), S = O(1)
        """
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False
        return True
