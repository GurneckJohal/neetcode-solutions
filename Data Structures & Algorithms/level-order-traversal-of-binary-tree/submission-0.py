# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()

        if root:
            queue.append(root)

        res = []
        while len(queue) > 0:
            level = []
            queue_len = len(queue)
            for i in range(queue_len):
                current_node = queue.popleft()
                level.append(current_node.val)
                
                if current_node.left:
                    queue.append(current_node.left)
                
                if current_node.right:
                    queue.append(current_node.right)
                
            res.append(level)

        return res