class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        results = { 0 : 1 }
        curr_sum = 0
        count = 0
        for num in nums:
            curr_sum += num
            if curr_sum - k in results:
                count += results[curr_sum - k]
            results[curr_sum] = 1 + results.get(curr_sum, 0)
        return count

