class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += (("#" + str(len(string)) + "#") + string)
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        index = 0
        while index < len(s):
            if(index == 0):
                metadata_index = 1
                parsed_metadata = False
                while(not parsed_metadata and metadata_index < len(s)):
                    if(s[metadata_index] != "#"):
                        metadata_index+=1
                    else:
                        parsed_metadata = True
                string_len = int((s[1:metadata_index]))
                found = s[metadata_index + 1: metadata_index+(1+string_len)]
                res.append(found)
                s = s[metadata_index+(1+string_len): ]
        return res
