from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # left_check = staticmethod(lambda val, limit: val < limit)
    # right_check = staticmethod(lambda val, limit: val > limit)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """Brute Force

        Pentru a verifica dacă un arbore este un arbore de căutare binar (BST)
        valid, fiecare nod trebuie să îndeplinească următoarele condiții:
        -Toate valorile din subarborele său stâng sunt strict mai mici decât
        valoarea nodului.
        -Toate valorile din subarborele său drept sunt strict mai mari decât
        valoarea nodului.

        În această abordare de tip „forță brută”, pentru fiecare nod:
        -Verificăm toate nodurile din subarborele său stâng pentru a ne asigura
        că sunt < node.val.
        -Verificăm toate nodurile din subarborele său drept pentru a ne asigura
        că sunt > node.val.
        -Apoi repetăm recursiv același proces pentru fiecare copil,
        considerându-l o nouă rădăcină.

        Această abordare verifică din nou multe noduri de mai multe ori, așa că
        este corectă, dar nu eficientă.

        T = O(n^2), S = O(n)
        """
        # def isValid(root: Optional[TreeNode], limit: int, check) -> bool:
        #     if not root:
        #         return True

        #     if not check(root.val, limit):
        #         return False

        #     return (
        #         isValid(root.left, limit, check)
        #         and isValid(root.right, limit, check)
        #     )

        # if not root:
        #     return True

        # if (
        #     not isValid(root.left, root.val, self.left_check)
        #     or not isValid(root.right, root.val, self.right_check)
        # ):
        #     return False

        # return (
        #     self.isValidBST(root.left)
        #     and self.isValidBST(root.right)
        # )



        """Recursive DFS (Bottom Up)

        Pentru fiecare nod, verificăm dacă subarborele său stâng și subarborele
        său drept sunt BST-uri valide și, în același timp, păstrăm cea mai mică
        și cea mai mare valoare din fiecare subarbore.

        Ideea este să folosim informația întoarsă de copii pentru a verifica
        nodul curent:
        -Subarborele stâng trebuie să fie un BST valid.
        -Subarborele drept trebuie să fie un BST valid.
        -Cea mai mare valoare din subarborele stâng trebuie să fie < node.val.
        -Cea mai mică valoare din subarborele drept trebuie să fie > node.val.

        Pentru un nod fără copii:
        -Subarborele stâng este considerat valid și are:
            min = +∞
            max = -∞
        -Subarborele drept este considerat valid și are aceleași valori.

        După ce verificăm nodul curent, întoarcem:
        -True, dacă ambii subarbori sunt BST-uri și valorile lor respectă
        regula BST.
        -Cea mai mică valoare din întregul subarbore.
        -Cea mai mare valoare din întregul subarbore.

        În acest fel, fiecare nod este procesat o singură dată, iar informația
        despre min/max este transmisă înapoi prin recursivitate.

        T = O(n), S = O(n)
        """
        # def dfs(node: Optional[TreeNode]) -> tuple[bool, int, int]:
        #     if not node:
        #         return True, float("inf"), float("-inf")

        #     is_left_bst, left_min, left_max = dfs(node.left)
        #     is_right_bst, right_min, right_max = dfs(node.right)

        #     if (
        #         is_left_bst and is_right_bst and left_max < node.val
        #         and node.val < right_min
        #     ):
        #         return True, min(left_min, node.val), max(right_max, node.val)

        #     return False, min(left_min, node.val), max(right_max, node.val)

        # return dfs(root)[0]



        """Recursive DFS 2 (Top Down)

        Un arbore de căutare binar nu se rezumă doar la faptul că fiecare nod
        este mai mic sau mai mare decât părintele său — fiecare nod trebuie să
        se încadreze într-un interval de valori valid, determinat de toți
        strămoșii săi.

        Pentru rădăcină, intervalul permis este (-∞, +∞).
        Când te deplasezi spre stânga, valoarea nodului trebuie să fie mai mică
        decât cea a părintelui, astfel încât limita superioară devine mai mică.
        Când te deplasezi spre dreapta, valoarea nodului trebuie să fie mai mare
        decât cea a părintelui, astfel încât limita inferioară devine mai mare.
        Pe măsură ce coborâm în arbore, continuăm să restrângem aceste limite.
        Dacă vreun nod încalcă intervalul permis → arborele nu este un BST.

        Aceasta verifică eficient toate regulile BST într-o singură trecere DFS.

        T = O(n), S = O(n)
        """
        # def dfs(node: Optional[TreeNode], left_limit: int, right_limit: int) -> bool:
        #     if not node:
        #         return True

        #     if not (left_limit < node.val < right_limit):
        #         return False

        #     return dfs(node.left, left_limit, node.val) and dfs(node.right, node.val, right_limit)

        # return dfs(root, float("-inf"), float("inf"))



        """BFS
        
        Un arbore este un BST valid numai dacă fiecare nod se încadrează într-un
        interval valid definit de strămoșii săi. În loc să folosim recursivitatea,
        putem folosi o coadă (BFS) pentru a verifica acest lucru nivel cu nivel.

        Începem cu rădăcina, al cărei interval valid este (-∞, +∞).
        -Când trecem la copilul din stânga, valoarea maximă permisă a acestuia
        devine valoarea nodului curent.
        -Când ne deplasăm către copilul din dreapta, valoarea minimă permisă a
        acestuia devine valoarea nodului curent.
        -Dacă vreun nod încalcă intervalul permis, arborele nu este un BST.

        În acest fel, verificăm fiecare nod exact o singură dată folosind BFS.

        T = O(n), S = O(n)
        """
        if not root:
            return True

        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, left, right = q.popleft()
            if not (left < node.val < right):
                return False
            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right, node.val, right))

        return True
