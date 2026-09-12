class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """Brute Force

        Pentru fiecare zi, pur si simplu cautam ziua urmatoare cu o temperatura
        mai ridicata. Comparam ziua curenta cu fiecare zi viitoare pana cand
        fie gasim una mai calda, fie ajungem la sfarsit.
         Daca gasim o zi mai calda, inregistram cate zile a durat.
         Daca nu, raspunsul este 0.
        Aceasta metoda este usor de inteles, dar lenta, deoarece in fiecare zi
        se pot analiza multe zile in avans.

        T = O(n^2), S = O(1)
        """
        # result = []

        # for i in range(len(temperatures)):
        #     count = 1
        #     j = i + 1

        #     while j < len(temperatures):
        #         if temperatures[j] > temperatures[i]:
        #             break
        #         j += 1
        #         count += 1

        #     count = 0 if j == len(temperatures) else count
        #     result.append(count)

        # return result



        """Stack

        Vrem sa aflam cat timp dureaza pana apare o zi mai calda pentru fiecare
        temperatura. Un stack ne ajuta, deoarece tine evidenta zilelor care
        inca asteapta o temperatura mai ridicata. Pe masura ce parcurgem lista
        inainte, ori de cate ori gasim o temperatura mai ridicata decat cea din
        varful stivei, inseamna ca tocmai am descoperit „urmatoarea zi mai calda”
        pentru acea zi anterioara. O scoatem din stiva, calculam diferenta in zile
        si continuam. In acest fel, fiecare zi este introdusa si scoasa din stiva
        cel mult o singura data, ceea ce face procesul eficient.

        T = O(n), S = O(n)
        """
        result = [0] * len(temperatures)
        stack: list[tuple[int, int]] = []  # (temp, index)

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, stack_index = stack.pop()
                result[stack_index] = index - stack_index

            stack.append((temp, index))

        return result
