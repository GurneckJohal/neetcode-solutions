class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            i = (abs(num)-1)
            nums[i] = abs(nums[i]) * -1
        
        res = []
        for i in range(1, len(nums) + 1):
            if nums[i-1] > 0:
                res.append(i)
        return res
