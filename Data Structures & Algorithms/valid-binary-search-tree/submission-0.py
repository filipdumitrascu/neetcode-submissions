# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> tuple[bool, int, int]:
            if not node:
                return True, float("inf"), float("-inf")

            is_left_bst, left_min, left_max = dfs(node.left)
            is_right_bst, right_min, right_max = dfs(node.right)

            if (
                is_left_bst and is_right_bst and left_max < node.val
                and node.val < right_min
            ):
                return True, min(left_min, node.val), max(right_max, node.val)

            return False, min(left_min, node.val), max(right_max, node.val)

        return dfs(root)[0]
