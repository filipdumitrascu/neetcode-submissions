from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """Brute Force

        Pentru orice nod dintr-un arbore, cea mai lungă cale care
        trece prin el este:
        înălțimea subarborelui stâng + înălțimea subarborelui drept

        Așadar, pentru a afla diametrul arborelui, verificăm această
        valoare pentru fiecare nod. De asemenea, o comparăm cu cel mai
        bun diametru găsit în subarborele stâng și în cel drept.

        T = O(n^2), S = O(n)
        """
        # def max_height(root: Optional[TreeNode]) -> int:
        #     if not root:
        #         return 0

        #     return 1 + max(max_height(root.left), max_height(root.right))

        # if not root:
        #     return 0

        # left_height = max_height(root.left)
        # right_height = max_height(root.right)

        # diameter = left_height + right_height
        # sub_trees_diameters = max(self.diameterOfBinaryTree(root.left),
        #                 self.diameterOfBinaryTree(root.right))

        # return max(diameter, sub_trees_diameters)



        """Recursive DFS

        Diametrul unui arbore binar este cea mai lungă cale dintre două noduri
        oarecare. Această cale trebuie să treacă printr-un anumit nod, iar la
        acel nod lungimea căii este:
        (înălțimea subarborelui stâng) + (înălțimea subarborelui drept)

        Astfel, în timp ce efectuăm o căutare în adâncime (DFS) pentru a
        calcula înălțimile, putem urmări simultan valoarea maximă a 
        sumei stânga + dreapta observată până în acel moment.
        Astfel, obținem diametrul într-o singură trecere, fără a recalcula
        înălțimile.

        h - log n (balanced tree) or n (degenerate tree)
        T = O(n), S = O(h)
        """
        # diameter = 0

        # def dfs(curr: Optional[TreeNode]) -> None:
        #     if not curr:
        #         return 0

        #     left_height = dfs(curr.left)
        #     right_height = dfs(curr.right)

        #     nonlocal diameter
        #     diameter = max(diameter, left_height + right_height)

        #     return max(left_height, right_height) + 1

        # dfs(root)
        # return diameter



        """Iterative DFS

        DFS recursiv este cea mai simplă metodă de calculare a diametrului, dar
        utilizează stiva de apeluri. Putem simula același comportament în mod
        iterativ, folosind propria noastră stivă.

        Efectuăm o traversare în post order:
        -Vizităm subarborele din stânga
        -Vizităm subarborele din dreapta
        -Apoi procesăm nodul curent

        Pentru fiecare nod, stocăm într un map:
        -înălțimea sa
        -cel mai bun diametru al său

        După ce ambii copii sunt procesați, putem calcula:
        -înălțime = 1 + max(înălțimea stângă, înălțimea dreaptă)
        -diametru = max(înălțimea stângă + înălțimea dreaptă, diametrul stâng,
        diametrul drept)

        Aceasta înseamnă că fiecare nod este procesat exact o singură dată.

        h - log n (balanced tree) or n (degenerate tree)
        T = O(n), S = O(h)
        """
        stack = [root]
        node_height_diameter = {None: (0, 0)}  # node -> (best height, best diameter)

        while stack:
            node = stack[-1]

            if node.left and node.left not in node_height_diameter:
                stack.append(node.left)
            elif node.right and node.right not in node_height_diameter:
                stack.append(node.right)
            else:
                node = stack.pop()

                left_height, left_diameter = node_height_diameter[node.left]
                right_height, right_diameter = node_height_diameter[node.right]

                node_height_diameter[node] = (1 + max(left_height, right_height),
                           max(left_height + right_height, left_diameter, right_diameter))

        return node_height_diameter[root][1]
