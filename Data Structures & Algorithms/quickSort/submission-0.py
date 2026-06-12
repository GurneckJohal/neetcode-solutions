# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1: return pairs
        insert_at = 0
        pivot = len(pairs) - 1
        for i in range(pivot):
            if pairs[i].key < pairs[pivot].key:
                temp = pairs[insert_at]
                pairs[insert_at] = pairs[i]
                pairs[i] = temp
                insert_at += 1

        temp = pairs[insert_at]
        pairs[insert_at] = pairs[pivot]
        pairs[pivot] = temp

        less = self.quickSort(pairs[:insert_at])
        greater = self.quickSort(pairs[insert_at+1:])
        
        return less + [pairs[insert_at]] +  greater