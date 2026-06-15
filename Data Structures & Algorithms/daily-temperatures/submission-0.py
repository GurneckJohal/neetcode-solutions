class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonic_stack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while monotonic_stack and temp > temperatures[monotonic_stack[-1]]:
                previous_day = monotonic_stack.pop()
                result[previous_day] = i - previous_day
            monotonic_stack.append(i)
        return result