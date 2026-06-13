class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        letter_counts = [0] * 26

        for i in range(len(s)):
            letter_counts[ord(s[i]) - ord('a')] += 1
            letter_counts[ord(t[i]) - ord('a')] -= 1

        for letter in letter_counts:
            if letter != 0:
                return False
        
        return True