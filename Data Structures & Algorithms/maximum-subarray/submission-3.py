class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        largest = nums[0]
        for i in range(1, len(nums)):
            curr_sum = nums[i] + max(curr_sum, 0)
            largest = max(curr_sum, largest)
        return largest