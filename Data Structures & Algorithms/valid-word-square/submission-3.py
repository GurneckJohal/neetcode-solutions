class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            col_string = ""
            for j in range(len(words)):
                if i < len(words[j]):
                    col_string = col_string + words[j][i]
            
            if words[i] != col_string:
                return False
        
        return True