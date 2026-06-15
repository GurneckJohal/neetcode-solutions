class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)

        heap = []
        for char, count in counts.items():
            heap.append([count, char])
        
        heapq.heapify_max(heap)

        prev = None

        res = ""

        while heap or prev:
            if not heap and prev:
                return ""
            
            count, char = heapq.heappop_max(heap)
            res = res + char
            count -= 1
            
            if prev:
                heapq.heappush_max(heap, prev)
                prev = None
            if count != 0:
                prev = [count, char]

        return res