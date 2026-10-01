import heapq
import collections


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
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

            if not max_heap:
                time = queue[0][1]
            else:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    queue.append([cnt, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])

        return time
