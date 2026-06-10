class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case "+":
                    operand_two = stack.pop()
                    operand_one = stack.pop()
                    res = operand_one + operand_two
                    stack.append(res)
                case "-":
                    operand_two = stack.pop()
                    operand_one = stack.pop()
                    res = operand_one - operand_two
                    stack.append(res)
                case "*":
                    operand_two = stack.pop()
                    operand_one = stack.pop()
                    res = operand_one * operand_two
                    stack.append(res)
                case "/":
                    operand_two = stack.pop()
                    operand_one = stack.pop()
                    res = math.trunc(operand_one / operand_two)
                    stack.append(res)
                case _:
                    stack.append(int(token))
            print(stack)
        return stack.pop()

# edge cases:
# - < 2 operands
# - dividing by 0
# - 
