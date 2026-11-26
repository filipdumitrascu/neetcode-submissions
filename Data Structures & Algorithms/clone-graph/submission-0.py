"""Abordari

- o parcurgere DFS  
- o parcurgere BFS
"""


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
        old_to_new = {}  # mandatory for cycles

        def dfs(node: int) -> Optional['Node']:
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)
            old_to_new[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node) if node else None
