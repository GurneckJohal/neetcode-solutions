# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        queue = deque()

        queue.append(root)

        res = []

        while len(queue) > 0:
            level = []
            queue_len = len(queue)

            for i in range(queue_len):
                current_node = queue.popleft()
                if not level:
                    level.append(current_node.val)
                
                if current_node.right:
                    queue.append(current_node.right)
                if current_node.left:
                    queue.append(current_node.left)
                
            res.extend(level)
        
        return res