from typing import Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Recursive DFS

        Doi arbori binari sunt identici dacă:
        -Structura lor este identică.
        -Nodurile corespunzătoare au aceleași valori.

        Așadar, în fiecare poziție:
        -Dacă ambele noduri sunt nule → se potrivesc.
        -Dacă unul este nul, dar celălalt nu → nu se potrivesc.
        -Dacă ambii există, dar valorile diferă → nu se potrivesc.
        -În caz contrar, se compară recursiv subarborii lor stângi și subarborii lor drepți.

        Aceasta este o comparație DFS directă, bazată pe structură și valori.

        h - log n (balanced tree) or n (degenerate tree)
        T = O(n), S = O(h)
        """
        # if not p and not q:
        #     return True

        # if p and q and p.val == q.val:
        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # return False



        """Iterative DFS

        În loc să folosim recursivitatea, putem folosi o stivă explicită pentru a
        compara cei doi arbori. Fiecare element al stivei conține o pereche de noduri
        — câte unul din fiecare arbore — care ar trebui să se potrivească.

        Pentru fiecare pereche:
        -Dacă ambele sunt nule, se potrivesc → continuăm.
        -Dacă doar unul este nul sau valorile lor diferă → arborii nu sunt identici.
        -Dacă se potrivesc, adăugăm copiii lor în aceeași ordine:
         -Perechea de copii din stânga
         -Perechea de copii din dreapta

        Dacă terminăm de procesat toate perechile fără neconcordanțe, arborii sunt identici.


        T = O(n), S = O(n)
        """
        # stack = [(p, q)]

        # while stack:
        #     node1, node2 = stack.pop()

        #     if not node1 and not node2:
        #         continue

        #     if not node1 or not node2 or node1.val != node2.val:
        #         return False
            
        #     stack.append((node1.left, node2.left))
        #     stack.append((node1.right, node2.right))

        # return True



        """BFS

        Algoritmul BFS (parcurgere pe niveluri) ne permite să comparăm cei
        doi arbori nivel cu nivel. Menținem două cozi — câte una pentru fiecare arbore.
        La fiecare pas, eliminăm o pereche de noduri care ar trebui să se potrivească:

        -Dacă ambele noduri sunt nule, se potrivesc → continuăm.
        -Dacă doar unul este nul sau valorile lor diferă → arborii nu sunt identici.
        -Dacă se potrivesc, introducem copiii lor în cozile respective
        în aceeași ordine: mai întâi copilul din stânga, apoi cel din dreapta.

        T = O(n), S = O(n)
        """
        queue = collections.deque([(p, q)])

        while queue:
            for _ in range(len(queue)):
                node_p, node_q = queue.popleft()

                if not node_p and not node_q:
                    continue

                if not node_p or not node_q or node_p.val !=  node_q.val:
                    return False

                queue.append((node_p.left, node_q.left))
                queue.append((node_p.right, node_q.right))

        return True
