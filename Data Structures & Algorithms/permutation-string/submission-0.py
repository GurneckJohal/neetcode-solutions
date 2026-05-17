class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counts = [0] * 26
        for char in s1:
            s1_counts[ord(char) - ord('a')] += 1
        count_set = set()
        count_set.add(tuple(s1_counts))
        
        s2_counts = [0] * 26
        l = 0
        for r, char in enumerate(s2):
            s2_counts[ord(char) - ord('a')] += 1
            if (r - l + 1 > len(s1)):
                s2_counts[ord(s2[l]) - ord('a')] -= 1
                l+=1
            if tuple(s2_counts) in count_set:
                return True
        return False