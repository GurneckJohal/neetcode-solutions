class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count = 0
        length = 100001
        l = 0
        for r in range(len(nums)):
            count += nums[r]
            while count >= target:
                length = min(r - l + 1, length)
                count -= nums[l]
                l+=1
        return 0 if length == 100001 else length