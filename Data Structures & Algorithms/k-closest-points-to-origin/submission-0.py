class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for point in points:
            point.insert(0, math.sqrt(point[0]**2 + point[1]**2))
        
        heap = []
        for point in points:
            heapq.heappush_max(heap, point)
            if len(heap) > k:
                heapq.heappop_max(heap)
        
        for point in heap:
            point.pop(0)
        
        return heap