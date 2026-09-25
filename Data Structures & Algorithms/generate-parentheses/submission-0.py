class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """Brute Force

        Generează toate șirurile de lungime 2n folosind doar „(” și „)”.
        Cele mai multe vor fi nevalide, așa că pentru fiecare șir complet îl validăm:

        -Ține evidența unui sold (numărul de paranteze deschise).
        -„(” mărește soldul, „)” îl micșorează.
        -Dacă soldul devine vreodată negativ, înseamnă că există prea multe
        paranteze „)” apărute prea devreme, ceea ce este nevalid.
        -La final, soldul trebuie să fie 0, ceea ce înseamnă că toate
        parantezele deschise sunt închise.

        T = O(2^(2n) * n), S = O(2^(2n) * n)
        """
        # res = []

        # def valid(s: str):
        #     open = 0
        #     for c in s:
        #         open += 1 if c == '(' else -1
        #         if open < 0:
        #             return False
        #     return not open

        # def dfs(s: str):
        #     if n * 2 == len(s):
        #         if valid(s):
        #             res.append(s)
        #         return

        #     dfs(s + '(')
        #     dfs(s + ')')

        # dfs("")
        # return res



        """Backtracking

        În loc să generăm toate șirurile și apoi să verificăm validitatea
        acestora, construim doar șiruri valide.

        Reguli cheie pentru paranteze valide:
        -Poți adăuga „(” doar dacă mai ai paranteze deschise disponibile
        (open < n).
        -Poți adăuga „)” doar dacă acest lucru nu afectează validitatea
        (close < open).
        -Un șir este complet și valid numai când open == close == n.

        Așadar, la fiecare pas, facem numai alegeri sigure, ceea ce evită din\
        timp căile nevalide.

        T = O(4^n / sqrt(n)), S = O(n)
        """
        stack = []
        res = []

        def backtrack(open_n, closed_n):
            if open_n == closed_n == n:
                # every character in the stack join to a complete string
                res.append("".join(stack))
                return

            if open_n < n:
                stack.append("(")
                backtrack(open_n + 1, closed_n)
                stack.pop()

            if closed_n < open_n:
                stack.append(")")
                backtrack(open_n, closed_n + 1)
                stack.pop()

        backtrack(0, 0)
        return res
