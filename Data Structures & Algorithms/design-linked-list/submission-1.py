class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = None

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0

        while curr and i <= index:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        
        return -1

    def addAtHead(self, val: int) -> None:
        if self.head.next == None:
            self.head.next = ListNode(val)
            self.head.next.prev = self.head
            self.tail = self.head.next
        else:
            prev_head = self.head.next
            prev_head.prev = ListNode(val)
            prev_head.prev.prev = self.head
            prev_head.prev.next = prev_head
            self.head.next = prev_head.prev

    def addAtTail(self, val: int) -> None:
        if self.tail == None:
            self.head.next = ListNode(val)
            self.head.next.prev = self.head
            self.tail = self.head.next
        else:
            self.tail.next = ListNode(val)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head

        i = 0

        while curr and i < index:
            i += 1
            curr = curr.next
        
        if curr:
            saved_next = curr.next
            curr.next = ListNode(val)
            curr.next.prev = curr
            curr.next.next = saved_next

            if saved_next == None:
                self.tail = curr.next
            else:
                saved_next.prev = curr.next

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next

        i = 0
        while curr and i < index:
            curr = curr.next
            i += 1
        
        if curr:
            saved_next = curr.next
            saved_prev = curr.prev

            saved_prev.next = saved_next

            if saved_next == None:
                self.tail = saved_prev if saved_prev != self.head else None
            else:
                saved_next.prev = saved_prev

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)