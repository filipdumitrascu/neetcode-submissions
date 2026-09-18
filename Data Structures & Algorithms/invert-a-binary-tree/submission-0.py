import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Recursive DFS

        Inversarea unui arbore binar înseamnă schimbarea între subarborele
        stâng și cel drept al fiecărui nod. Cu ajutorul căutării în adancime
        (DFS), folosim recursivitatea pentru a inversa arborele de sus în jos:

        -La fiecare nod, schimbăm între ele copiii stâng și drept.
        -Apoi inversăm recursiv subarborele stâng.
        -Inversăm recursiv subarborele din dreapta.

        Deoarece fiecare subarbore este la rândul său un arbore binar mai mic,
        recursivitatea gestionează în mod natural această structură.
        Inversarea are loc în timpul coborârii recursive, iar fiecare subarbore
        este oglindit corect.

        T = O(n), S = O(n)
        """
        # def dfs(root: Optional[TreeNode]) -> None:
        #     if not root:
        #         return

        #     root.left, root.right = root.right, root.left

        #     dfs(root.left)
        #     dfs(root.right)

        # dfs(root)
        # return root



        """Iterative DFS

        DFS iterativ inversează un arbore binar folosind o stivă explicită în
        loc de recursivitate. Ideea este aceeași ca în cazul DFS recursiv:

        -Se vizitează un nod.
        -Se schimbă între ele copiii săi din stânga și din dreapta.
        -Continuăm procesul pentru copiii acestuia.

        Însă, în loc de stiva de apeluri, folosim propria noastră structură
        de date de tip stivă.
        Procesul este următorul:

        -Introducem rădăcina în stivă.
        -Extragem nodul de sus, schimbăm între ei copiii acestuia.
        -Introducem copiii acestuia în stivă (dacă există).
        -Continuăm până când stiva este goală.

        Aceasta simulează DFS-ul recursiv într-o manieră iterativă și
        funcționează bine atunci când adâncimea recursivității poate fi prea mare.

        T = O(n), S = O(n)
        """
        # if not root:
        #     return None

        # stack = [root]

        # while stack:
        #     node = stack.pop()

        #     node.left, node.right = node.right, node.left

        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)

        # return root



        """BFS

        Pentru a inversa (oglindi) un arbore binar, fiecare nod trebuie să-și
        schimbe între ele copiii din stânga și din dreapta. Folosind căutarea
        în lățime (BFS), procesăm arborele nivel cu nivel:

        -Începem de la rădăcină.
        -Pentru fiecare nod, schimbăm între ele copiii acestuia.
        -Apoi introducem în coadă noii copii din stânga și din dreapta.
        -Continuăm până când fiecare nod a fost procesat.

        Această abordare asigură că fiecare nod este vizitat exact o singură
        dată și inversat imediat ce este întâlnit.

        T = O(n), S = O(n)
        """
        if not root:
            return None

        queue = collections.deque([root])
        while queue:
            node = queue.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
