class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        min_l = min_r = 0
        min_count = max(len(s), len(t))
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        for char in t:
            count_t[char] += 1
        for r, char in enumerate(s):
            count_s[char] += 1
            substring_contains_t = True
            for t_char in t:
                if count_s[t_char] < count_t[t_char]:
                    substring_contains_t = False
            while l <= r and substring_contains_t:
                if r - l + 1 <= min_count:
                    min_count = r - l + 1
                    min_l = l
                    min_r = r + 1
                count_s[s[l]] -= 1
                for t_char in t:
                    if count_s[t_char] < count_t[t_char]:
                        substring_contains_t = False
                l+=1
        return s[min_l:min_r]