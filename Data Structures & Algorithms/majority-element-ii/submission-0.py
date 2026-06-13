class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority = len(nums) // 3
        count = Counter(nums)

        res = []
        for num, freq in count.items():
            if freq > majority:
                res.append(num)
        
        return res