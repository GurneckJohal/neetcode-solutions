class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = -1
        suffix = [0] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            suffix[i] = maxi
            maxi = max(maxi, arr[i])
        return suffix
           
        
            