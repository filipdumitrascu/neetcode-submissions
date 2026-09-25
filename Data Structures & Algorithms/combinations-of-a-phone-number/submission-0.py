class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """Backtracking

        Fiecare cifră corespunde unui set de caractere (ca pe tastatura unui
        telefon). Sarcina constă în a alege câte un caracter pentru fiecare
        cifră, în ordine, și a genera toate combinațiile posibile.

        Gândiți-vă la acest proces ca la construirea unui șir pas cu pas:
        -La indexul i, alegeți un caracter din corespondența cifrelor[i]
        -Treceți la următoarea cifră
        -Când lungimea șirului construit este egală cu numărul de cifre, am 
        format o combinație validă

        Aceasta este o problemă clasică de tip arbore de decizie:
        -Fiecare nivel - o cifră
        -Fiecare ramură - un caracter posibil pentru acea cifră

        Metoda backtracking ne permite să explorăm toate ramurile în mod
        eficient.

        T = O(n * 4^n), S = O(n)
        """
        if len(digits) == 0:
            return []

        keys = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def helper(inp):
            if inp == '':
                return ['']
            ans = []

            rest_strings = helper(inp[1:])
            key_ketter = keys[inp[0]]  # next digit to append

            for char in key_ketter:
                for word in rest_strings:
                    ans.append(char + word)

            return ans
        return helper(digits)



        """Iteration

        În loc să folosim recursivitatea, construim combinațiile nivel cu nivel.

        Începem cu un șir gol.
        Pentru fiecare cifră:

        Luăm toate combinațiile construite până în acel moment
        Adăugăm la capăt fiecare caracter posibil asociat cifrei curente
        Astfel se creează o nouă listă de combinații
        Acest procedeu este similar cu BFS / expansiunea nivel cu nivel:

        Fiecare cifră adaugă un nou „strat” de caractere
        Combinațiile se extind pas cu pas până când toate cifrele sunt procesate

        T = O(n * 4^n), S = O(n)
        """
        # if not digits:
        #     return []

        # res = [""]
        # digit_to_char = {
        #     "2": "abc",
        #     "3": "def",
        #     "4": "ghi",
        #     "5": "jkl",
        #     "6": "mno",
        #     "7": "qprs",
        #     "8": "tuv",
        #     "9": "wxyz",
        # }

        # for digit in digits:
        #     tmp = []
        #     for cur_str in res:
        #         for c in digit_to_char[digit]:
        #             tmp.append(cur_str + c)
        #     res = tmp
        # return res
