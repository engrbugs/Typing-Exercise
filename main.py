#! /usr/bin/env python3

import threading
import time
import os

from colorama import init, Fore, Style
import keyboard  # using module keyboard

from lib import active_window, write_config
import var

WINDOW_TEXT = ''
VERSION = '1.0.0'


def timer_loop():
    global current_time
    global loop_exit
    start_time = 0
    start_pressed = None
    while not loop_exit:  # making a loop
        if str(active_window.get_active_window()) == WINDOW_TEXT:
            readkey = keyboard.read_key()
            if readkey == 'enter':
                readkey = ''
            elif readkey == 'backspace':
                var.total_missed_char += 1

            if readkey != '' and start_pressed is None:  # if key 'q' is pressed
                start_pressed = True
                start_time = time.time()
            elif keyboard.is_pressed('enter') and start_pressed is True:
                start_pressed = None
                end_time = time.time()
                current_time = end_time - start_time


def check_word(word):
    incorrect_char = 0
    result = ''
    i = 0
    for i in range(len(word)):
        if i > len(var.training_word) - 1:
            incorrect_char += 1
            result += Fore.RED + word[i] + var.END_COLORAMA
        else:
            if word[i] != var.training_word[i]:
                result += Fore.RED + word[i] + var.END_COLORAMA
            else:
                result += word[i]
    if i < len(var.training_word) - 1:
        incorrect_char += len(var.training_word[i+1:])
        result += Fore.RED + var.training_word[i+1:] + var.END_COLORAMA
    if incorrect_char == 0:
        result = Style.BRIGHT + result + var.END_COLORAMA
    return result, incorrect_char


def welcome_display():
    print(f'Typing Exercise{VERSION}: {Fore.BLUE}{var.BOLD}{var.training_word}{var.END_COLORAMA} '
          f'(type to change: {var.SET_CHANGE_TRAINING_WORD})')


if __name__ == '__main__':
    init()
    if os.path.exists(var.APP_PATH + f'\\{var.INI_FILE}'):
        write_config.read_ini()
    WINDOW_TEXT = str(active_window.get_active_window())
    welcome_display()
    current_time = 0
    loop_exit = None
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
            var.training_word = xy.strip()
            write_config.write_ini()
            print('New training word saved!')
            welcome_display()
            break
        elif x.lower().strip() == var.EXIT_PROGRAM:
            loop_exit = True
            quit()
        elif x.lower().strip() == var.SET_RESET_DATA:
            print('Are you sure? (yes/no)', end=":     ")
            xy = input()
            if xy.lower().strip() == 'yes':
                print('Data reset.')
                var.total_missed_char = 0
                var.total_typed_char = 0
                var.total_minutes = 0
                write_config.write_ini()
            welcome_display()
            continue
        report_word, report_mistakes = check_word(x)
        var.total_missed_char += report_mistakes
        var.total_typed_char += len(x)
        var.total_minutes += current_time / 60
        accuracy = 1 - (var.total_missed_char/var.total_typed_char)
        wpm = var.total_typed_char / (var.total_minutes * var.LEN_WORDS_CHARS)
        write_config.write_ini()
        print(f'{report_word} (ACC: {str(round(accuracy * 100, 2))}%) '
              f'for {str(round(current_time, 2))}s '
              f'(WPM = {str(round(wpm, 2))}) '
              f'Type \'{var.SET_RESET_DATA}\' to reset data')
