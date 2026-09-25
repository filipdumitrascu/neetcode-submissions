from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """Brute Force

        Un arbore de căutare binar (BST) are o proprietate specială:

        subarborele stâng < rădăcina < subarborele drept
        Însă această metodă de tip „forță brută” nu utilizează proprietatea BST.
        Pur și simplu:

        Parcurgem întregul arbore și colectăm toate valorile nodurilor.
        Sortăm valorile colectate.
        Al k-lea element ca mărime se află la indexul k-1 în lista sortată.


        T = O(n log n), S = O(n)
        """
        # arr = []

        # def dfs(node):
        #     if not node:
        #         return

        #     arr.append(node.val)
        #     dfs(node.left)
        #     dfs(node.right)

        # dfs(root)
        # arr.sort()
        # return arr[k - 1]



        """Inorder Traversal

        Un arbore de căutare binar (BST) are o proprietate importantă:

        Parcurgerea în ordine (Stânga → Nod → Dreapta) oferă întotdeauna
        valorile în ordine sortată.

        Așadar, în loc să colectăm toate valorile și să le sortăm manual, putem:

        Efectua o parcurgere în ordine.
        Aceasta generează automat valorile în ordine crescătoare.
        Al k-lea element din această listă în ordine este răspunsul.
        Acest lucru face ca soluția să fie mai eficientă și utilizează structura
        inerentă a BST-ului.

        T = O(n), S = O(n)
        """
        # nodes = []

        # def dfs(node: Optional[TreeNode]) -> None:
        #     if not node:
        #         return

        #     dfs(node.left)
        #     nodes.append(node.val)
        #     dfs(node.right)

        # dfs(root)
        # return nodes[k - 1]



        """Recursive DFS

        Într-un BST, parcurgerea în ordine intermediară (Stânga → Nod → Dreapta)
        vizitează în mod natural nodurile într-o ordine sortată.

        Așadar, în loc să stocăm toate valorile, putem:

        Să parcurgem arborele în ordine intermediară,
        Să numărăm nodurile pe măsură ce le vizităm,
        Să ne oprim imediat ce ajungem la al k-lea nod ca mărime.
        Astfel se evită stocarea tuturor valorilor nodurilor, iar întoarcerea
        timpurie ne permite să ne oprim odată ce a fost găsit al k-lea nod ca
        mărime.

        T = O(n), S = O(n)
        """
        # count = k
        # result = root.val

        # def dfs(node: Optional[TreeNode]) -> None:
        #     nonlocal count, result
        #     if not node:
        #         return

        #     dfs(node.left)
        #     if count == 0:
        #         return

        #     count -= 1
        #     if count == 0:
        #         result = node.val
        #         return

        #     dfs(node.right)

        # dfs(root)
        # return result



        """Iterative DFS

        Într-un BST, o traversare în ordine (stânga -> nod -> dreapta) prezintă
        nodurile în ordine sortată.
        În loc de recursivitate, simulăm această traversare cu ajutorul unei
        stive:
        -Adăugăm toți nodurile din stânga (coborâm cât mai adânc posibil).
        -Extragem nodul de sus - acesta este următoarea valoare mai mică.
        -Trecem la subarborele său din dreapta și repetăm.
        -Când extragem al k-lea nod, acesta este răspunsul nostru.

        În acest fel, vizităm nodurile doar până ajungem la al k-lea cel mai
        mic — nu este nevoie să parcurgem întregul arbore.

        T = O(n), S = O(n)
        """
        # stack = []
        # curr = root

        # while stack or curr:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left

        #     curr = stack.pop()
        #     k -= 1

        #     if k == 0:
        #         return curr.val
        #     curr = curr.right

        # return curr.val



        """Morris Traversal

        Parcurgerea în ordine a unui arbore binar sortat (BST) oferă valorile
        în ordine sortată, astfel încât al k-lea nod vizitat este al k-lea cel
        mai mic.
        Însă recursivitatea și stivele consumă spațiu suplimentar.

        Parcurgerea Morris ne permite să efectuăm o parcurgere în ordine
        folosind un spațiu suplimentar de complexitate O(1), prin crearea
        temporară a unui thread (un pointer spre dreapta) de la predecesorul
        unui nod înapoi către nodul respectiv.

        Pentru fiecare nod:
        -Dacă nu are un copil stâng - îl vizităm direct.
        -Dacă are un copil stâng - găsim predecesorul său în inordine.
         -Dacă pointerul drept al predecesorului este gol - creăm o legătură
         temporară către nodul curent și ne deplasăm spre stânga.
         -Dacă pointerul drept al predecesorului indică deja nodul curent -
         eliminăm legătura, vizităm nodul și ne deplasăm spre dreapta.
        Scădem valoarea lui k de fiecare dată când „vizităm” un nod.
        Nodul la care k devine 0 este al k-lea cel mai mic.

        Această metodă funcționează deoarece simulăm ordinea inorder fără
        a folosi memorie suplimentară.

        T = O(n), S = O(1)
        """
        curr = root

        while curr:
            if not curr.left:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right

        return -1
