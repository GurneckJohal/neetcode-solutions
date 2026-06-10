class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        
        while l < r and height[l] == 0:
            l += 1
        while l < r and height[r] == 0:
            r -= 1
        max_l, max_r = height[l], height[r]
        most = 0

        while l < r:
            if max_l <= max_r:
                most += max_l - height[l]
                l += 1
                max_l = max(max_l, height[l])
            else:
                most += max_r - height[r]
                r-=1
                max_r = max(max_r, height[r])

        return most