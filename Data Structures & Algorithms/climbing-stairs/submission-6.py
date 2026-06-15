class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n

        return self.climb_stairs_memoized(n, {})

    
    def climb_stairs_memoized(self, n, memo):
        if n <= 3: return n

        if n in memo:
            return memo[n]
        
        memo[n] = self.climb_stairs_memoized(n-1, memo) + self.climb_stairs_memoized(n-2, memo)
        return memo[n]
