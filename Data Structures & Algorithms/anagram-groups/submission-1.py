class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lists = {}
        for s in strs:
            arr = [0] * 26
            for char in s:
                i = ord(char) - ord('a') 
                arr[i]+=1
            key = tuple(arr)    
            value = lists.get(key, [])
            value.append(s)
            lists[key] = value
        return list(lists.values())
