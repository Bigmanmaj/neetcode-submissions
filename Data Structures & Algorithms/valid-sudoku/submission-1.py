class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = 9
        columns = 9
        row_set = set()
        column_set = set()
        squares = [[set() for i in range(3)] for i in range(3)]
        for i in range(rows):
            for j in range(columns):
                if board[i][j] in row_set:
                    return False
                if board[j][i] in column_set:
                    return False
                if board[i][j] != '.':
                    row_set.add(board[i][j])
                    if board[i][j] in squares[i//3][j//3]:
                        return False
                    squares[i//3][j//3].add(board[i][j])
                if board[j][i] != '.':
                    column_set.add(board[j][i])
            row_set.clear()
            column_set.clear()
        return True