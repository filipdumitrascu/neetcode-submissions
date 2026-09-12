class Solution:
    def isValid(self, s: str) -> bool:
        """Brute Force

        O pereche de paranteze este valida daca cea deschisa apare cu matchul
        ei langa ea: "()", "{}", "[]". Astfel, pentru a declara stringul valid
        o idee straightforward este sa parcurgem repetitiv stringul si sa
        eliminam fiecare match. Daca dupa fiecare match elminiat (si cele formate
        ulterior) stringul e vid, acesta a fost initial valid. 
        Altfel, daca nu e vid, strimgul initial nu era valid.
        E o solutie ineficienta pentru ca parcurgem stringul de mai multe ori,
        si il reconstruim de fiecare data cand eliminam un set de paranteze.

        T = O(n^2), S = O(n)
        """
        # while '()' in s or '{}' in s or '[]' in s:
        #     s = s.replace('()', '')
        #     s = s.replace('{}', '')
        #     s = s.replace('[]', '')
        
        # return s == ''



        """Stack

        Cand o paranteza inchisa se intalneste, aceasta se matchuieste cu ultima
        deschisa. Practic ultima paranteza deschisa din string e prima care se
        matchuieste cu una inchisa. LIFO fiind principul stackului, aceasta
        structura de date ne ajuta eficient sa determinam daca stingul e valid
        sau nu. Introducem in stack doar parantezele deschise. Cand intalnim
        una inchisa verificam daca se matchuieste cu topul stackului. Daca nu,
        stringul e invalid. Altfel continuma pana terminam stringul si in caz in
        care nu au ramas in stack paranteze deschise nematchuite, stringul e valid.

        T = O(n), S = O(n)
        """
        stack = []
        close_to_open = { ")": "(", "]": "[", "}": "{"}

        for char in s:
            # if char is a close
            if char in close_to_open:
                # stack not empty and last elem in stack
                # is the matching parentheses
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False
