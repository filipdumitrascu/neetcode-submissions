import heapq
import collections


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        """Brute Force    TLE

        Simulăm activitatea procesorului câte o unitate de timp pe rând.
        La fiecare pas, analizăm toate sarcinile rămase și alegem:
        - O sarcină care nu se află în perioada de așteptare (care nu a fost
        executată în ultimele n unități de timp),
        - Dintre acestea, cea cu cel mai mare număr de execuții rămase.

        Dacă nu există o astfel de sarcină, procesorul rămâne inactiv în acea
        unitate de timp.
        Repetăm acest proces până când toate sarcinile sunt finalizate.
        Aceasta este o simulare directă, de tip „forță brută”: foarte ușor de
        înțeles, dar ineficientă.

        t - total time, n - cooldown time
        T = O(t * n), S = O(t)
        """
        # # numarul de aparitii pentru fiecare task ('A' - 'Z')
        # task_counts = [0] * 26

        # for task in tasks:
        #     task_index = ord(task) - ord('A')
        #     task_counts[task_index] += 1

        # # Pastram doar task-urile care exista
        # remaining_tasks = []

        # for task_index in range(26):
        #     if task_counts[task_index] > 0:
        #         remaining_tasks.append(
        #             [task_counts[task_index], task_index]
        #         )

        # # Timpul total simulat.
        # elapsed_time = 0

        # # Istoricul task-urilor executate.
        # processed = []

        # while remaining_tasks:
        #     # Indexul task-ului pe care îl vom executa.
        #     best_task_index = -1

        #     # Verificăm fiecare task rămas.
        #     for task_position in range(len(remaining_tasks)):
        #         task_id = remaining_tasks[task_position][1]

        #         # Verificăm dacă task-ul se află în cooldown.
        #         #
        #         # Dacă a fost executat în ultimele `n` unități de timp,
        #         # nu îl putem executa acum.
        #         is_available = all(
        #             processed[previous_time] != task_id
        #             for previous_time in range(
        #                 max(0, elapsed_time - n),
        #                 elapsed_time
        #             )
        #         )

        #         if not is_available:
        #             continue

        #         # Dintre task-urile disponibile alegem task-ul
        #         # cu cele mai multe execuții rămase.
        #         if (
        #             best_task_index == -1
        #             or remaining_tasks[best_task_index][0]
        #             < remaining_tasks[task_position][0]
        #         ):
        #             best_task_index = task_position

        #     # Am consumat o unitate de timp indiferent dacă
        #     # procesorul a executat un task sau a stat idle.
        #     elapsed_time += 1

        #     # Presupunem inițial că procesorul este idle.
        #     executed_task = -1

        #     # Dacă am găsit un task disponibil, îl executăm.
        #     if best_task_index != -1:
        #         executed_task = remaining_tasks[best_task_index][1]

        #         # O execuție a task-ului a fost consumată.
        #         remaining_tasks[best_task_index][0] -= 1

        #         # Dacă nu mai avem execuții pentru acest task,
        #         # îl eliminăm din lista task-urilor rămase.
        #         if remaining_tasks[best_task_index][0] == 0:
        #             remaining_tasks.pop(best_task_index)

        #     # Salvăm ce s-a executat în acest moment.
        #     # -1 = idle
        #     processed.append(executed_task)

        # return elapsed_time



        """Max Heap

        Vrem întotdeauna să executăm sarcina care mai are cele mai multe
        apariții rămase, deoarece acestea sunt cele mai greu de încadrat în
        program (au nevoie de mai multe intervale cu pauze de așteptare).

        Așadar:
        - Menținem un heap maxim al sarcinilor în funcție de numărul lor rămas
        (cea mai frecventă se află în vârf).
        - La fiecare unitate de timp, alegem cea mai frecventă sarcină
        disponibilă și o executăm.
        - După executarea unei sarcini, aceasta intră într-o coadă de așteptare
        cu momentul în care va fi din nou disponibilă (ora curentă + n).
        - Când perioada de așteptare a unei sarcini se încheie, o reintroducem
        în heap, astfel încât să poată fi programată din nou.
        - Dacă heap-ul este gol, dar unele sarcini se află încă în perioada de
        așteptare, putem avansa ora curentă până la următorul moment în care o
        sarcină devine disponibilă.

        În acest fel, utilizăm întotdeauna procesorul cât mai eficient posibil,
        respectând în același timp perioada de așteptare.

        m - num(tasks)
        T = O(m), S = O(1)
        """
        count = {}
        for task in tasks:
            count[task] = count.get(task, 0) + 1

        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = collections.deque()  # pairs of [-cnt, idle_time]
        while max_heap or queue:
            time += 1

            # daca nu e nimic in heap, inseamna ca toate taskurile
            # trebuie sa astepte si sarim direct la timpul primului
            # task disponibil
            if not max_heap:
                time = queue[0][1]
            else:
                # se executa taskul si se pune in coada pentru cooldown
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    queue.append([cnt, time + n])

            # daca a trecut timpul de cooldown, revine in heap pentru a se executa
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])

        return time



        """Greedy

        În loc să simulăm întregul program, putem gândi în termeni de intervale:
        - Să presupunem că "max_freq" este frecvența maximă a oricărei sarcini
        (de exemplu, dacă A apare de 5 ori, iar B de 3 ori, atunci "max_freq" = 5).
        - Imaginăm că așezăm toate instanțele sarcinii celei mai frecvente una lângă alta:
        A _ A _ A _ A _ A
        - Există "max_freq" - 1 intervale între aceste sarcini cele mai frecvente.
        - Fiecare interval trebuie să aibă o dimensiune de cel puțin n pentru a
        respecta timpul de așteptare.
        - Deci, numărul inițial de sloturi libere necesare = ("max_freq" - 1) * n.

        Acum, încercăm să umplem aceste sloturi libere folosind alte sarcini:
        - Pentru fiecare altă sarcină cu frecventa c, aceasta poate umple până la
        min(c, "max_freq" - 1) dintre aceste spații libere
        (deoarece există doar "max_freq" - 1 spații libere).
        Cand c == "max_freq", minimul merge pe "max_freq" - 1.

        - Scădem această cantitate umplută din numărul de sloturi libere.
        - După ce am luat în considerare toate sarcinile, dacă timpul idle
        este încă pozitiv (adica daca mai avem idleluri), trebuie să adăugăm
        acele sloturi idle la timpul total.
        - Dacă timpul idle devine zero sau negativ, înseamnă că toate
        intervalele sunt deja umplute (sau supraîncărcate) de sarcini, deci nu
        este nevoie de timp idle suplimentar.

        Pentru ca: (de exemplu)
        - Am 4 sloturi obligatorii între cele 5 A-uri. Dacă am suficiente taskuri non-A
        ca să le umplu, atunci pot distribui aceste taskuri astfel încât și celelalte
        taskuri să respecte cooldown-ul. Si practic devine len(tasks)

        În concluzie:
        Timpul total = len(sarcini) (fiecare sarcină durează 1 unitate)
        + max(0, timp idle) (intervalele suplimentare pe care nu le-am putut umple).

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
        toate ocupă ultimul rând al structurii. (A si B de 4 ori)

        A _ _ | A _ _ | A _ _ | A B

        Așadar, timpul minim necesar pentru a programa toate sarcinile fără a
        încălca regulile de timp de așteptare este: 
          timp = ("max_freq" - 1) * (n + 1) + "max_count"

        Cu toate acestea, dacă numărul de sarcini este mai mare decât acest
        timp calculat, atunci simpla executare a tuturor sarcinilor durează mai mult.

        Astfel, răspunsul real trebuie să fie: max(len(sarcini), timp)

        T = O(m), S = O(1)
        """
        # count = [0] * 26
        # for task in tasks:
        #     count[ord(task) - ord('A')] += 1

        # max_freq = max(count)
        # max_count = 0
        # for i in count:
        #     max_count += 1 if i == max_freq else 0

        # time = (max_freq - 1) * (n + 1) + max_count
        # return max(len(tasks), time)
