class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """Stack

        Masinile au o pozitie initiala si o viteza. Daca prind o masina din
        fata intr o pozitie inainte sau chiar pe target, devin acelasi "fleet"
        cu viteza masinii din fata (care e mai mica din moment ce a prins-o).
        Astfel, procesam masinile invers, de la cea mai apropiata de target
        la cea mai indepartata si calculam timpul exact necesar de a ajunge la
        target. In cazul in care o masina indepartata are timpul mai mic sau egal
        cu cea curenta, inseamna ca acestea vor forma un fleet si le numaram
        impreuna. De aici se foloseste stack, ultima masina procesta poate fi
        si prima masina care se scoate din numaratoare intrucat se grupeaza
        in fleet cu una deja existenta. Astfel, din stack se scot masinilie care
        se grupeaza, intra intr un fleet si raman doar fleeturile in sine.
        Bottleneckul este sortarea, necesara pentru logica solutiei.

        T = O(n log n), S = O(n)
        """
        pairs = sorted(zip(position, speed), key=lambda pair: pair[0], reverse=True)
        stack = []

        for position, speed in pairs:
            stack.append((target - position) / speed)  # time left to reach target

            if len(stack) >= 2 and stack[-1] <= stack[-2]:  # collision
                stack.pop()

        return len(stack)



        """ Interation

        Stackul scoate din el masinile care intrau in fleet cu alte masini deja
        in stack. Practic calcula din numarul de masini totale cate se intalnesc
        cu altele si asa ajungea la numarul de fleeturi. In schimb, in approachul
        asta, daca masinii curente ii ia mai mult timp sa ajunga la target decat
        fleetul din fata ei, se numara ca fleet individual. Practic aici plecam
        de la un fleet si crestem, nu de la n fleeturi si scadem.

        T = O(n log n), S = O(n)
        """
        # pairs = sorted(zip(position, speed), key=lambda pair: pair[0], reverse=True)

        # fleets = 1
        # prev_time = (target - pairs[0][0]) / pairs[0][1]

        # for i in range(1, len(pairs)):
        #     curr_time = (target - pairs[i][0]) / pairs[i][1]

        #     if curr_time > prev_time:  # nu ajunge mai repede sau tot atunci ca masina din fata
        #         fleets += 1
        #         prev_time = curr_time

        # return fleets
