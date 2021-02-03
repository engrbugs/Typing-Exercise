#! /usr/bin/env python3
from colorama import init
import threading
import time
import logging
import keyboard  # using module keyboard
from lib import active_window
import write_config
import var
from colorama import Fore

WINDOW_TEXT = ''

LEN_WORDS_CHARS = 5  # char per word

BOLD = "\033[1m"
END = "\033[0;0m"

SET_CHANGE_TRAINING_WORD = 'change training'

INI_FILE = 'data.ini'


def timer_loop():
    global current_time
    loop_exit = None
    start_time = 0
    end_time = 0
    start_pressed = None
    readed = ''
    while not loop_exit:  # making a loop
        if str(active_window.get_active_window()) == WINDOW_TEXT:
            try:  # used try so that if user pressed other than the given key error will not be shown
                readed = keyboard.read_key()
                if readed == 'enter':
                    readed = ''
                if readed != '' and start_pressed is None:  # if key 'q' is pressed
                    readed = ''
                    start_pressed = True
                    start_time = time.time()
                    # logging.info("Timer  : start")
                    # break  # finishing the loop
                elif keyboard.is_pressed('enter') and start_pressed is True:
                    start_pressed = None
                    # logging.info("Timer  : end")
                    end_time = time.time()
                    # loop_exit = True
                    current_time = end_time - start_time
                    readed = ''
            except:
                break  # if user pressed a key other than the given key the loop will break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init()
    write_config.read_ini()
    WINDOW_TEXT = str(active_window.get_active_window())

    # print(Fore.RED + 'some red text')
    # print(Back.GREEN + 'and with a green background')
    # print(Style.DIM + 'and in dim text')
    # print(Style.RESET_ALL)
    # print('back to normal now')
    print(f'Typing Exercise: {Fore.BLUE}{BOLD}{var.training_word}{END} (type to change: {SET_CHANGE_TRAINING_WORD})')

    word = 'engrbugs@gmail.com'
    exit_word = 'exit'
    current_time = 0

    logging.info("Main  : before creating thread")
    t1 = threading.Thread(target=timer_loop)
    logging.info("Main  : before running thread")
    t1.start()
    logging.info("Main  : waiting for thread to finish")
    x = ''
    while x != 'exit':
        print('Type to start', end=":     ")
        x = input()
        if x.lower().strip() == SET_CHANGE_TRAINING_WORD:
            print('Type new training word', end=":     ")
            xy = input()

            training_word = xy.strip()

            write_config.write_ini()
            print('New training word saved!')
            print(
                f'Typing Exercise: {Fore.BLUE}{BOLD}{training_word}{END} '
                f'(type to change: {SET_CHANGE_TRAINING_WORD})')
        print(f'{x} and {current_time}')

    #

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
