GRID_SIDE_LENGTH = 3
GRID_CELL_COUNT = GRID_SIDE_LENGTH * GRID_SIDE_LENGTH

HUMAN_NAME    = "Player"
COMPUTER_NAME = "Computer"

BLANK_SYMBOL    = "."
HUMAN_SYMBOL    = "O"
COMPUTER_SYMBOL = "X"

BLANK_CELL_VALUE    = 0
HUMAN_CELL_VALUE    = 1
COMPUTER_CELL_VALUE = GRID_SIDE_LENGTH + 1

SYMBOL_DICTIONARY = {
    BLANK_CELL_VALUE    : BLANK_SYMBOL,
    HUMAN_CELL_VALUE    : HUMAN_SYMBOL,
    COMPUTER_CELL_VALUE : COMPUTER_SYMBOL
}

HUMAN_PENULTIMATE_WIN_VALUE = (GRID_SIDE_LENGTH - 1) * HUMAN_CELL_VALUE

HUMAN_WIN_LINE_VALUE    = GRID_SIDE_LENGTH * HUMAN_CELL_VALUE
COMPUTER_WIN_LINE_VALUE = GRID_SIDE_LENGTH * COMPUTER_CELL_VALUE

# Base scoring of importent scenarios on the "scale" of the grid to ensure minor scenarios remain low value relatively.
SCORE_COMPUTER_VICTORY           = GRID_CELL_COUNT * GRID_CELL_COUNT
SCORE_PREVENT_HUMAN_VICTORY      = SCORE_COMPUTER_VICTORY - 1
SCORE_CENTER_CELL_BIAS           = 5
SCORE_COMPUTER_CELL_ON_LINE      = 2
SCORE_HUMAN_CELL_ON_LINE         = 1