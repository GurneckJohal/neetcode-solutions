class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        count = 0
        l = 0
        my_dict = {}
        for r in range(len(s)):
            if s[r] in my_dict and my_dict[s[r]] >= l:
                l = my_dict[s[r]] + 1
            my_dict[s[r]] = r
            count = r - l + 1
            longest = max(longest, count)
        return longest