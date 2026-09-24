from typing import Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        """Recursive DFS

        Pentru a vedea partea dreaptă a unui arbore, la fiecare adâncime ne
        interesează doar primul nod pe care îl întâlnim privind dinspre dreapta.

        Dacă efectuăm o căutare în adâncime (DFS) vizitând:
        1.mai întâi copilul din dreapta, apoi
        2.copilul din stânga
        … atunci primul nod la care ajungem la fiecare adâncime este nodul
        vizibil din partea dreaptă.

        Stocăm acel nod în momentul în care ajungem pentru prima dată
        la acea adâncime.

        T = O(n), S = O(n)
        """
        # result = []

        # def dfs(node: Optional[TreeNode], depth: int) -> None:
        #     if not node:
        #         return None

        #     if depth == len(result):
        #         result.append(node.val)

        #     dfs(node.right, depth + 1)
        #     dfs(node.left, depth + 1)

        # dfs(root, 0)
        # return result



        """BFS

        În BFS explorăm arborele nivel cu nivel.
        Dacă analizăm fiecare nivel de la stânga la dreapta, ultimul nod pe
        care îl întâlnim la acel nivel este cel vizibil din partea dreaptă.

        Așadar, pentru fiecare nivel:

        Parcurgem toate nodurile.
        Reținem nodul situat cel mai la dreapta.
        Îl adăugăm la răspuns.

        T = O(n), S = O(n)
        """
        if not root:
            return []

        result = []
        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            for index in range(level_size):
                node = queue.popleft()

                if index == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result
