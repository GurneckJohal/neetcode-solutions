class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        hs = set()
        for r in range(len(nums)):
            if r > k:
                hs.remove(nums[l])
                l+=1
            if not nums[r] in hs:
                hs.add(nums[r])
            else:
                return True
        return False