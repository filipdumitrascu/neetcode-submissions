class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """Brute Force   TLE

        O idee burte force ar fi sa consideram fiecare bara ca fiind cea mai
        scurta bara din dreptunghi. Pentru a afla cat de mult se poate extinde
        dreapta-stanga dreptunghiul cu aceasta inaltime, ne uitam stanga dreapta
        si obtinem cel mai indepartat indice care are cel putin acesata inaltime.
        Latimea obtinuta ne da cel mai mare dreptunghi cu aceasta inaltime limita.
        Repetam pentru toate barile si obtinem cea mai mare arie posibila. 

        T = O(n^2), S = O(1)
        """
        # max_area = 0

        # for i in range(len(heights)):
        #     height = heights[i]

        #     right_most = i + 1
        #     while right_most < len(heights) and heights[right_most] >= height:
        #         right_most += 1

        #     left_most = i
        #     while left_most >= 0 and heights[left_most] >= height:
        #         left_most -= 1

        #     left_most += 1
        #     right_most -= 1

        #     max_area = max(max_area, height * (right_most - left_most + 1))
        # return max_area



        """Stack

        Vrem, pentru fiecare barq, zona cea mai larga in care aceasta poate
        actiona ca cea mai scurta bară (similar brute force).
        Cu o singura trecere si o stiva, putem face acest lucru pe loc:
         Pastram o stiva de bare ordonate in functie de inaltime, crescanda,
        fiecare fiind stocata impreuna cu cel mai mic indice de la care poate
        incepe acea inaltime.
         Cand intalnim o noua bara mai scurta decat cea de sus din stiva, inseamna
        ca bara mai inalta de deasupra nu se poate extinde mai departe spre dreapta.
          Așadar, o scoatem din stiva si calculam aria pe care ar putea-o acoperi.
        Noua bara mai scurta poate incepe de la stanga, de la indexul de inceput al barei
        scoase din stiva, așa ca reutilizam acel index. Dupa trecere, calculam
        ariile pentru orice bare ramase in stiva, extinzandu-le pana la capat.
        Fiecare bara este introdusa si scoasa din stiva cel mult o data, oferind
        o solutie eficienta, cu o singura trecere.

        T = O(n), S = O(n)
        """
        max_area = 0
        stack: list[tuple[int, int]] = []  # (index, height)

        for current_index, current_height in enumerate(heights):
            start = current_index

            # pop the heights (from the stack) that are higher than
            # the current one. (they can't be extended to the right anymore)
            while stack and stack[-1][1] > current_height:
                prev_index, prev_height = stack.pop()
                max_area = max(max_area, prev_height * (current_index - prev_index))

                # extend to the left the lower height (the current one)
                start = prev_index

            stack.append((start, current_height))

        # there can still be heights with area not calculated
        # (the ones which reached to the end)
        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))

        return max_area
