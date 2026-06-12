# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_head = l1
        tail = l1
        overflow = 0
        while l1 and l2:
            tail = l1
            old_l1_val = l1.val
            l1.val = ((l1.val + l2.val) % 10) + overflow
            overflow = 1 if (old_l1_val + l2.val) >= 10 else 0
            l1 = l1.next
            l2 = l2.next
        if not l1 and not l2:
            if overflow:
                tail.next = ListNode(1)
        else:
            if not l1 and l2:
                tail.next = l2
                while overflow and l2:
                    tail = l2
                    old_l2_val = l2.val
                    l2.val = (l2.val + overflow) % 10
                    overflow = 1 if (overflow + old_l2_val) >= 10 else 0
                    l2 = l2.next
                if overflow:
                    tail.next = ListNode(1)
            else:
                while overflow and l1:
                    tail = l1
                    old_l1_val = l1.val
                    l1.val = (l1.val + overflow) % 10
                    overflow = 1 if (overflow + old_l1_val) >= 10 else 0
                    l1 = l1.next
                if overflow:
                    tail.next = ListNode(1)
        
        return l1_head
        