from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """DFS

        Pentru fiecare nod, să-l considerăm ca fiind punctul cel mai înalt al
        unei căi potențiale. O cale poate trece printr-un nod după cum urmează:
        subarborele stâng → nodul → subarborele drept

        Așadar, pentru fiecare nod avem nevoie de două lucruri:
        -Calea descendentă maximă pornind de la copilul său stâng
        -Calea descendentă maximă pornind de la copilul său drept
        
        O cale descendentă se termină la acel copil și se desfășoară exclusiv
        în jos (fără întoarcere în sus).
        Aceasta se calculează folosind get_max_downward_path().
        Apoi calculăm cea mai bună cale completă prin acest nod:
         node.val + leftDown + rightDown

        Încercăm acest lucru pentru fiecare nod folosind DFS și actualizăm
        răspunsul global.

        T = O(n^2), S = O(n)
        """
        # result = float("-inf")

        # def get_max_downward_path(node: Optional[TreeNode]) -> int:
        #     if not node:
        #         return 0
            
        #     left_path = get_max_downward_path(root.left)
        #     right_path = get_max_downward_path(root.right)

        #     path = root.val + max(left_path, right_path)
        #     return max(0, path)

        # def dfs(node: Optional[TreeNode]) -> None:
        #     nonlocal result
        #     if not node:
        #         return

        #     left_branch = get_max_downward_path(node.left)
        #     right_branch = get_max_downward_path(node.right)

        #     result = max(result, node.val + left_branch + right_branch)
        #     dfs(node.left)
        #     dfs(node.right)

        # dfs(root)
        # return result



        """Optimal DFS

        În problema sumei maxime a căilor, o cale poate începe și se poate
        termina oriunde în arbore, dar trebuie să se îndrepte în jos la fiecare
        pas (părinte → copil).

        Pentru fiecare nod, sunt importante două valori:
        -Calea descendentă maximă care pornește de la acest nod
          Această cale poate merge doar într-o singură direcție
          (stânga sau dreapta).
          Este utilizată de nodul părinte pentru a extinde calea în sus.
          Se calculează astfel:
           node.val + max(leftDown, rightDown)

        -Calea maximă prin acest nod
          Aceasta poate include atât căile descendente din stânga, cât și
          cele din dreapta:
           node.val + leftDown + rightDown
          Aceasta poate forma calea maximă globală.
        
        În timpul calculării DFS:
        Dacă suma unei căi descendente este negativă, o eliminăm (considerăm 0),
        deoarece adăugarea valorilor negative nu face decât să înrăutățească calea.
        La fiecare nod, actualizează maximul global folosind „calea prin acest nod”.
        Returnează cea mai bună cale descendentă către părinte.

        Acest lucru asigură că fiecare nod este vizitat o singură dată — timp
        optim O(n).

        T = O(n), S = O(n)
        """
        res = [root.val]

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_max = dfs(node.left)
            right_max = dfs(node.right)

            # for negative numbers
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            # compute max path WITH a split
            res[0] = max(res[0], node.val + left_max + right_max)

            return node.val + max(left_max, right_max)  # without split

        dfs(root)
        return res[0]
