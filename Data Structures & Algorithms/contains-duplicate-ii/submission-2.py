class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = defaultdict(list)
        for i, num in enumerate(nums):
            if num in m:
                for index in m[num]:
                    if abs(index - i) <= k:
                        return True
                m[num].append(i)
            else:
                m[num].append(i)
        return False