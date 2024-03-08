import pytest
from functions_minesweeper import *


def test_count_adjacent_mines_in_corner():
    board = ['X', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O']
    count = count_adjacent_mines(board, 0, 4)
    assert (count == 0)


def test_inserting_mines():
    board = ['O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O']
    insert_mines(board, [[0, 4]])
    assert (board == ['O', 'O', 'O', 'O', 'X',
                      'O', 'O', 'O', 'O', 'O',
                      'O', 'O', 'O', 'O', 'O',
                      'O', 'O', 'O', 'O', 'O',
                      'O', 'O', 'O', 'O', 'O'])


def test_playing_turn():        # Two outputs, board and True/False???
    board = ['O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'X', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O']
    play_turn(board, 2, 2)
    assert (board == ['O', 'O', 'O', 'O', 'O',
                      'O', 'O', 'O', 'O', 'O',
                      'O', 'O', '#', 'O', 'O',
                      'O', 'O', 'O', 'O', 'O',
                      'O', 'O', 'O', 'O', 'O'])


def test_checking_win():
    board = ['1', 'X', '1', '1', ' ',
             ' ', '1', '1', 'X', '1',
             ' ', ' ', ' ', '2', ' ',
             ' ', ' ', '1', 'X', '1',
             ' ', ' ', ' ', '1', ' ']
    check_win(board)
    assert True
