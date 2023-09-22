# File: Wordle.py

"""
Section 3 
Developers: Eva Wu, Caleb Hefner
Scrum Master: Brayden Paul
Product Owner: Bronson Horne
"""

import random
import tkinter
from tkinter import *
from WordleDictionary import FIVE_LETTER_WORDS, FIVE_LETTER_WORDS_SPANISH
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS


def wordle():
    picked_word = ""
    word_list=[]

    #selected_language = gw.get_selected_language()



    def proceed_with_language_selection():
        nonlocal picked_word, word_list
        selected_language = var.get()

        if selected_language == 0:
            picked_word = random.choice(FIVE_LETTER_WORDS)
            word_list = FIVE_LETTER_WORDS
            
        elif selected_language == 1:
            picked_word = random.choice(FIVE_LETTER_WORDS_SPANISH)
            word_list = FIVE_LETTER_WORDS_SPANISH
        root.destroy()



    

    # pick the random word
    # if selected_language == 0:
    #     picked_word = random.choice(FIVE_LETTER_WORDS)
    #     word_list = FIVE_LETTER_WORDS
        
    # elif selected_language == 1:
    #     picked_word = random.choice(FIVE_LETTER_WORDS_SPANISH)
    #     word_list = FIVE_LETTER_WORDS_SPANISH

    def enter_action(s):

        CORRECT_COLOR = "#66BB66" # A shade of green
        PRESENT_COLOR = "#CCBB66" # A shade of brownish yellow
        MISSING_COLOR = "#999999" # A Shade of gray

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
            if word in word_list:
                gw.show_message( "Good Guess!" + picked_word)

                picked_word_used_positions = [False, False, False, False, False]
                word_letter_positions = [0, 1, 2, 3, 4]

                i = 0
                for letter in word:
                    if letter == picked_word[i]:
                        gw.set_square_color(current_row, i, CORRECT_COLOR)
                        picked_word_used_positions[i] = True
                        word_letter_positions.remove(i)
                    i += 1

                for i in word_letter_positions:
                    if word[i] in picked_word and not picked_word_used_positions[picked_word.index(word[i])]:
                        gw.set_square_color(current_row, i, PRESENT_COLOR)
                        picked_word_used_positions[picked_word.index(word[i])] = True
                    else:
                        gw.set_square_color(current_row, i, MISSING_COLOR)

                # check if the word matched picked word 
                if word == picked_word: 
                    # End game and congrat user
                    return gw.show_message("Congrats! Correct word is " + picked_word)         

                # set the new row 
                N_ROWS = gw.get_current_row()+1
                gw.set_current_row(N_ROWS)
                
            elif word not in word_list:
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
        
    selected_language = None
    root = tkinter.Tk()
    var = tkinter.IntVar()
    var2 = tkinter.IntVar()
    c1 = tkinter.Radiobutton(root, text='English',variable=var, value=0)
    c1.pack(anchor = W)
    c2 = tkinter.Radiobutton(root, text='Spanish',variable=var, value=1)
    c2.pack(anchor = W)
    c3 = tkinter.Checkbutton(root, text='Color',variable=var2, onvalue=1, offvalue=2)
    c3.pack(anchor = W)

    submit_button = tkinter.Button(root, text="Submit", command=proceed_with_language_selection)
    submit_button.pack()

    root.mainloop()

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
    
# Startup code

if __name__ == "__main__":
    wordle()
    
