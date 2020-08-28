board = [
    [3, 0, 0, 5, 9, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 2, 1, 0, 9],
    [0, 0, 0, 8, 0, 4, 3, 7, 0],
    [0, 3, 0, 0, 7, 0, 2, 0, 0],
    [0, 8, 0, 6, 2, 9, 0, 3, 0],
    [0, 0, 2, 0, 1, 0, 0, 9, 0],
    [0, 9, 7, 2, 0, 6, 0, 0, 0],
    [4, 0, 1, 9, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 5, 7, 0, 0, 8],
]


def sudoku_board():
    """Print the board with style"""
    # adds a separator every 3 rows
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - -")
        for j in range(len(board)):
            # add a separator every 3 columns except for the last one
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            # if last position, prints to next line
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + "", end="")
    return board


def find_empty():
    """Find the location of the first zero and return it's location"""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, column
    # Can you loop a function? Like if there's still a zero in board, run find_empty?


def try_num():
    """Using find_empty()'s return value, search the row, column, and box to see if a number is valid"""
    x = find_empty()
    print(x)
    # example, x = (0,1)
    for i in range(1, len(board) + 1):
        try:
            # if board[0] has 1, then loop again
            if board[x[0]].index(i):
                continue
            # if it gives an error because 1 is NOT in board[0], then go to except
        except:
            y = x[0]
            z = x[1]
            # checks if column is valid
            if is_valid_col(z) == False:
                continue
            # checks if box is valid
            if is_valid_box(z) == False:
                continue
            # number is currently valid, so set the zero to number
            board[y][z] = i
            return sudoku_board()
    # went through all numbers and none are valid, so call this function
    none_valid()


def none_valid():
    # all numbers invalid, so need to go back a step


def is_valid_col(num):
    """See if column has num being tried in function try_num()"""
    for i in range(1, len(board) + 1):
        # goes through each row and checks correct index to see if number is valid
        if board[i][num] == num:
            return False
    return True


def is_valid_box(num):
    """See if box has num being tried in function try_num()"""
    for i in range(1, len(board) + 1):
        # Goes through correct box to see if number is valid
        # How??
