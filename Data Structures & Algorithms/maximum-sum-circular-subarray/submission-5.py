class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        min_sum = nums[0]
        max_sum = nums[0]
        curr_min_sum = nums[0]
        curr_max_sum = nums[0]
        total_sum = nums[0]
        for r in range(1,len(nums)):
            curr_min_sum = min(curr_min_sum + nums[r], nums[r])
            min_sum = min(min_sum, curr_min_sum)

            curr_max_sum = max(curr_max_sum + nums[r], nums[r])
            max_sum = max(max_sum, curr_max_sum)

            total_sum += nums[r]

        circular_sum = total_sum - min_sum

        if(circular_sum == 0):
            return max_sum
        
        return max(max_sum, circular_sum)

            