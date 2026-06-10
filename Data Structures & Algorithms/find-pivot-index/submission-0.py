class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixes = [0] * (len(nums)+2)
        postfixes = [0] * (len(nums)+2)

        count = 0
        for i, num in enumerate(nums):
            count += num
            prefixes[i+1] = count

        count = 0
        for i in range(1, len(nums)+1):
            count += nums[len(nums) - i]
            postfixes[i] = count
        
        for i in range(0, len(nums)+1):
            if prefixes[i] == postfixes[(len(nums) - i)-1]:
                return i
        
        return -1
