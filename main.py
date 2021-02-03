#! /usr/bin/env python3
from colorama import init
import threading
import time
import keyboard  # using module keyboard
from lib import active_window
import write_config
import var
from colorama import Fore

WINDOW_TEXT = ''


def timer_loop():
    global current_time
    loop_exit = None
    start_time = 0
    start_pressed = None
    while not loop_exit:  # making a loop
        if str(active_window.get_active_window()) == WINDOW_TEXT:
            readkey = keyboard.read_key()
            if readkey == 'enter':
                readkey = ''
            if readkey != '' and start_pressed is None:  # if key 'q' is pressed
                start_pressed = True
                start_time = time.time()
            elif keyboard.is_pressed('enter') and start_pressed is True:
                start_pressed = None
                end_time = time.time()
                current_time = end_time - start_time


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init()
    write_config.read_ini()
    WINDOW_TEXT = str(active_window.get_active_window())
    print(f'Typing Exercise: {Fore.BLUE}{var.BOLD}{var.training_word}{var.END} '
          f'(type to change: {var.SET_CHANGE_TRAINING_WORD})')
    current_time = 0

    # start timer listener
    t1 = threading.Thread(target=timer_loop)
    t1.start()

    x = ''
    while x != 'exit':
        print('Type to start', end=":     ")
        x = input()
        if x.lower().strip() == var.SET_CHANGE_TRAINING_WORD:
            print('Type new training word', end=":     ")
            xy = input()
            training_word = xy.strip()
            write_config.write_ini()
            print('New training word saved!')
            print(
                f'Typing Exercise: {Fore.BLUE}{var.BOLD}{training_word}{var.END} '
                f'(type to change: {var.SET_CHANGE_TRAINING_WORD})')
        print(f'{x} and {current_time}')


    # x = ''
    # while x.lower() != exit_word:
    #     print('Type Now:', end=">    ")
    #     inputted_string = input()
    #     #  Clean white spaces from beginning to end.
    #     x = inputted_string.strip()
    #     if x.lower() == word:
    #         print('Correct!')
    #     elif x.lower() == exit_word:
    #         quit()
    #     else:
    #         print('Incorrect!')
