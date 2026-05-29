class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1: return 1
        
        
        longest = 1
        l = 0
        expected_sign = ''

        for r in range(1,len(arr)):
             
            if arr[r] == arr[r-1]:
                l = r
                expected_sign = ''
            else:
                sign = '<' if arr[r-1] < arr[r] else '>'
                if expected_sign == '':
                    expected_sign = '>' if arr[r-1] < arr[r] else '<'
                else:
                    if sign != expected_sign:
                        l = r - 1
                        expected_sign = '>' if arr[r-1] < arr[r] else '<'
                    else:
                        expected_sign = '>' if expected_sign == '<' else '<'
            longest = max(longest, r - l + 1)
        return longest