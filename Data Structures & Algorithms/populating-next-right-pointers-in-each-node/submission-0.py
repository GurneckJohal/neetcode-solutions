"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None

        queue = deque()

        queue.append(root)

        while len(queue) > 0:
            next_pointers = len(queue) - 1
            for i in range(len(queue)):
                node = queue.popleft()
                if next_pointers > 0:
                    node.next = queue[0]
                else:
                    node.next = None
                if node.left:
                    queue.append(node.left)
                    queue.append(node.right)
                next_pointers -= 1
        
        return root