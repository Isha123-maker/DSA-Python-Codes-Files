# Define a class to represent the Sudoku board and all operations on it
class Board:
    def __init__(self, board):
        # store the initial puzzle (a 2D list) as an instance attribute
        self.board = board

    def __str__(self):
        # produce a string representation of the board for printing
        board_str = ''
        for row in self.board:
            # replace 0 with '*' and turn other numbers into strings
            row_str = [str(i) if i else '*' for i in row]
            # join the row into a space-separated string
            board_str += ' '.join(row_str)
            # add a newline at the end of each row
            board_str += '\n'
        return board_str

    def find_empty_cell(self):
        # find the first empty cell (represented by 0) in the board
        for row, contents in enumerate(self.board):   # row index + row contents
            try:
                # try to locate the first 0 in this row
                col = contents.index(0)
                return row, col   # return coordinates of empty cell
            except ValueError:
                # if there's no 0 in this row, move to the next
                pass
        return None   # no empty cells found → puzzle solved

    def valid_in_row(self, row, num):
        # check if num is not already present in the given row
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        # check if num is not already present in the given column
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        # check if num is not already present in the 3x3 square
        row_start = (row // 3) * 3   # top row of the 3x3 square
        col_start = (col // 3) * 3   # left column of the 3x3 square
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        # check if num can be placed at position (row, col)
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        # only valid if it's safe across row, col, and 3x3 square
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self):
        # recursive backtracking solver
        if (next_empty := self.find_empty_cell()) is None:
            # base case: no empty cells → solved!
            return True

        # try placing numbers 1 through 9 in the empty cell
        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                # place the guess on the board
                self.board[row][col] = guess

                # recursive call: try to solve the rest of the puzzle
                if self.solver():
                    return True

                # backtrack: undo the guess if it didn’t lead to a solution
                self.board[row][col] = 0
        # if no number fits, return False → triggers backtracking
        return False


# Helper function to use the Board class and solve the puzzle
def solve_sudoku(board):
    gameboard = Board(board)   # create a Board instance
    print(f'Puzzle to solve:\n{gameboard}')  # show unsolved puzzle
    if gameboard.solver():     # attempt to solve it
        print(f'Solved puzzle:\n{gameboard}')  # show solved puzzle
    else:
        print('The provided puzzle is unsolvable.')  # no solution exists
    return gameboard


# Example Sudoku puzzle with 0 representing empty cells
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

# Run the solver on the puzzle
solve_sudoku(puzzle)
