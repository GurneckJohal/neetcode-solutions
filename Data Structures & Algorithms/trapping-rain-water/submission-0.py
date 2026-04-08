class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        while l <= r:
            if max_left <= max_right:
                max_left = max(max_left, height[l])
                trapped += max_left - height[l]
                l+=1
            else:
                max_right = max(max_right, height[r])
                trapped += max_right - height[r]
                r-=1
        return trapped
