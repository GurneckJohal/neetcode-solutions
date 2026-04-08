class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        longest = 0
        l = 0
        most_freq = 0
        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1
            most_freq = max(hm.values())
            while (r - l + 1) - most_freq > k:
                hm[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest





# steps
# 1. increase count of current character
# 2. get most freq character count
# 3. calc leftover chars (window_size = most_freq_count)
# 4. check if leftover size is greater than k
# 5. if greater then increment l
# 6. else take window size and compare to longest
# 7. return longest