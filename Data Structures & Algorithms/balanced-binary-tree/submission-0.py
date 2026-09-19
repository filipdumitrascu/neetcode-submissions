from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """Brute Force

        Un arbore este echilibrat dacă diferența dintre înălțimile
        subarborilor stâng și drept ai fiecărui nod este de cel mult 1.

        Abordarea straightforward respectă întocmai definiția:
        -Pentru fiecare nod, se calculează înălțimea subarborelui său stâng.
        -Se calculează înălțimea subarborelui său drept.
        -Se verifică dacă diferența dintre acestea este ≤ 1.
        -Această verificare se repetă recursiv pentru toți nodurile.

        T = O(n^2), S = O(n)
        """
        # def height(root: Optional[TreeNode]) -> int:
        #     if not root:
        #         return 0
        #     return 1 + max(height(root.left), height(root.right))

        # if not root:
        #     return True

        # left_height = height(root.left)
        # right_height = height(root.right)

        # if abs(left_height - right_height) > 1:
        #     return False

        # return self.isBalanced(root.left) and self.isBalanced(root.right)



        """Recursive DFS

        Soluția de tip „brute-force” duce la pierderea de timp prin recalcularea
        repetată a înălțimilor subarborilor. Remediem această problemă efectuând
        o singură căutare în adâncime (DFS) care returnează două informații
        simultan pentru fiecare nod:

        -Este subarborele echilibrat? (Adevărat/Fals)
        -Care este înălțimea acestuia?

        În acest fel, fiecare subarbore este procesat o singură dată.
        Dacă la orice nod diferența de înălțime este mai mare decât 1, îl marcăm ca
        fiind dezechilibrat și nu mai luăm în considerare nivelurile mai adânci.

        h - log n (balanced tree) or n (degenerate tree)
        T = O(n), S = O(h)
        """
        def dfs(root: Optional[TreeNode]) -> tuple[bool, int]:
            if not root:
                return (True, 0)

            left = dfs(root.left)
            right = dfs(root.right)

            balanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)

            return (balanced, 1 + max(left[1], right[1]))

        return dfs(root)[0]



        """Iterative DFS

        Soluția DFS recursivă calculează înălțimea și echilibrul într-o singură
        traversare post order.
        Această versiune iterativă face același lucru, dar simulează
        recursivitatea folosind o stivă.

        Ideea:
        -Trebuie să vizităm fiecare nod după copiii săi (postorder).
        -Odată ce ambii copii ai unui nod sunt procesați, cunoaștem deja înălțimile lor.
        -Apoi:
         -Verificăm dacă diferența de înălțime este ≤ 1
         -Salvăm înălțimea nodului (1 + max(stânga, dreapta))

        Dacă vreun nod este dezechilibrat, returnăm imediat false.

        T = O(n), S = O(n)
        """
        # stack = []
        # node = root
        # last = None
        # depths = {}

        # while stack or node:
        #     if node:
        #         stack.append(node)
        #         node = node.left
        #         continue

        #     node = stack[-1]
        #     if not node.right or last == node.right:
        #         stack.pop()
        #         left = depths.get(node.left, 0)
        #         right = depths.get(node.right, 0)

        #         if abs(left - right) > 1:
        #             return False

        #         depths[node] = 1 + max(left, right)
        #         last = node
        #         node = None
        #     else:
        #         node = node.right

        # return True
