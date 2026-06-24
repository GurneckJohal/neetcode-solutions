class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1: return 1
        i = len(s) - 1

        while s[i] == ' ':
            i -= 1
        
        right = i
        while i > 0 and s[i] != ' ':
            i -= 1
        
        left = i

        return right - left