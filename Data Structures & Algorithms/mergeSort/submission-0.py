# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1: return pairs

        first_half = self.mergeSort(pairs[:len(pairs)//2])
        second_half = self.mergeSort(pairs[len(pairs)//2:])

        sorted_array = []

        while first_half or second_half:
            v1 = first_half[0] if len(first_half) > 0 else None
            v2 = second_half[0] if len(second_half) > 0 else None
            
            if v1 and v2:
                if v1.key <= v2.key:
                    sorted_array.append(v1)
                    first_half = first_half[1:]
                else:
                    sorted_array.append(v2)
                    second_half = second_half[1:]
            elif v1 and not v2:
                sorted_array.append(v1)
                first_half = first_half[1:]
            else:
                sorted_array.append(v2)
                second_half = second_half[1:]

        return sorted_array