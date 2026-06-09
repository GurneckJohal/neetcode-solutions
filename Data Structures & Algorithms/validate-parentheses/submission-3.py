class Solution:
    def isValid(self, s: str) -> bool:
        opening_brackets = {"(", "[", "{"}
        
        valid_pairs = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }

        stack = []

        for bracket in s:
            stack.append(bracket)
            if bracket not in opening_brackets:
                stack.pop()
                if len(stack) == 0 or bracket != valid_pairs[stack[-1]]:
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0