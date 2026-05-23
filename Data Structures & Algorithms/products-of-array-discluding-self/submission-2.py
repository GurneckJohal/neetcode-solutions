class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)
        for i in range(len(nums)):
            prev = 1
            if i > 0:
                prev = prefixes[i-1]
            prefixes[i] = prev * nums[i]
        for i in range(len(nums) - 1, 0, -1):
            prev = 1
            if i < len(nums) - 1:
                prev = suffixes[i+1]
            suffixes[i] = prev * nums[i]
        output = [1] * len(nums)
        for i in range(len(nums)):
            prefix = 1
            if i > 0:
                prefix = prefixes[i-1]
            suffix = 1
            if i < len(nums) - 1:
                suffix = suffixes[i+1]
            output[i] = prefix * suffix
        return output