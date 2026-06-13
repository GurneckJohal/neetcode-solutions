# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                root = root.left
            elif not root.left:
                root = root.right
            else:
                min_leaf_val = self.findMinLeaf(root.right).val
                root.right = self.deleteNode(root.right, min_leaf_val)
                root.val = min_leaf_val
        return root
    
    def findMinLeaf(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr