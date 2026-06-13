# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        left_height = self.dfs(root.left)
        right_height = self.dfs(root.right)

        if left_height != -1 and right_height != -1:
            return abs(left_height - right_height) <= 1
        return False

    
    def dfs(self, root):
        if not root: return 0

        left_height = self.dfs(root.left)
        right_height = self.dfs(root.right)

        if left_height != -1 and right_height != -1:
            height = max(left_height, right_height)
            if abs(left_height - right_height) <= 1:
                return height + 1
        return -1


