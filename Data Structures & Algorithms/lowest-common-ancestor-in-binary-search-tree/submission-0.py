class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """Recursive DFS

        Lucrăm cu un arbore de căutare binar (BST), deci:
        -Toate valorile din subarborele stâng al unui nod sunt mai mici decât valoarea nodului.
        -Toate valorile din subarborele drept sunt mai mari decât valoarea nodului.

        Pentru două noduri p și q:
        -Dacă ambele valori sunt mai mici decât nodul curent -> ambele trebuie să se
        afle în subarborele stâng.
        -Dacă ambele valori sunt mai mari decât nodul curent -> ambele trebuie să se
        afle în subarborele din dreapta.
        -În caz contrar, nodul curent este punctul de divizare în care un nod se află
        în stânga, iar celălalt în dreapta (sau unul dintre ele este egal cu nodul curent).

        Acest punct de divizare este strămoșul comun cel mai mic (LCA).

        h - log n (balanced tree) or n (degenerate tree)
        T = O(h), S = O(h)
        """
        # if not root or not p or not q:
        #     return None

        # if max(p.val, q.val) < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)

        # if min(p.val, q.val) > root.val:
        #     return self.lowestCommonAncestor(root.right, p, q)

        # return root



        """Iterative DFS

        Aceasta este versiunea iterativă a găsirii strămoșului comun cel mai mic (LCA)
        într-un arbore de căutare binar (BST).
        Deoarece un BST este ordonat:
        -subarbore stâng < nod < subarbore drept

        Putem stabili unde se află ambele noduri doar prin compararea valorilor.

        -Dacă p și q sunt amândouă mai mari decât nodul curent -> ne deplasăm spre dreapta.
        -Dacă ambele sunt mai mici -> ne deplasăm spre stânga.
        -Dacă se separă (câte unul pe fiecare parte) sau unul este egal cu nodul curent ->
        nodul curent este LCA, deoarece este primul nod în care căile lor se separă.

        Astfel se evită recursivitatea și se parcurge pur și simplu arborele până când
        se găsește punctul de separare.

        h - log n (balanced tree) or n (degenerate tree)
        T = O(h), S = O(1)
        """
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                break

        return curr
