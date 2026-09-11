class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Brute Force

        Un substring este valid daca putem sa ii facem toate caracterele egale
        facand cel mult k modificari. Sansele cele mai mari de a realiza acest
        lucru este sa schimbam toate caracterele in caracterul care apare de
        cele mai multe ori. (ar fi cele mai putine modificari de facut)

        Ideea brute force este sa incercam orice substring posibil, incepand cu
        fiecare index. Astfel, expandam substringul si tinem cont de cat de des
        apare fiecare caracter. Daca numarul de modificari necesare
        (lungime - frecventa maxima caracter) este pana in k, updatam raspunsul.
        Logica de mai sus garanteaza ca solutia functioneaza dar verificarea
        tuturor susbtringurilor este ineficienta.

        T = O(n^2), S = O(1)
        """
        # result = 0
        # for i in range(len(s)):
        #     freq = {}
        #     max_freq = 0

        #     for j in range(i, len(s)):
        #         freq[s[j]] = freq.get(s[j], 0) + 1
        #         max_freq = max(max_freq, freq[s[j]])

        #         if j - i + 1 - max_freq <= k:
        #             result = max(result, j - i + 1)

        # return result



        """Sliding Window

        In loc sa luam fiecare substring incepand cu fiecare index, tinem un 
        window de caractere. Pe masura ce expandam windowul, tinem cont de
        frecventa fiecarui caracter si frecventa maxima. Momentul in care oprim
        expandarea windowului e acelasi ca la brute force:
        window size - frecventa celui mai frecvent caracter > k  si incepem
        shrinkuirea din stanga pana conditia redevine adevarata.

        Dupa srinkuire frecventa maxima este posibil falsa pentru ca nu o
        recalculam. Asta poate face windowul temporar valid chiar daca frecventa
        maxima este mai mica in realitate. Tot este corect pentru ca aceasta
        valoare falsa nu va ajuta la obtinerea unui rezultat mai bun decat cel
        care era atins cand frecventa maxima era accurate.

        T = O(n), S = O(n)
        """
        freq = {}
        result = 0

        left = 0
        max_freq = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(max_freq, freq[s[right]])

            while right - left + 1 - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
