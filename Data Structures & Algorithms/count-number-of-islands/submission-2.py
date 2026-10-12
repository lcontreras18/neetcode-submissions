class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        def dfs(row, column):
            if row < 0 or column < 0 or row >= rows or column >= columns or grid[row][column] != '1':
                return
            else:
                grid[row][column] = '0'

                dfs(row + 1, column)
                dfs(row - 1, column)
                dfs(row, column + 1)
                dfs(row, column - 1)



        num_islands = 0
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == '1':
                    num_islands += 1
                    dfs(row,column)
        
        return num_islands
