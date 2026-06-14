class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums) + 1)
        suffix = [1] * (len(nums) + 1)
        pre = 1
        suf = 1
        for i in range(len(nums)):
            pre *= nums[i]
            suf *= nums[(len(nums) - 1) - i]
            prefix[i+1] = pre
            suffix[i+1] = suf
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[(len(nums) - 1) - i]
        return res 