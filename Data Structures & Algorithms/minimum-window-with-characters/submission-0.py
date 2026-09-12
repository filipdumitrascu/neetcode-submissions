class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Brute Force

        Ne dorim cel mai mic susbtring din s care corntine toate caracterele
        din t, cu aceeasi frecventa. (dar nu numai, poate contine si alte
        caractere). Pentru aceasta verificare, declaram 2 hash mapuri, unul
        pentru t si unul pentru substringurile din s. Cand caracterele din t
        au atins aceeasi frecventa in substringul din s, retinem lungimea
        substringului. Astfel, suntem obligati sa parcurgem toate substringurile
        pentru a vedea lungimea minima, de unde reiese ineficienta approachului
        brute force, intrucat verficam overlapping susbtrings, aceleasi caractere
        de mai multe ori.

        n - len(s), k - total number of unique characters in s and t
        T = O(n^2), S = O(k)
        """
        # if len(s) < len(t):
        #     return ""

        # freq_t = {}
        # for c in t:
        #     freq_t[c] = 1 + freq_t.get(c, 0)

        # result = (-1, 1)
        # result_len = float("inf")
        # need = len(freq_t)

        # for i in range(len(s)):
        #     freq_s = {}
        #     have = 0
        #     for j in range(i, len(s)):
        #         freq_s[s[j]] = 1 + freq_s.get(s[j], 0)

        #         if freq_s[s[j]] == freq_t.get(s[j], 0):
        #             have += 1

        #         if have == need and (j - i + 1) < result_len:
        #             result_len = j - i + 1
        #             result = (i, j)

        # left, right = result
        # return s[left: right + 1] if result_len != float("inf") else ""



        """Sliding Window

        In loc sa verificam toate substringurile, folosim un sliding window.
        Il extindem la dreapta pana cand avem toate frecventele caracterelor din
        t si pe urma incercam sa gasim o lungime mai mica a substringului
        shrinkuind de la stanga. Daca o frecventa din t se pierde, cu left
        fixat reincepem extinderea in dreapta. Astfel, intai ne asiguram
        ca calculam lungimi pentru susbtringuri valide si pe urma incercam sa le
        micsoram lungimea, totul in timp liniar.

        n - len(s), k - total number of unique characters in s and t
        T = O(n), S = O(k)
        """
        if len(s) < len(t):
            return ""

        window = {}
        freq_t = {}
        for c in t:
            freq_t[c] = 1 + freq_t.get(c, 0)

        have = 0
        need = len(freq_t)

        result = (-1, 1)
        result_len = float("inf")

        left = 0
        for right in range(len(s)):
            window[s[right]] = 1 + window.get(s[right], 0)

            if freq_t.get(s[right], 0) == window[s[right]]:
                have += 1

            while have == need:
                if right - left + 1 < result_len:
                    result_len = right - left + 1
                    result = (left, right)

                window[s[left]] -= 1
                if window[s[left]] < freq_t.get(s[left], 0):
                    have -= 1

                left += 1

        left, right = result
        return s[left: right + 1] if result_len != float("inf") else ""
