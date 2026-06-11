class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None
        
        curr = head.next
        head.next = None
        while curr != None:
            saved_next = curr.next
            curr.next = head
            head = curr
            curr = saved_next
        return head