class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point
            heapq.heappush_max(heap, [x**2 + y**2, x, y])
            if len(heap) > k:
                heapq.heappop_max(heap)
        
        res = []

        for point in heap:
            dist, x, y = point
            res.append([x,y])
        
        return res