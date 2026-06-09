class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for op in operations:
            match op:
                case "D":
                    scores.append(int(scores[-1])*2)
                case "+":
                    scores.append(int(scores[-1])+int(scores[-2]))
                case "C":
                    scores.pop()
                case _:
                    scores.append(op)
        return sum(int(score) for score in scores)