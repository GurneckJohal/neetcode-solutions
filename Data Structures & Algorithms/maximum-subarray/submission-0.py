class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        max_l, max_r = 0, 0
        l = 0

        for r in range((len(nums))):
            if(curr_sum < 0):
                curr_sum = 0
                l = r
            curr_sum+=nums[r]
            if(curr_sum >= max_sum):
                max_sum = curr_sum
                max_l, max_r = l, r
        
        return max_sum