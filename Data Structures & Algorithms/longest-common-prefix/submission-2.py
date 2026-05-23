class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i, char in enumerate(strs[0]):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or not strs[j][i] == char:
                    return prefix
            prefix = prefix + char
        return prefix
            
