import os

APP_PATH = os.path.dirname(os.path.abspath(__file__))

LEN_WORDS_CHARS = 5  # char per word

BOLD = "\033[1m"
END_COLORAMA = "\033[0;0m"

SET_CHANGE_TRAINING_WORD = 'change training'
SET_RESET_DATA = 'reset'
EXIT_PROGRAM = 'exit'

INI_FILE = 'data.ini'

# SAVE IN INI FILE
training_word = 'hello world'
total_missed_char = 0
total_typed_char = 0
total_minutes = 0


