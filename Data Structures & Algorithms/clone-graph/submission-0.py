from typing import Optional
import collections


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """DFS

        Graful poate conține cicluri, așa că nu putem pur și simplu să copiem
        nodurile în mod recursiv fără să ținem minte ce am copiat deja.
        Pentru a rezolva această problemă, folosim o hartă (vechi → nou):
        - Când întâlnim un nod pentru prima dată, îi creăm o copie.
        - Dacă întâlnim din nou același nod, reutilizăm copia deja creată.
        - Astfel se evită buclele infinite și se asigură că fiecare nod este
        clonat exact o singură dată.

        Căutarea în profunzime (DFS) ne ajută să explorăm și să clonăm toate
        nodurile conectate.

        v - vertices, e - edges
        T = O(v + e), S = O(v)
        """
        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)
            old_to_new[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None



        """BFS

        Graful poate conține cicluri, așa că, în timpul clonării, trebuie să
        evităm crearea de noduri duplicate sau intrarea într-o buclă infinită.
        Folosind căutarea în lățime (BFS), explorăm graficul nivel cu nivel și
        păstrăm o hartă care conține legăturile dintre nodurile originale și
        clonele lor.
        - Când un nod este întâlnit pentru prima dată, creăm clona acestuia și
        o stocăm în hartă.
        - Pentru fiecare vecin, ne asigurăm că clona acestuia există, apoi
        conectăm nodurile clonate.
        - Harta garantează că fiecare nod este clonat o singură dată.

        v - vertices, e - edges
        T = O(v + e), S = O(v)
        """
        # if not node:
        #     return None

        # old_to_new = {}
        # old_to_new[node] = Node(node.val)
        # q = collections.deque([node])

        # while q:
        #     cur = q.popleft()
        #     for nei in cur.neighbors:
        #         if nei not in old_to_new:
        #             old_to_new[nei] = Node(nei.val)
        #             q.append(nei)
        #         old_to_new[cur].neighbors.append(old_to_new[nei])

        # return old_to_new[node]
