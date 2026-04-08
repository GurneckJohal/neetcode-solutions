class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        l = 0
        longest = 0
        for r in range(len(s)):
            if s[r] in hm and hm[s[r]] >= l:
                l = hm[s[r]] + 1
            hm[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest