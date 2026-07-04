# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_path = (-1000 * 1001)

        def bfs(groot):
            nonlocal max_path
            if not groot: return 0

            left_max = bfs(groot.left)
            right_max = bfs(groot.right)


            node_max = max(left_max + groot.val, right_max + groot.val, left_max + right_max + groot.val, groot.val)

            max_path = max(max_path, node_max)

            return max(left_max + groot.val, right_max + groot.val, groot.val)

        bfs(root)
        
        return max_path