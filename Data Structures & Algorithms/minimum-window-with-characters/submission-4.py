class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        min_l = min_r = 0
        min_count = max(len(s), len(t))
        count_s = defaultdict(int)
        count_t = defaultdict(int)

        for char in t:
            count_t[char] += 1
        need = len(count_t)
        have = 0
        
        for r, char in enumerate(s):
            count_s[char] += 1
            if char in count_t and count_s[char] == count_t[char]:
                have += 1
            while l <= r and have == need:
                if r - l + 1 <= min_count:
                    min_count = r - l + 1
                    min_l = l
                    min_r = r + 1
                count_s[s[l]] -= 1
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have-=1
                l+=1
        return s[min_l:min_r]