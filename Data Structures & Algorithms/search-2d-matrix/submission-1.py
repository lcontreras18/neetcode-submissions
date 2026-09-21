class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        columns = len(matrix[0])
        rows = len(matrix)

        left = 0
        right = (columns * rows) - 1

        while left <= right:
            middle = (right + left) // 2
            row = middle // columns
            column = middle % columns

            val = matrix[row][column]

            if val == target:
                return True
            elif val > target:
                right = middle - 1
            else:
                left = middle + 1
        
        return False
