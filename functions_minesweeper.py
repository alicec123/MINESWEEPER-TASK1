def initialise_board():
    """
    This function initialises the minesweeper grid.

    Arguments
    ---------
    This function takes no inputs.

    Returns
    ---------
    board (list) : 1D list representing the minesweeper board. It contains 25 items, with each item being
    the string "O", representing a square that has not yet been selected in the game.

    Notes
    ---------
    Pre conditions : None
    Post condition : The returned board is a list of 25 ‘O’s representing unselected values
    """
    # A single 'O' string multiplied by 25 to generate the board in 1D form.
    board = ['O'] * 25
    return board


def display_board(board):
    """
    This function displays the list to screen as a 5 x 5 board. "O", spaces and number of adjacent mines will be
    displayed, however, mines "X" should still be displayed as "O".

    Arguments
    ---------
    board : This function has one input, the list that represents the board, as generated in the function
    initialise_board.

    Returns
    ---------
    This function has no outputs.

    Notes
    ---------
    Pre conditions : None
    Post condition : The output should display the list as a 5 x 5 board form.
    """
    # Nested for loop will index at each element and check for a mine. At the end of each row of 5, it prints
    # a new line to create the 2D shape.
    board_size = 5
    for i in range(board_size):
        for j in range(board_size):
            index = i * board_size + j
            if board[index] == 'X':
                print('O', end=' ')
            else:
                print(board[index], end=' ')
        print()


def insert_mines(board, positions):
    """
    This function inserts mines at the specified positions. The mines are denoted by the character 'X'.

    Arguments
    ---------
    board : A list representing the board
    positions : A list of lists representing each mine location. The first index represents the row (0-4) and
    the second index represents the column (0-4).

    Returns
    ---------
    Output 1 : A list representing the updated board.

    Notes
    ---------
    Pre conditions : None
    Post condition : The output should display the list as a 5 x 5 board form.
    """
    # Using a for loop, insert 'X' as a mine at the index.
    size = 5
    for pos in positions:
        row, col = pos
        index = row * size + col
        board[index] = 'X'
    return board


def count_adjacent_mines(board, row, column):
    """
    This function counts the sum of the mines, "X", adjacent and/or diagonal to the selected row and column position.

    Arguments
    ---------
    board : A list representing the board
    row : An int representing the row (0-4) of the square being checked for adjacent mines.
    column : An int representing the column (0-4) of the square being checked for adjacent mines.

    Returns
    ---------
    Output 1 : An int representing the number of adjacent/diagonal mines.

    Notes
    ---------
    Pre conditions : None
    Post condition : None
    """
    # Declare the size of board and initial count for the mines
    board_size = 5
    count_mine = 0

    # Check the above three elements to see if a mine exists. If a mine is found, add 1 to the count
    if row > 0:
        # Above the selected element
        if board[(row - 1) * board_size + column] == 'X':
            count_mine += 1
        # Above (diagonal) left
        if (column > 0) and board[(row - 1) * board_size + (column - 1)] == 'X':
            count_mine += 1
        # Above (diagonal) right
        if column < (board_size - 1) and board[(row - 1) * board_size + (column + 1)] == 'X':
            count_mine += 1

        # Check the bottom three elements to see if a mine exists
    if row < board_size - 1:
        # Below the selected element
        if board[(row + 1) * board_size + column] == 'X':
            count_mine += 1
            # Below (diagonal) left
        if (column > 0) and board[(row + 1) * board_size + (column - 1)] == 'X':
            count_mine += 1
        # Below (diagonal) right
        if column < (board_size - 1) and board[(row + 1) * board_size + (column + 1)] == 'X':
            count_mine += 1

    # Check the right side element to see if a mine exists
    if column < (board_size - 1) and board[row * board_size + (column + 1)] == 'X':
        count_mine += 1

    # Check the left side element to see if a mine exists
    if (column > 0) and board[row * board_size + (column - 1)] == 'X':
        count_mine += 1

    return count_mine


def play_turn(board, row, column):
    """
    This function plays a turn using the provided row and column on the board. If a hidden mine is selected, it
    is changed to a "#" character. Otherwise, the number of adjacent mines to the selected position will replace
    the existing character. If there are no adjacent mines, the space character " " replaces the selected position.

    Arguments
    ---------
    board : A list representing the board
    row : An int representing the row (0-4) of the square being selected.
    column : An int representing the column (0-4) of the square being selected.

    Returns
    ---------
    Output 1 : a list representing the updated board.
    Output 2 : a bool with value "True" if a mine is selected, otherwise "False".

    Notes
    ---------
    Pre conditions: None
    Post condition: None
    """
    size = 5
    is_mine_selected = False

    # Calculates the index of a specified position on the board
    index = (row*size+column)

    # Check if specified position is a mine or not
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
    """
    This function determines if a player has won the game. This occurs when all positions that do not contain a
    mine have been selected.

    Arguments
    ---------
    board : A list representing the board.

    Returns
    ---------
    Output 1 : A bool representing if the game as been won (True) or has not been won (False).

    Notes
    ---------
    Pre conditions: None
    Post condition: None
    """
    for space in board:
        if space == 'O':
            return False
    return True


def play_game(positions):
    """
    This function plays the game from start to finish! The function play_game calls other functions created earlier.

    Arguments
    ---------
    positions : A list of lists indicating the positions that the mines will be placed in the board.

    Returns
    ---------
    This function has no outputs.

    Notes
    ---------
    Pre conditions: The board should first be initialised and have mines inserted at locations indicated by the input.
                    It should also display the initial state of the board with the mines hidden.
    Post condition: None
    """
    # Initialize the board
    minesweeper_board = initialise_board()

    # Inserting the new mines
    insert_mines(minesweeper_board, positions)

    # Display the initial board as the original board with mines hidden as 'O's
    print("Starting board:")
    display_board(minesweeper_board)

    # Play the game until it has been won or lost
    while True:
        # Obtain the row and column input from the user's end
        user_input = input("Enter row and column (separated by space): ")
        row, column = map(int, user_input.split())

        # Call the play_turn function, then update the board
        updated_board, is_mine_selected = play_turn(minesweeper_board, row, column)
        # Display the updated board
        display_board(updated_board)

        # Check if the game has been won. If won, it prints out a message.
        if check_win(updated_board):
            print("Congratulations, you have won the game!")
            break

        # If a mine has been selected, the game is over. It prints out a "game over" message.
        elif is_mine_selected:
            print("Game over! You've selected a mine. Better luck next time!")
            break


# Example usage:
# mine_positions = [[3, 2], [3, 1], [4, 3]]
# play_game(mine_positions)
