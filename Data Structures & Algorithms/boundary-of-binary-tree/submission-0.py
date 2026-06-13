# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        return [root.val] + self.preorder(root.left)[:-1] + self.get_leafs(root.left) + self.get_leafs(root.right) + self.postorder(root.right)[1:]

    def get_leafs(self, root) -> List[int]:
        if not root: return []

        if not root.left and not root.right:
            return [root.val]
        else:
            return self.get_leafs(root.left) + self.get_leafs(root.right)

    def preorder(self, root) -> List[int]:
        if not root: return []

        res = [root.val]
        left_bound = self.preorder(root.left)

        if not left_bound:
            right_bound = self.preorder(root.right)

            if not right_bound:
                return res
            else:
                res.extend(right_bound)
                return res
        
        res.extend(left_bound)
        return res

    def postorder(self, root) -> List[int]:
        if not root: return []

        res = [root.val]

        right_bound = self.postorder(root.right)

        if not right_bound:
            left_bound = self.postorder(root.left)

            if not left_bound:
                return res
            else:
                left_bound.extend(res)
                return left_bound
        
        right_bound.extend(res)
        return right_bound

