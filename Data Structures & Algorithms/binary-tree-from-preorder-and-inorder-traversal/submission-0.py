from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        """Brute Force

        Primul element al tabloului de preordonare este întotdeauna
        rădăcina. Putem găsi poziția acestei rădăcini în tabloul de ordonare
        în ordine, care împarte tabloul de ordonare în ordine în subarbori stângi
        și drepți. Elementele situate înaintea rădăcinii în tabloul de ordonare în
        ordine aparțin subarborelui stâng, iar cele situate după aceasta aparțin
        subarborelui drept. Aceeași împărțire se aplică și în cazul preordonării
        Construim recursiv subarborii stângi și drepți folosind porțiunile
        corespunzătoare din ambele tablouri.

        T = O(n^2), S = O(n)
        """
        # if not preorder or not inorder:
        #     return None

        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])  # O(n) for each call

        # root.left = self.brute_force_dfs(preorder[1: mid + 1], inorder[: mid])
        # root.right = self.brute_force_dfs(preorder[mid + 1: ], inorder[mid + 1: ])

        # return root



        """Hash Map

        În abordarea DFS de bază, căutăm poziția rădăcinii în ordinea inorder
        folosind o căutare liniară, care durează O(n) timp pe nod. Prin
        precalcularea unei hărți hash care asociază valorile cu indicii lor în
        ordinea inorder, putem găsi poziția rădăcinii în timp O(1). De asemenea,
        evităm crearea de noi tablouri prin transmiterea indicilor care definesc
        limitele subtabloului curent.

        T = O(), S = O()
        """
        # inorder_indices = {value: index for index, value in enumerate(inorder)}
        # pre_idx = 0

        # def dfs(left: int, right: int) -> Optional[TreeNode]:
        #     nonlocal pre_idx

        #     if left > right:
        #         return None

        #     root_val = preorder[pre_idx]
        #     pre_idx += 1

        #     root = TreeNode(root_val)
        #     mid = inorder_indices[root_val]

        #     root.left = dfs(left, mid - 1)
        #     root.right = dfs(mid + 1, right)

        #     return root

        # return dfs(0, len(inorder) - 1)



        """Optimal DFS

        Putem evita complet utilizarea hărții hash folosind o abordare bazată
        pe limite. În loc să determinăm în mod explicit poziția rădăcinii,
        transmitem o valoare „limită” care ne indică momentul în care trebuie
        să încetăm construirea subarborelui stâng. Când întâlnim valoarea limită
        în trăsirea în ordine, știm că subarborele stâng este complet. Indicele
        de preordine ne indică ce nod trebuie să creăm în continuare, iar indicele
        de trăsire în ordine ne indică momentul în care am terminat un subarbor.

        T = O(n), S = O(n)
        """
        # preorder_index = 0
        # inorder_index = 0

        # def dfs(limit):
        #     nonlocal preorder_index, inorder_index

        #     if preorder_index >= len(preorder):
        #         return None

        #     if inorder[inorder_index] == limit:
        #         inorder_index += 1
        #         return None

        #     root = TreeNode(preorder[preorder_index])
        #     preorder_index += 1

        #     root.left = dfs(root.val)
        #     root.right = dfs(limit)
        #     return root

        # return dfs(float('inf'))



        """Morris Traversal

        Parcurgerea Morris ne permite să construim arborele în mod iterativ,
        fără a folosi o stivă de recursivitate. Ideea constă în utilizarea
        pointerilor din dreapta ai nodurilor pentru a stoca temporar referințele
        către părinți, simulând astfel stiva de apeluri. Construim nodurile pe
        măsură ce parcurgem arborele în ordine preordinală, conectându-le prin
        intermediul pointerilor din stânga și din dreapta. Când finalizăm un
        subarbore din stânga (detectat prin potrivirea secvenței în ordine
        inorder), restabilim structura inițială ștergând legăturile temporare
        și deplasându-ne în sus pe arbore.

        T = O(n), S = O(1)
        """
        head = TreeNode(None)
        curr = head
        i, j, n = 0, 0, len(preorder)
        while i < n and j < n:
            # Go right and then as far left as possible
            curr.right = TreeNode(preorder[i], right=curr.right)
            curr = curr.right
            i += 1
            while i < n and curr.val != inorder[j]:
                curr.left = TreeNode(preorder[i], right=curr)
                curr = curr.left
                i += 1
            j += 1
            while curr.right and j < n and curr.right.val == inorder[j]:
                prev = curr.right
                curr.right = None
                curr = prev
                j += 1

        return head.right
