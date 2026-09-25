import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """Recursive DFS

        Un nod este „bun” dacă, pe calea de la rădăcină la acel nod, niciun nod
        anterior nu are o valoare mai mare decât a acestuia. Așadar, pe măsură
        ce parcurgem arborele, trebuie doar să reținem valoarea maximă întâlnită
        până în acel moment pe calea curentă.

        Dacă valoarea nodului curent este ≥ acea valoare maximă → atunci este
        un nod bun.

        T = O(n), S = O(n)
        """
        # result = 0

        # def dfs(node: Optional[TreeNode], max_above: int) -> None:
        #     if not node:
        #         return

        #     nonlocal result
        #     if node.val >= max_above:
        #         max_above = node.val
        #         result += 1

        #     dfs(node.left, max_above)
        #     dfs(node.right, max_above)

        # dfs(root, float("-inf"))
        # return result



        """BFS

        Un nod este „bun” dacă, de-a lungul traseului de la rădăcină până la
        acel nod, niciun nod anterior nu are o valoare mai mare decât a
        acestuia. Folosind algoritmul BFS, putem parcurge nivel cu nivel,
        păstrând valoarea maximă întâlnită până în acel moment pentru fiecare
        traseu. De fiecare dată când vizităm un nod, comparăm valoarea acestuia
        cu valoarea maximă respectivă — dacă este mai mare sau egală, acest nod
        este bun.

        Fiecare nod fiu moștenește valoarea maximă actualizată a propriului
        său traseu.

        T = O(n), S = O(n)
        """
        queue = collections.deque([(root, float("-inf"))])
        result = 0

        while queue:
            node, max_above = queue.popleft()

            if node.val >= max_above:
                result += 1
                max_above = node.val

            if node.left:
                queue.append((node.left, max_above))

            if node.right:
                queue.append((node.right, max_above))

        return result
