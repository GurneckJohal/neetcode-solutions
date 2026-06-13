# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
      
        tree = self.bfs(root)
        return tree[k-1]

    def bfs(self, root) -> List[int]:
        if not root: return []

        return self.bfs(root.left) + [root.val] + self.bfs(root.right)
