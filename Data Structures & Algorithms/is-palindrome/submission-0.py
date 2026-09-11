class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Reverse String

        Pentru a verifica ca un string este palindrom, tinem evidenta doar a
        literelor si a digiturilor, restul poate fi ignorat. Putem construi o
        forma normalizata a stringului (spatiu auxiliar n, timp n) care contine
        doar caractere alpha numerice, toate converite lowercase pentru consistenta.

        De aici devine simplu: un string e palindrom daca este identic cu forma
        lui reversed. (spatiu auxiliar pentru reverse n, timp pentru reverse n)
        (timp pentru comparare n)

        T = O(3n) = O(n), S = O(2n) = O(n)
        """
        # normalized_str = ''.join(char.lower() for char in s if char.isalnum())
        # return normalized_str == normalized_str[::-1]



        """Two Pointers

        In loc sa construim stringul normalizat, putem verifica daca e palindrom
        in place. Pointerul left pe primul caracter se compara (case insensitive)
        cu pointerul right de pe ultimul caracter. Se evita caracterele non alpha
        numerice iar pointerii se indreapta treptat catre centru. Daca in orice
        moment caractrele nu sunt egale, stringul nu este palindrom. Aceasta metoda
        evita spatiul extra si parcurge stringul doar o data.

        T = O(n), S = O(1)
        """
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
