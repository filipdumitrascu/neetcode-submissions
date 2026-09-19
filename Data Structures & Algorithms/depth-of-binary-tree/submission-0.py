from typing import Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """Recursive DFS
        
        Algoritmul DFS recursiv calculează adâncimea maximă a unui arbore
        binar prin explorarea fiecărui nod.
        Ideea este simplă:

        -Adâncimea unui arbore = 1 + adâncimea maximă a subarborilor săi
        stâng și drept.
        -Dacă un nod este None, adâncimea sa este 0.

        Așadar, pentru fiecare nod:
        -Se calculează recursiv adâncimea subarborelui stâng.
        -Se calculează recursiv adâncimea subarborelui din dreapta.
        -Se ia valoarea maximă dintre cele două.
        -Se adaugă 1 pentru nodul curent.

        h - log n (balanced tree) or n (degenerate tree)
        T = O(n), S = O(h)
        """
        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



        """Iterative DFS

        În loc să ne bazăm pe recursivitate pentru a explora arborele, putem
        simula DFS în mod explicit folosind o stivă. Stiva va stoca perechi
        formate din:
        -nodul curent
        -adâncimea acelui nod în arbore

        De fiecare dată când extragem un nod din stivă:
        -Actualizăm adâncimea maximă observată până în acel moment.
        -Introducem în stivă copiii săi din stânga și din dreapta, cu adâncimea + 1.

        Această abordare funcționează ca o căutare în adâncime (DFS) manuală, în
        care ținem noi înșine evidența adâncimii.
        Ea evită recursivitatea și este utilă atunci când adâncimea recursivă
        poate deveni prea mare.

        T = O(n), S = O(n)
        """
        # if not root:
        #     return 0

        # stack = [(root, 1)]
        # max_depth = 1

        # while stack:
        #     node, depth = stack.pop()
        #     max_depth = max(max_depth, depth)

        #     if node.left:
        #         stack.append((node.left, depth + 1))

        #     if node.right:
        #         stack.append((node.right, depth + 1))

        # return max_depth



        """BFS

        Căutarea în lățime (BFS) parcurge arborele nivel cu nivel.
        Acest lucru o face perfectă pentru calcularea adâncimii maxime, deoarece:
        -Fiecare iterație a BFS parcurge un nivel întreg al arborelui.
        -Astfel, fiecare nivel parcurs corespunde unei creșteri a adâncimii cu 1.
        Pur și simplu numărăm câte niveluri traversăm până când coada rămâne goală.

        Gândiți-vă la coadă ca la o frontieră în mișcare:
        -Începeți cu rădăcina → adâncime = 1
        -Adăugați copiii acesteia → adâncime = 2
        -Adăugați copiii acestora → adâncime = 3
        -Continuați până când nu mai rămân noduri.
        
        Numărul de niveluri procesate de BFS este exact adâncimea arborelui.

        T = O(n), S = O(n)
        """
        if not root:
            return 0

        queue = collections.deque([root])

        depth = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth += 1

        return depth
