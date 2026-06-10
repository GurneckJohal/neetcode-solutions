class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        curr_most = most = 0
        
        while l < r:
            curr_most = min(heights[l], heights[r]) * (r - l)
            most = max(most, curr_most)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return most