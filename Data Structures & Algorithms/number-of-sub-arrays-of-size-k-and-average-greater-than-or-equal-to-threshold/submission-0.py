class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        avg = 0
        count = 0
        for r in range(len(arr)):
            if r - l + 1 > k:
                avg -= (arr[l]/k)
                l+=1
            
            avg += (arr[r]/k)
            if avg >= threshold and r - l + 1 == k:
                count+=1
            
            
        return count