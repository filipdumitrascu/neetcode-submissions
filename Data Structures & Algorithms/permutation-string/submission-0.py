class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Brute Force

        Problema se rezuma la a gasi un substring in s2 care este anagrama cu
        stringul s1. E nevoie de 2 tehnici aici:
        - iterarea prin substringurile lui s2
        - verificarea de anagrame
        Ideea brute force alege cele mai ineficiente metode pentru ambele tehnici.
        Se iau toate substringurile (orice lungime ce incepe cu orice caracter)
        si verificarea de anagrame se face prin sortare si comparare.
        (s1 sortat o data si comparat cu toate substringurile sortate)

        n - len(s2)
        T = O(n^3 log n), S = O(n)
        """
        # s1 = sorted(s1)

        # for i in range(len(s2)):
        #     for j in range(i, len(s2)):
        #         sub_string = s2[i: j + 1]

        #         if len(sub_string) != len(s1):
        #             continue

        #         sub_string = sorted(sub_string)

        #         if sub_string == s1:
        #             return True

        # return False



        """Hash Map

        O prima optimizare ar fi pentru verificarea de anagrame. In loc sa sortam,
        putem declara un hash map pentru s1 cu frecventa caracterelor si cate
        unul pentru fiecare substring. Daca in orice moment se depaseste frecventa
        unui anmit caracter din s1 in constructia substringului in s2, oprim
        construirea susbtringului cu acel caracter ca prim caracter. Iar daca
        in orice moment toate caracterele din s1 au aceeasi frecventa in s2, am
        gasit substringul anagram si intoarcem True.
        Astfel, verificarea de anagrame se face in timp constant cu ajutorul
        hash mapurilor dar tot producem munca repetitiva prin substringuti
        prentru ca resetam verificarea la orice pozitie.

        m - len(s1), n - len(s2)
        T = O(n * m), S = O(1)
        """
        # count_s1 = {}
        # for c in s1:
        #     count_s1[c] = count_s1.get(c, 0) + 1

        # need = len(count_s1)
        # for i in range(len(s2)):
        #     count_s2 = {}
        #     have = 0

        #     for j in range(i, len(s2)):
        #         count_s2[s2[j]] = count_s2.get(s2[j], 0) + 1

        #         if count_s1.get(s2[j], 0) < count_s2[s2[j]]:
        #             break

        #         if count_s1[s2[j]] == count_s2[s2[j]]:
        #             have += 1

        #         if have == need:
        #             return True

        # return False



        """Sliding Window

        Avand in vdere ca susbtringul din s2 trebuie sa aiba aceeasi lungime
        ca stringul s1, putem folosi un sliding window de lungime fixa.
        Astfel, verificam doar substringurile ce pot produce rezultatul True,
        printr o iterare liniara a stringului s2. Verificarea de anagrame e
        aceeasi, 2 hash mapuri (sau arrayuri daca stim cas doar cele 26 de litere a-z)
        ce trebuie sa aiba aceeasi frecventa pe toate caracterele. Pe masura ce
        mutam windowul pe s2, updatam frecventele eliminiand caracterul din stanga
        si adaugandu l pe cel din dreapta. Sunt singurele 2 modificari, nu e
        nevoie sa recalculam toate frecventele in s2.

        m - len(s1), n - len(s2)
        T = O(n), S = O(1)
        """
        if len(s1) > len(s2):
            return False

        target_count = [0] * 26  # s1
        window_count = [0] * 26  # s2

        for i in range(len(s1)):
            target_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if target_count[i] == window_count[i] else 0)

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Add right character
            index = ord(s2[right]) - ord('a')
            window_count[index] += 1

            if window_count[index] == target_count[index]:
                matches += 1
            elif window_count[index] - 1 == target_count[index]:
                matches -= 1


            # Remove left character
            index = ord(s2[left]) - ord('a')
            window_count[index] -= 1

            if window_count[index] == target_count[index]:
                matches += 1
            elif window_count[index] + 1 == target_count[index]:
                matches -= 1

            left += 1

        return matches == 26
