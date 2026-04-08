class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = -1
        suffix = [0] * len(arr)
        for i in range(len(arr) - 1, 0, -1):
            maxi = max(maxi, arr[i])
            suffix[i] = maxi
        for i in range(len(arr)):
            if i + 1 == len(arr):
                arr[i] = -1
            else:
                arr[i] = suffix[i+1]
        return arr
           
        
            