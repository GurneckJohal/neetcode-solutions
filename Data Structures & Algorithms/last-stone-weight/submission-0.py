class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]

        heapq.heapify_max(stones)
        
        while len(stones) >= 2:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)
            if stone1 != stone2:
                heapq.heappush_max(stones, abs(stone1 - stone2))
        
        if len(stones) > 0:
            return stones[0]
        return 0