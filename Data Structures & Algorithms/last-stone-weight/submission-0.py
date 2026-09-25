import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        """Sorting

        Trebuie să ciocnești întotdeauna cele două pietre cele mai grele una de alta.
        O modalitate simplă de a te asigura că faci acest lucru este:

        -Sortam lista de pietre astfel încât cele mai grele să se afle la sfârșit.
        -Elimină ultimele două pietre (cele cu cele mai mari valori).
        -Ciocnește-le:
          Dacă sunt egale → ambele dispar.
          Dacă sunt diferite → diferența devine o nouă piatră.
        -Inserează noua piatră (dacă există) înapoi în listă.
        -Repetă până când rămâne cel mult o singură piatră.

        Sortarea de fiecare dată nu este cea mai eficientă abordare, dar este
        simplă și ușor de implementat.

        T = O(n^2 log n), S = O(n)
        """
        # while len(stones) > 1:
        #     stones.sort()
        #     curr = stones.pop() - stones.pop()

        #     if curr != 0:
        #         stones.append(curr)
            
        # return stones[0] if stones else 0



        """Binary Search

        Întotdeauna spargem cele două pietre cele mai grele.
        Dacă păstrăm pietrele în ordine, cele două pietre cele mai grele se
        află la capătul arrayului, așa că le putem selecta cu ușurință.
        După spargere:
        -Îndepărtăm cele două pietre cele mai grele.
        -Dacă sunt diferite, diferența dintre ele devine o nouă piatră.
        -Pentru a menține lista sortată, trebuie să inserăm această nouă piatră
        în poziția corectă.

        În loc să scanăm liniar pentru a găsi poziția, folosim căutarea binară
        pentru a găsi rapid locul în care ar trebui să se afle această nouă
        piatră în lista sortată, apoi mutăm elementele pentru a o insera acolo.
        Astfel, lista rămâne sortată pentru următoarea iterație.

        T = O(n^2), S = O(n)
        """
        # stones.sort()
        # n = len(stones)

        # while n > 1:
        #     curr = stones.pop() - stones.pop()
        #     n -= 2
        #     if curr > 0:
        #         left = 0
        #         right = n - 1
        #         while left <= right:
        #             mid = left + (right - left) // 2
        #             if stones[mid] < curr:
        #                 left = mid + 1
        #             else:
        #                 right = mid - 1
        #         pos = l
        #         n += 1
        #         stones.append(0)
        #         for i in range(n - 1, pos, -1):
        #             stones[i] = stones[i - 1]
        #         stones[pos] = curr

        # return stones[0] if n > 0 else 0



        """Max Heap

        Trebuie să eliminăm mereu, în mod repetat, cele două pietre cele mai grele.
        Un max-heap este perfect pentru acest scop, deoarece ne permite să
        extragem eficient valorile cele mai mari.

        Majoritatea limbajelor de programare oferă min-heap-uri, așa că o
        strategie obișnuită este aceea de a stoca valori negative.
        Astfel, valoarea cea mai mică (cea mai negativă) reprezintă piatra
        cea mai mare.

        Proces:
        -Convertește toate pietrele în valori negative și construiește un heap.
        -Extrage în mod repetat cele două pietre cele mai mici (adică cele mai grele).
        -Distruge-le:
          Dacă sunt egale → ambele sunt distruse.
          Dacă sunt diferite → introduce valoarea negativă a diferenței dintre
          ele înapoi în heap.
        -Când rămâne o singură piatră sau niciuna, returnează greutatea rămasă
        sau 0.

        T = O(n log n), S = O(n)
        """
        # stones_heap = [-s for s in stones]

        # heapq.heapify(stones_heap)
        # while len(stones_heap) > 1:
        #     first_stone = heapq.heappop(stones_heap)
        #     second_stone = heapq.heappop(stones_heap)

        #     if second_stone > first_stone:
        #         heapq.heappush(stones_heap, first_stone - second_stone)

        # return abs(stones_heap[0]) if stones_heap else 0



        """Bucket Sort

        Deoarece toate valorile pietrelor se încadrează într-un interval numeric
        limitat, putem evita sortarea sau utilizarea unui heap prin folosirea
        sortării pe intervale / numărării frecvențelor.

        In loc să ținem evidența fiecărei pietre în parte, stocăm numărul de
        pietre existente pentru fiecare greutate posibilă.

        Idei cheie:
        -Să presupunem că bucket[w] stochează numărul de pietre cu greutatea w
        pe care le avem.
        -Căutăm în mod repetat cea mai grea piatră disponibilă.
        -Când spargem pietrele cu greutățile a și b:
          Dacă a == b, acestea se anulează reciproc.
          Dacă sunt diferite, piatra rămasă a - b este adăugată înapoi în bucket.
        -Continuăm până când rămâne o singură greutate diferită de zero.

        Acest lucru funcționează deoarece operațiunile cu bucket-ul
        (incrementare, decrementare, scanare) sunt eficiente atunci când
        intervalul de greutăți este gestionabil.

        n - len(stones),  w - max(stones)
        T = O(n + w), S = O(w)
        """
        max_stone = max(stones)
        bucket = [0] * (max_stone + 1)
        for stone in stones:
            bucket[stone] += 1

        first = max_stone
        second = max_stone
        while first > 0:
            if bucket[first] % 2 == 0:
                first -= 1
                continue

            j = min(first - 1, second)
            while j > 0 and bucket[j] == 0:
                j -= 1

            if j == 0:
                return first

            second = j
            bucket[first] -= 1
            bucket[second] -= 1

            bucket[first - second] += 1
            first = max(first - second, second)

        return first
