class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        longer = len(s) if len(s) > len(t) else len(t)

        for i in range(longer):
            if(i < len(s)):
                count_s[s[i]] = count_s.get(s[i], 0) + 1
            if(i < len(t)):
                count_t[t[i]] = count_t.get(t[i], 0) + 1

        return count_s == count_t
