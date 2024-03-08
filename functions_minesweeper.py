def initialise_board():
    board = ['O'] * 25
    return board


def display_board(board):
    size = 5
    for i in range(size):
        for j in range(size):
            index = i * size + j
            if board[index] == 'X':
                print('O', end=' ')
            else:
                print(board[index], end=' ')
        print()     # Prints a new line after each row of 5


def insert_mines(board, positions):
    size = 5
    for pos in positions:
        row, col = pos
        index = row * size + col
        board[index] = 'X'
    return board


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


def play_turn(board, row, column):
    size = 5
    is_mine_selected = False

    # Calculate the index of selected position
    index = row * size + column

    # Check if selected position is a mine
    if board[index] == 'X':
        board[index] = '#'
        is_mine_selected = True
    else:
        # Counting our adjacent number of mines
        mine_count = count_adjacent_mines(board, row, column)
        # Updating the board with our mine count
        if mine_count == 0:
            board[index] = ' '
        else:
            board[index] = str(mine_count)

    return board, is_mine_selected


def check_win(board):
    for space in board:
        if space == 'O':
            return False
    return True


def play_game(positions):
    # Initialize the board
    minesweeper_board = initialise_board()
    # Insert the new mines
    insert_mines(minesweeper_board, positions)

    # Display the initial board (with our hidden mines 'X' as 'O')
    print("Starting board:")
    display_board(minesweeper_board)

    # Play the game until it's won or lost
    while True:
        # Obtain the row and column from user
        user_input = input("Enter row and column (separated by space): ")
        row, column = map(int, user_input.split())

        # Play a turn
        updated_board, is_mine_selected = play_turn(minesweeper_board, row, column)

        # Display updated board
        display_board(updated_board)

        # Check if the game has been won
        if check_win(updated_board):
            print("Congratulations! You've won the game!")
            break
        # Check if a mine is selected
        elif is_mine_selected:
            print("Oh no! You've selected a mine. Game over!")
            break


# Example usage:
# mine_positions = [[3, 2], [3, 1], [4, 3]]
# play_game(mine_positions)
