class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        slowest = 1
        fastest = max(piles)
        while slowest <= fastest:
            k = (fastest + slowest) // 2
            time_taken = lambda bananas: math.ceil(bananas/k)
            total_time = sum(map(time_taken, piles))
            if total_time <= h:
                fastest = k - 1
            elif total_time > h:
                slowest = k + 1

        return slowest