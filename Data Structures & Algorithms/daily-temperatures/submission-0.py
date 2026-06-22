class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []

        for idx, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                topTemp, topIndex = stack.pop()
                res[topIndex] = idx - topIndex
                


            stack.append([temperature, idx])
        return res