class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2: return False

        prefixes = [0] * (len(nums) + 1)

        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            prefixes[i+1] = prefix
            for j in range(i):
                if (prefixes[i+1] - prefixes[j]) % k == 0 : return True
        
        return False