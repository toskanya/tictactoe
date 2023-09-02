SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
SCREEN_COLOR = (225, 225, 225)

BOARD_WIDTH = 810
BOARD_HEIGHT = 810
BOARD_POS = ((SCREEN_WIDTH - BOARD_WIDTH) / 2, (SCREEN_HEIGHT - BOARD_HEIGHT) / 2)
BOARD_COLOR = (225, 229, 204)

LINE_COLOR = (102, 51, 0)
LINE_WIDTH = 10

STEP = BOARD_WIDTH / 3

MARKER_WIDTH = STEP - 100

O_COLOR = (100, 225, 100)
O_WIDTH = 12
X_COLOR = (100, 100, 225)
X_WIDTH = 15

FONT_COLOR = (150, 0, 0)
FONT_PATH = r'C:\Users\trand\longg\Document\cs50 harvard\tic tac toe project\super_boys.ttf'
FONT_SIZE = 100
FONT_POS = (BOARD_WIDTH / 2, BOARD_HEIGHT / 2)

result = {
    -1: 'Player O wins',
     1: 'Player X wins',
     0: 'Draw',
}

Human = {
    'X': 1,
    'O': -1,
}