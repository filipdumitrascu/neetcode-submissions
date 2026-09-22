from typing import Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        """Recursive DFS

        Parcurgerea nivel cu nivel înseamnă vizitarea arborelui nivel cu nivel,
        de sus în jos. În cazul DFS, în loc să folosim o coadă, folosim
        recursivitatea și transmitem adâncimea curentă.

        De fiecare dată când ajungem la un nod:
         -Dacă este prima dată când vizităm această adâncime, creăm o listă
        nouă pentru nivelul respectiv.
         -Adăugăm valoarea nodului la lista corespunzătoare acelei adâncimi.
         -Explorăm recursiv copiii din stânga și din dreapta la adâncimea + 1.

        T = O(n), S = O(n)
        """
        # levels = []

        # def dfs(node: Optional[TreeNode], depth: int) -> None:
        #     if not node:
        #         return None

        #     if len(levels) == depth:
        #         levels.append([])

        #     levels[depth].append(node.val)
        #     dfs(node.left, depth + 1)
        #     dfs(node.right, depth + 1)

        # dfs(root, 0)
        # return levels



        """BFS

        Parcurgerea nivel cu nivel vizitează un arbore nivel cu nivel, de la 
        stânga la dreapta. Algoritmul BFS se potrivește în mod natural acestei
        abordări, deoarece procesează nodurile în ordinea în care apar,
        folosind o coadă.

        Ideea:
        -Se introduce nodul rădăcină în coadă.
        -Se extrag în mod repetat noduri din coadă; acestea formează
        nivelul curent.
        -Se adaugă copiii acestora în coadă; aceștia vor forma nivelul următor.
        -Se continuă până când coada este goală.
        Astfel se asigură că fiecare nod este vizitat în ordinea perfectă
        a nivelurilor.

        T = O(n), S = O(n)
        """
        levels = []
        queue = collections.deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()

                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if level:
                levels.append(level)

        return levels
