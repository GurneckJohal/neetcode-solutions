class ListNode:
    def __init__(self, val: int, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = None
    
    def get(self, index: int) -> int:
        curr = self.head.next
        
        curr_index = 0
        while curr and curr_index <= index:
            if curr_index == index:
                return curr.val
            curr_index += 1
            curr = curr.next
        
        return -1

    def insertHead(self, val: int) -> None:
        if not self.head.next:
            self.head.next = ListNode(val)
            self.tail = self.head.next
        else:     
            temp = self.head.next
            self.head.next = ListNode(val)
            self.head.next.next = temp


    def insertTail(self, val: int) -> None:
        if not self.tail:
            self.head.next = ListNode(val)
            self.tail = self.head.next
        else:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr = self.head
        curr_index = 0
        while curr_index < index and curr:
            curr_index += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next

        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next

        return res