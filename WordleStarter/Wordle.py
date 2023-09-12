# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    current_row=0
    def enter_action(s):
        current_row=gw.get_current_row()+1
        gw.set_current_row(current_row)
        gw.show_message(current_row)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
