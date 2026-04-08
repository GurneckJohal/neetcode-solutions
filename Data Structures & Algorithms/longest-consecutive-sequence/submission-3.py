class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in nums:
            if not num - 1 in num_set:
                count = 0
                while num+count in num_set:
                    count+=1
                longest = max(longest, count)
        return longest
                