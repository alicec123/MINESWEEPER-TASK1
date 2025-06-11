# Minesweeper game in Python

This game is a simplified, text-based version of Minesweeper.

The game creates a 5x5 grid where each cell is initially hidden and marked with 'O'. Mines are hidden at specified positions on the board (provided at the start). The player selects a cell by entering a row and column. If the cell contains a mine, the game ends in a loss. If it doesn't, the cell reveals the number of adjacent mines. The player wins by revealing all non-mine cells without triggering any mines.

Cells with no adjacent mines are marked with a space ' ', and mines remain hidden until triggered (then shown as '#').
