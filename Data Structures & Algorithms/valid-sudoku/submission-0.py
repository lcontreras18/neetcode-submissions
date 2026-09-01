class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #validate rows
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] in seen:
                    return False
                elif board[i][j] != '.':
                    seen.add(board[i][j])
        
        #validate columns
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] in seen:
                    return False
                elif board[j][i] != '.':
                    seen.add(board[j][i])
        
        #validate boxes

        starts = [(0,0),(0,3),(0,6),
        (3,0),(3,3),(3,6),
        (6,0),(6,3),(6,6)]

        for i, j in starts:
            seen = set()
            for row in range(i, i + 3):
                for column in range(j, j + 3):
                    if board[row][column] in seen:
                        return False
                    elif board[row][column] != '.':
                        seen.add(board[row][column])

        return True
