def initialise_board():
    board_size = 5
    board = ['O'] * (25)
    return board

minesweeper_board = initialise_board()
print(minesweeper_board)

def display_board(board):
    size = 5
    for i in range(size):
        for j in range(size):
            index = i * size + j
            if board[index] == 'X':
                print('O', end=' ')
            else:
                print(board[index], end=' ')
        print() #prints a new line after each row of 5

minesweeper_board = ['O', '1', 'X', '3', 'O',
                     '2', '3', 'O', '2', '2',
                     'O', 'X', '3', 'X', '1',
                     '2', 'X', 'O', '3', 'X',
                     'O', '3', 'O', '2', '1']

display_board(minesweeper_board)

def insert_mines(board, positions):
    size = 5
    for pos in positions:
        row, col = pos
        index = row * size + col
        board[index] = 'X'
    return board

# Example usage:
minesweeper_board = ['O'] * 25
mine_positions = [[2, 3], [1, 4]]
minesweeper_board = insert_mines(minesweeper_board, mine_positions)
print(minesweeper_board)

def count_adjacent_mines(board, row, column):
    size = 5
    mine_count = 0

    # Check above
    if row > 0 and board[(row - 1) * size + column] == 'X':
        mine_count += 1
    # Check below
    if row < size - 1 and board[(row + 1) * size + column] == 'X':
        mine_count += 1
    # Check left
    if column > 0 and board[row * size + (column - 1)] == 'X':
        mine_count += 1
    # Check right
    if column < size - 1 and board[row * size + (column + 1)] == 'X':
        mine_count += 1

    return mine_count

# Example usage:
minesweeper_board = ['O', '1', 'X', '3', 'O',
                     '2', '3', 'O', '2', '2',
                     'O', 'X', '3', 'X', '1',
                     '2', 'X', 'O', '3', 'X',
                     'O', '3', 'O', '2', '1']
row = 1
column = 1
adjacent_mines = count_adjacent_mines(minesweeper_board, row, column)
print("Number of adjacent mines:", adjacent_mines)


def play_turn(board, row, column):
    size = 5
    is_mine_selected = False

    # Calculate index of selected position
    index = row * size + column

    # Check if selected position is a mine
    if board[index] == 'X':
        board[index] = '#'
        is_mine_selected = True
    else:
        # Count adjacent mines
        mine_count = count_adjacent_mines(board, row, column)
        # Update board with mine count or space
        if mine_count == 0:
            board[index] = ' '
        else:
            board[index] = str(mine_count)

    return board, is_mine_selected

# Helper function to count adjacent mines
def count_adjacent_mines(board, row, column):
    size = 5
    mine_count = 0

    # Check above
    if row > 0 and board[(row - 1) * size + column] == 'X':
        mine_count += 1
    # Check below
    if row < size - 1 and board[(row + 1) * size + column] == 'X':
        mine_count += 1
    # Check left
    if column > 0 and board[row * size + (column - 1)] == 'X':
        mine_count += 1
    # Check right
    if column < size - 1 and board[row * size + (column + 1)] == 'X':
        mine_count += 1

    return mine_count

# Example usage:
minesweeper_board = ['O', '1', 'X', '3', 'O',
                     '2', '3', 'O', '2', '2',
                     'O', 'X', '3', 'X', '1',
                     '2', 'X', 'O', '3', 'X',
                     'O', '3', 'O', '2', '1']
row = 1
column = 1
updated_board, is_mine_selected = play_turn(minesweeper_board, row, column)
print("Updated board:", updated_board)
print("Mine selected?", is_mine_selected)


def check_win(board):
    for square in board:
        if square == 'O':
            return False
    return True

# Example usage:
minesweeper_board = [' ', '1', '#', '3', ' ',
                     '2', '3', ' ', '2', '2',
                     ' ', '#', '3', '#', '1',
                     '2', '#', ' ', '3', '#',
                     ' ', '3', ' ', '2', '1']

game_won = check_win(minesweeper_board)
print("Game won?", game_won)


def play_game(positions):
    # Initialize board
    minesweeper_board = initialise_board()
    # Insert mines
    insert_mines(minesweeper_board, positions)

    # Display initial state of the board (with mines hidden)
    print("Initial state of the board:")
    display_hidden_board(minesweeper_board)

    # Play the game until it's won or lost
    while True:
        # Get user input for row and column
        user_input = input("Enter row and column numbers (separated by space): ")
        row, column = map(int, user_input.split())

        # Play turn
        updated_board, is_mine_selected = play_turn(minesweeper_board, row, column)

        # Display updated board
        display_board(updated_board)

        # Check if the game is won
        if check_win(updated_board):
            print("Congratulations! You've won the game!")
            break
        # Check if a mine is selected
        elif is_mine_selected:
            print("Oh no! You've selected a mine. Game over!")
            break


# Function to display the board with hidden mines
def display_hidden_board(board):
    size = 5
    for i in range(size):
        for j in range(size):
            index = i * size + j
            if board[index] == 'X':
                print('O', end=' ')
            else:
                print(board[index], end=' ')
        print()


# Example usage:
mine_positions = [[1, 2], [3, 1], [4, 3]]
play_game(mine_positions)
