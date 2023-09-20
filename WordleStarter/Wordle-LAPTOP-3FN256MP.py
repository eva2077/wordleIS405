# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS



def wordle():

    # pick the random word
    picked_word = random.choice(FIVE_LETTER_WORDS)
    def enter_action(s):

        # set letter_ count as 0 
        letter_count = 0 
        # set var for word 
        word = ""
        # get current row 
        current_row = gw.get_current_row()
        # count how many letters were entered 
        count =0 
        while count < 5:
            letter = gw.get_square_letter(current_row,count)
            if letter != " ":
                letter_count += 1
                # concatnate letters into a word
                word += letter
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
            # turn the words entered into lowercase 
            word = word.lower()
            # check if the word is in the dictionary
            if word in FIVE_LETTER_WORDS:
                gw.show_message( "Good Guess!" + picked_word)
                # check if the word matched picked word 
                if word == picked_word: 
                    # End game and congrat user
                    return gw.show_message("Congrats! Correct word is " + picked_word)         

                # set the new row 
                N_ROWS = gw.get_current_row()+1
                gw.set_current_row(N_ROWS)
                
            elif word not in FIVE_LETTER_WORDS:
                gw.show_message("Not in the list")
                # clear the words 
                for count in range(5):
                    gw.set_square_letter(current_row,count," ")
                # set the row and let user try again 
                gw.set_current_row(current_row)
            # reset letter count to 0
            letter_count = 0 
        else:
            gw.show_message("Error!")
    


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
