"""Abordari

- o parcurgere DFS  
- o parcurgere BFS
"""


import collections


# # Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """DFS

        T = O(v + e), S = O(v)
        """
        # old_to_new = {}  # mandatory for cycles

        # def dfs(node: int) -> Optional['Node']:
        #     if node in old_to_new:
        #         return old_to_new[node]

        #     copy = Node(node.val)
        #     old_to_new[node] = copy
        #     for nei in node.neighbors:
        #         copy.neighbors.append(dfs(nei))
        #     return copy
        
        # return dfs(node) if node else None


        """BFS

        T = O(v + e), S = O(v)
        """
        if not node:
            return None

        old_to_new = {}
        old_to_new[node] = Node(node.val)
        q = collections.deque([node])

        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in old_to_new:
                    old_to_new[nei] = Node(nei.val)
                    q.append(nei)
                old_to_new[cur].neighbors.append(old_to_new[nei])
        return old_to_new[node]
