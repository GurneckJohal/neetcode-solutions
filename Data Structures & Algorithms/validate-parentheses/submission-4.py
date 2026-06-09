class Solution:
    def isValid(self, s: str) -> bool:
        valid_pairs = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }

        stack = []

        for bracket in s:
            if bracket in valid_pairs:
                stack.append(bracket)
            else:
                if len(stack) == 0 or bracket != valid_pairs[stack[-1]]:
                    return False
                stack.pop()
        
        return len(stack) == 0