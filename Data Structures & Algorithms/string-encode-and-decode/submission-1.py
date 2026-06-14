class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        if s == "" : return []
        i = 0
        res = []
        while i < len(s):
            str_len = ""
            while s[i] != "#":
                str_len = str_len + s[i]
                i += 1
            i += 1
            j = 0
            string = ""
            while j < int(str_len):
                string = string + s[i]
                i += 1
                j += 1
            res.append(string)
        return res
        

            
        
            
                