from typing import Optional
import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def _dfs_encode(self, root: Optional[TreeNode]) -> str:
        """
        Vrem să transformăm un arbore într-un șir de caractere (serializare) și
        apoi să reconstruim același arbore pornind de la acel șir (deserializare).

        Folosim DFS în ordine preordinală (rădăcină → stânga → dreapta),
        deoarece aceasta înregistrează în mod natural un nod înaintea copiilor săi.

        Când un nod există → înregistrăm valoarea acestuia.
        Când lipsește un copil → înregistrăm „N”, astfel încât să știm unde se
        află pointerii nul.

        Exemplu:
        1,2,N,N,3,N,N reprezintă în mod unic un arbore.

        În timpul deserializării, citim lista în ordine:
        „N” → returnăm None
        În caz contrar → creăm nodul, apoi construim partea stângă,
        apoi cea dreaptă.

        Acest lucru funcționează deoarece algoritmul DFS în preordine
        vizitează întotdeauna nodurile în ordinea exactă a structurii.

        T = O(n), S = O(n)
        """
        result = []

        def dfs(node):  # preorder
            if not node:
                result.append("N")
                return

            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(result)

    def _dfs_decode(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        index = 0

        def dfs():
            nonlocal index

            if vals[index] == "N":
                index += 1
                return None

            node = TreeNode(int(vals[index]))
            index += 1

            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

    def _bfs_encode(self, root: Optional[TreeNode]) -> str:
        """

        În loc să folosim DFS, tratăm arborele ca pe o coadă
        (parcurgere pe niveluri). BFS vizitează nodurile nivel cu nivel, așa că
        înregistrăm pur și simplu valorile în această ordine:
        -Dacă un nod există → înregistrăm valoarea acestuia și adăugăm copiii
        săi (chiar dacă aceștia sunt None).
        -Dacă un nod lipsește → înregistrăm „N” pentru a marca locurile goale.

        Astfel ne asigurăm că structura este păstrată, deoarece BFS procesează
        nodurile exact așa cum apar în structura arborelui.

        În timpul deserializării, folosim din nou BFS:
        -Prima valoare este rădăcina.
        -Apoi, pentru fiecare nod din coadă, îi atribuim copiii din stânga și
        din dreapta folosind valorile următoare din listă.

        Astfel, reconstrucția arborelui rămâne aliniată cu ordinea serializată.

        T = O(n), S = O(n)
        """
        if not root:
            return "N"

        result = []
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if not node:
                result.append("N")
            else:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        return ",".join(result)

    def _bfs_decode(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")

        if vals[0] == "N":
            return None

        root = TreeNode(int(vals[0]))
        queue = collections.deque([root])
        index = 1

        while queue:
            node = queue.popleft()

            if vals[index] != "N":
                node.left = TreeNode(int(vals[index]))
                queue.append(node.left)

            index += 1

            if vals[index] != "N":
                node.right = TreeNode(int(vals[index]))
                queue.append(node.right)

            index += 1

        return root

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # return self._dfs_encode(root)
        return self._bfs_encode(root)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # return self._dfs_decode(data)
        return self._bfs_decode(data)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
