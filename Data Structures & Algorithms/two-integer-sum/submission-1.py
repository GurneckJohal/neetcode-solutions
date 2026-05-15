class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, num in enumerate(nums):
            if hm.get(target - num) is None:
                hm[num] = i
            else:
                return [hm.get(target - num), i]
                
