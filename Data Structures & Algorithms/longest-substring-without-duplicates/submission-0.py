class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Brute Force

        Un approach straightforward ar fi sa consider fiecare caracter ca inceput
        de substring si sa continui sa extind substringul pana gasesc un duplicat.
        Cand am gasit un duplicat, iau lungimea setului si o salvez. Se garanteaza
        gasirea lungimii maxime pentru un substring fara duplicate dar solutia
        este ineficienta.

        T = O(n^2), S = O(1)
        """
        # result = 0

        # for i in range(len(s)):
        #     chars = set()
        #     for j in range(i, len(s)):
        #         if s[j] in chars:
        #             break
        #         chars.add(s[j])
        #     result = max(result, len(chars))

        # return result



        """Sliding Window

        In loc sa resetez prima pozitie pe fiecare index, tinem un window
        de caractere care are mereu caractere unice. Se exapndeaza mutand
        pointerul drept cate o pozitie. In momnetul in care am gasit un duplicat,
        shrinkuim windowul de la pointerul stang pana eliminam prima aparitie
        a caracterului. (pentu ca duplciatul gasit in dreapta sa devina unic
        si sa puntem in continuare sa avansam). In acest mod, windowul reprezinta
        mereu un substring valid si la fiecare expandare calculam si retinem 
        lungimea maxima. Este eficient pentru ca e o solutie liniara unde fiecare
        caracter este adaugat si scos cel mult o data.

        m - total number of unique chars
        T = O(n), S = O(m)
        """
        chars = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in chars:
                # remove all chars from left till the char from right is unique
                chars.remove(s[left])
                left += 1

            chars.add(s[right])
            result = max(result, right - left + 1)

        return result
