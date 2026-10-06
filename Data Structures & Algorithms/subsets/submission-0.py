class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        res = []
        solution = []

        def dfs(i):
            if i == n:
                res.append(solution.copy())
                return
            
            dfs(i + 1)

            solution.append(nums[i])
            dfs(i + 1)
            solution.pop()

        dfs(0)
        return res
        