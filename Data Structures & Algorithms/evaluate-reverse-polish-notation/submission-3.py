class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """Brute Force

        Notatia poloneza inversa (RPN) evalueaza expresiile fara paranteze
        prin aplicarea fiecarui operator asupra celor doua numere cele mai recente.
        O idee brute force este de a scana lista in mod repetat pana cand gasim
        un operator. Cand il gasim, luam cele doua numere dinaintea lui, calculam
        rezultatul si inlocuim toate cele trei tokenuri cu rezultatul. Continuam
        sa comprimam lista in acest mod pana cand ramane o singura valoare
        raspunsul final. Aceasta abordare functioneaza, dar este lenta, deoarece
        reconstruim si rescaneaza lista in mod repetat.

        T = O(n^2), S = O(n)
        """
        # while len(tokens) > 1:
        #     for i in range(len(tokens)):
        #         if tokens[i] not in "+-*/":
        #             continue

        #         a = int(tokens[i - 2])
        #         b = int(tokens[i - 1])

        #         match tokens[i]:
        #             case '+':
        #                 result = a + b
        #             case '-':
        #                 result = a - b
        #             case '*':
        #                 result = a * b
        #             case '/':
        #                 result = int(a / b)

        #         tokens = tokens[: i - 2] + [str(result)] + tokens[i + 1:]
        #         break

        # return int(tokens[0])


        """Recursion

        Notatia poloneza inversa functioneaza in mod natural cu recursivitatea,
        deoarece fiecare operator se aplica celor doua valori cele mai recente
        care il preced. Daca procesam expresia de la sfarsit, de fiecare data
        cand intalnim:
         un numar → acesta este pur si simplu returnat ca valoare
         un operator → evaluam recursiv cele doua valori care îi apartin

        Astfel se creeaza un arbore de evaluare natural:
         Fiecare operator devine un apel recursiv,
         Fiecare numar devine un caz de baza,
         Iar valoarea finala returnată este expresia evaluată in intregime.
        Această abordare este clara, eleganta si reflecta structura RPN in sine.

        T = O(n), S = O(n)
        """
        # def dfs() -> int:
        #     token = tokens.pop()
        #     if token not in "+-*/":
        #         return int(token)

        #     right = dfs()
        #     left = dfs()

        #     match token:
        #         case '+':
        #             return left + right
        #         case '-':
        #             return left - right
        #         case '*':
        #             return left * right
        #         case '/':
        #             return int(left / right)

        # return dfs()


        """Stack

        Un stack se potriveste perfect cu notatia poloneza inversa, deoarece
        cele mai recente numere sunt intotdeauna cele folosite in continuare.
        Pe masura ce analizam token-urile:
         Cand intalnim un numar, il introducem in stiva.
         Cand intalnim un operator, extragem primele doua numere din stiva,
        aplicam operația, si introducem rezultatul inapoi in stiva. In acest fel,
        stiva contine intotdeauna rezultatele intermediare, iar valoarea finala
        ramasa este raspunsul. Este o metoda clara, eficienta si respecta intocmai
        modul in care trebuie evaluata notatia poloneza inversa (RPN).

        T = O(n), S = O(n)
        """
        stack = []
        for token in tokens:
            match token:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '-':
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '/':
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b / a))
                case _:
                    stack.append(int(token))

        return stack[0]
