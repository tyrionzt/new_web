import re
from Tkinter import *
from collections import defaultdict
from random import choice
import tkMessageBox as mb


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


class Solution1:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: return a valid Sudoku board
        """

        def could_place(d, row, col):
            """
            Check if one could place a number d in (row, col) cell
            """
            return not (d in rows[row] or d in columns[col] or d in boxes[box_index(row, col)])

        def place_number(d, row, col):
            """
            Place a number d in (row, col) cell
            """
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)

        def remove_number(d, row, col):
            """
            Remove a number which didn't lead
            to a solution
            """
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = ''

        def place_next_numbers(row, col):
            """
            Call backtrack function in recursion
            to continue to place numbers
            till the moment we have a solution
            """
            # if we're in the last cell
            # that means we have the solution
            if col == N - 1 and row == N - 1:
                sudoku_solved[0] = True
            # if not yet
            else:
                # if we're in the end of the row
                # go to the next row
                if col == N - 1:
                    backtrack(row + 1, 0)
                # go to the next column
                else:
                    backtrack(row, col + 1)

        def backtrack(row=0, col=0):
            """
            Backtracking
            """
            # if the cell is empty
            if not board[row][col]:
                # iterate over all numbers from 1 to 9
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        # if sudoku is solved, there is no need to backtrack
                        # since the single unique solution is promised
                        if not sudoku_solved[0]:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)

        # box size
        n = 3
        # row size
        N = n * n
        # lambda function to compute box index
        box_index = lambda row, col: (row // n) * n + col // n

        # init rows, columns and boxes
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j]:
                    d = int(board[i][j])
                    place_number(d, i, j)


        sudoku_solved = {}
        sudoku_solved[0] = False
        backtrack()
        return board


def generate():
    board = [["", "", "", "", "", "", "", "", ""] for i in range(9)]
    for i in range(30):
        board[choice(range(9))][choice(range(9))] = choice(range(1, 10))
    return board


main = Tk()
main.title("sudoku")
board = [["", "", "", "", "", "", "", "", ""] for i in range(9)]
main.geometry("430x280")


def get_result():
    for i in range(9):
        for j in range(9):
            board[i][j] = globals()["text_input" + str(i) + str(j)].get()
    print board
    res = Solution().isValidSudoku(board)
    print res
    if not isinstance(res, tuple):
        Label(main, text="congratulations!!! you win", bg="green").pack(side=CENTER)
        print 1111
    else:
        x, y = res[1][0], res[1][1]
        # error = StringVar(value=board[x][y])
        # globals()["text_input" + str(x) + str(y)] = Entry(main, textvariable=error, width=3, bg="red")
        # globals()["text_input" + str(x) + str(y)].grid(row=x, column=y)
        mb.showerror(title="error!!!", message="%s row, %s column" % (x+1, y+1), bg="red")
        # error = Label(main, text="error!!! %s row, %s column" % (x+1, y+1), bg="red")
        # error.pack(side=BOTTOM)


def clean():
    for i in range(9):
        for j in range(9):
            locals()["vars" + str(i) + str(j)] = StringVar()
            globals()["text_input" + str(i) + str(j)] = Entry(main, textvariable=locals()["vars" + str(i) + str(j)],
                                                              width=3)
            globals()["text_input" + str(i) + str(j)].grid(row=i, column=j)


def new():
    for i in range(9):
        for j in range(9):
            new_board = generate()
            locals()["vars" + str(i) + str(j)] = StringVar(value=new_board[i][j])
            globals()["text_input" + str(i) + str(j)] = Entry(main, textvariable=locals()["vars" + str(i) + str(j)],
                                                              width=3)
            globals()["text_input" + str(i) + str(j)].grid(row=i, column=j)


def answer():
    pass


B = Button(main, text="confirm", width=6, command=get_result).grid(row=1, column=13)
B1 = Button(main, text="clean", width=6, command=clean).grid(row=3, column=13)
B2 = Button(main, text="new", width=6, command=new).grid(row=5, column=13)
B3 = Button(main, text="answer", width=6, command=answer).grid(row=7, column=13)
main.mainloop()
