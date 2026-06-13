class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        print(counts)
        res = 0
        has_char_with_odd_freq_char_count = False
        for freq in counts.values():
            if freq % 2 == 0:
                res += freq
            else:
                has_char_with_odd_freq_char_count = True
                if freq > 1:
                    res += (freq - 1)

        
        

        return res + 1 if has_char_with_odd_freq_char_count else res