import heapq
import collections


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        """Brute Force

        Simulăm activitatea procesorului câte o unitate de timp pe rând.
        La fiecare pas, analizăm toate sarcinile rămase și alegem:
        -O sarcină care nu se află în perioada de așteptare (care nu a fost
        executată în ultimele n unități de timp),
        -Dintre acestea, cea cu cel mai mare număr de execuții rămase.

        Dacă nu există o astfel de sarcină, procesorul rămâne inactiv în acea
        unitate de timp.
        Repetăm acest proces până când toate sarcinile sunt finalizate.
        Aceasta este o simulare directă, de tip „forță brută”: foarte ușor de
        înțeles, dar ineficientă.

        t - total time, n - cooldown time
        T = O(t n), S = O(t)
        """
        # count = [0] * 26
        # for task in tasks:
        #     count[ord(task) - ord('A')] += 1

        # arr = []
        # for i in range(26):
        #     if count[i] > 0:
        #         arr.append([count[i], i])

        # time = 0
        # processed = []
        # while arr:
        #     max_i = -1
        #     for i in range(len(arr)):
        #         if all(processed[j] != arr[i][1] for j in range(max(0, time - n), time)):
        #             if max_i == -1 or arr[max_i][0] < arr[i][0]:
        #                 max_i = i

        #     time += 1
        #     curr = -1
        #     if max_i != -1:
        #         curr = arr[max_i][1]
        #         arr[max_i][0] -= 1
        #         if arr[max_i][0] == 0:
        #             arr.pop(max_i)
        #     processed.append(curr)

        # return time



        """Max Heap

        Vrem întotdeauna să executăm sarcina care mai are cele mai multe
        apariții rămase, deoarece acestea sunt cele mai greu de încadrat în
        program (au nevoie de mai multe intervale cu pauze de așteptare).

        Așadar:
        -Menținem un heap maxim al sarcinilor în funcție de numărul lor rămas
        (cea mai frecventă se află în vârf).
        -La fiecare unitate de timp, alegem cea mai frecventă sarcină
        disponibilă și o executăm.
        -După executarea unei sarcini, aceasta intră într-o coadă de așteptare
        cu momentul în care va fi din nou disponibilă (ora curentă + n).
        -Când perioada de așteptare a unei sarcini se încheie, o reintroducem
        în heap, astfel încât să poată fi programată din nou.
        -Dacă heap-ul este gol, dar unele sarcini se află încă în perioada de
        așteptare, putem avansa ora curentă până la următorul moment în care o
        sarcină devine disponibilă.

        În acest fel, utilizăm întotdeauna procesorul cât mai eficient posibil,
        respectând în același timp perioada de așteptare.

        m - num(tasks)
        T = O(m), S = O(1)
        """
        # count = {}
        # for task in tasks:
        #     count[task] = count.get(task, 0) + 1

        # max_heap = [-cnt for cnt in count.values()]
        # heapq.heapify(max_heap)

        # time = 0
        # queue = collections.deque()  # pairs of [-cnt, idle_time]
        # while max_heap or queue:
        #     time += 1

        #     if not max_heap:
        #         time = queue[0][1]
        #     else:
        #         cnt = 1 + heapq.heappop(max_heap)
        #         if cnt:
        #             queue.append([cnt, time + n])

        #     if queue and queue[0][1] == time:
        #         heapq.heappush(max_heap, queue.popleft()[0])

        # return time



        """Greedy

        În loc să simulăm întregul program, putem gândi în termeni de intervale:
        -Să presupunem că "max_freq" este frecvența maximă a oricărei sarcini
        (de exemplu, dacă A apare de 5 ori, iar B de 3 ori, atunci "max_freq" = 5).
        -Imaginăm că așezăm toate instanțele sarcinii celei mai frecvente una lângă alta:
        A _ _ A _ _ A _ _ A _ _ A
        -Există "max_freq" - 1 intervale între aceste sarcini cele mai frecvente.
        -Fiecare interval trebuie să aibă o dimensiune de cel puțin n pentru a
        respecta timpul de așteptare.
        -Deci, numărul inițial de sloturi libere necesare = ("max_freq" - 1) * n.

        Acum, încercăm să umplem aceste sloturi libere folosind alte sarcini:
        -Pentru fiecare altă sarcină cu numărul c, aceasta poate umple până la
        min(c, "max_freq" - 1) dintre aceste spații libere
        (deoarece există doar "max_freq" - 1 spații libere).

        -Scădem această cantitate umplută din numărul de sloturi libere.
        -După ce am luat în considerare toate sarcinile, dacă timpul inactiv
        este încă pozitiv, trebuie să adăugăm acele sloturi inactiv la timpul total.
        -Dacă timpul inactiv devine zero sau negativ, înseamnă că toate
        intervalele sunt deja umplute (sau supraîncărcate) de sarcini, deci nu
        este nevoie de timp inactiv suplimentar.

        În concluzie:

        Timpul total = len(sarcini)
        (fiecare sarcină durează 1 unitate) + max(0, timp inactiv)
        (intervalele suplimentare pe care nu le-am putut umple).

        T = O(m), S = O(1)
        """
        # count = [0] * 26
        # for task in tasks:
        #     count[ord(task) - ord('A')] += 1

        # count.sort()
        # max_freq = count[25]
        # idle = (max_freq - 1) * n

        # for i in range(24, -1, -1):
        #     idle -= min(max_freq - 1, count[i])
        # return max(0, idle) + len(tasks)



        """Math

        Sarcina cu cea mai mare frecvență determină structura minimă necesară
        a programului. Dacă o sarcină apare de "max_freq" ori, aceste apariții
        trebuie să fie la o distanță de cel puțin n unități una de alta.
        Astfel se creează ("max_freq" - 1) „intervale”, iar fiecare interval
        trebuie să aibă o lungime de (n + 1) sloturi
        (sarcina în sine + n perioade de așteptare).

        Dacă mai multe sarcini au aceeași frecvență maximă ("max_count" sarcini),
        toate ocupă ultimul rând al structurii.

        Așadar, timpul minim necesar pentru a programa toate sarcinile fără a
        încălca regulile de timp de așteptare este: 
          timp = ("max_freq" - 1) * (n + 1) + "max_count"

        Cu toate acestea, dacă numărul de sarcini este mai mare decât acest
        timp calculat, atunci simpla executare a tuturor sarcinilor durează mai mult.

        Astfel, răspunsul real trebuie să fie: max(len(sarcini), timp)

        T = O(m), S = O(1)
        """
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        max_freq = max(count)
        max_count = 0
        for i in count:
            max_count += 1 if i == max_freq else 0

        time = (max_freq - 1) * (n + 1) + max_count
        return max(len(tasks), time)
