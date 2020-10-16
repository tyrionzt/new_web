import re
class Solution:  # judge sudoku is avaiable
    def isValidSudoku(self, board):
        for i in range(9):
            locals()["sudoku" + str(i)] = []
        for i in range(9):
            row = []
            col = []
            for j in range(9):
                if board[i][j] and not re.match(r'^[1-9]{1}$', board[i][j]):
                    return False, (i, j)
                pos = (i // 3) * 3 + j // 3
                if board[i][j].isdigit():
                    if board[i][j] in row:
                        return False, (i, j)
                    row.append(board[i][j])

                if board[j][i].isdigit():
                    if board[j][i] in col:
                        return False, (i, j)
                    col.append(board[j][i])

                if board[i][j].isdigit():
                    if board[i][j] in locals()["sudoku" + str(pos)]:
                        return False, (i, j)
                    locals()["sudoku" + str(pos)].append(board[i][j])
        return True


aa = Solution().isValidSudoku([
  ["5","3","","","7","","","",""],
  ["6","","","1","9","5","","",""],
  ["","9","8","","","","","6",""],
  ["8","","","","6","","","","3"],
  ["4","","","8","","3","","","1"],
  ["7","","","","2","","","","6"],
  ["","6","","","","","2","8",""],
  ["","","","4","1","9","","","5"],
  ["","","","","8","","","7","9"]
])
print aa