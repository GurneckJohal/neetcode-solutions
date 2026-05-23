class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        hm = {}
        for r, char in enumerate(s):
            if not char in hm:
                longest = max(r - l + 1, longest)
            else:
                remove_index = hm[char]
                while l <= remove_index:
                    remove_char = s[l]
                    del hm[remove_char]
                    l += 1
            hm[char] = r
        return longest