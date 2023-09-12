# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    
    def enter_action(s):
        letter_count = 0 
        # get current row 
        current_row = gw.get_current_row()
        # count how many letters were entered 
        count =0 
        while count < 5:
            letter = gw.get_square_letter(current_row,count)
            if letter != " ":
                letter_count += 1
            count +=1
        # Checking if user entered in 5 letters 
        if letter_count < 5:
            # reset letter count 
            letter_count = 0 
            # tell user to enter 5 letters 
            gw.show_message("Please enter in 5 letters")
            # reset row to the current one 
            gw.set_current_row(N_ROWS-1)
        elif letter_count == 5:
            gw.show_message("Good guess!")
            letter_count = 0 
        else:
            gw.show_message("Error!")
        # prepare for next row
        N_ROWS=gw.get_current_row()+1
        # set the new row
        gw.set_current_row(N_ROWS)


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
