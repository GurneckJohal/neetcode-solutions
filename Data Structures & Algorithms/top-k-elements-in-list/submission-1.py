class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        return list(map(lambda x: x[0], counts.most_common()))[:k]
