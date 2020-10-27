# ROCK-PAPER-SCISSORS GAME WITH THE RESULT OF THE SERIES PLAYED IN TKINTER

import tkinter
import random
stats = [5]                                                                                                                              # blank list to store result of game

def get_winner(call):
    if random.random() <= (1 / 3):                                                                                                       # computer selecting on random
        throw = "rock"                                                                                                                   # out of the three choices
    elif (1 / 3) < random.random() <= (2 / 3):                                                                                           # rock,paper or scissors
        throw = "scissor"                                                                                                                # as it's move
    else:
        throw = "paper"

    if(throw == "rock" and call == "paper") or (throw == "paper" and call == "scissor") or (throw == "scissor" and call == "rock"):
        stats.append('W')                                                                                                                # checking the player choice
        result = 'YOU WON!!!'                                                                                                            # against the computer
    elif throw == call:                                                                                                                  # to declare if the player
        stats.append('D')                                                                                                                # lost or won or
        result = "It's a DRAW"                                                                                                           # if the match is draw
    else:
        stats.append('L')
        result = 'YOU LOST!'

    global output                                                                                                                        # declaring geme result as output globally
    output.config(text="Comp did:" + throw + "\n" + result)                                                                              # to be reused later anywhere
def pass_s():
    get_winner("scissor")                                                                                                                # player's choice
def pass_r():
    get_winner("rock")                                                                                                                   # player's choice
def pass_p():
    get_winner("paper")                                                                                                                  # player's choice

def serie():
    for i in stats: lst = i
    if stats.count('L') > stats.count('W'):
        results = "You lost the series."                                                                                                 # series result calculation
    elif stats.count('L') == stats.count('W'):
        results = "Series is Draw"                                                                                                       # to check win,loss or draw series
    else:
        results = "You WON the series"


    global series                                                                                                                        # declaring series globally to be reused
    series.config(text=result)


from tkinter import *
window = Tk()                                                                                                                            # creating tkinter window
scissor = Button(window, text='Scissors', bg="#ff9999", padx=10, pady=5, command=pass_s, width=10)                                       # player button
rock = Button(window, text='Rock', bg="#80ff80", padx=10, pady=5, command=pass_r, width=10)                                              # player button
paper = Button(window, text='Paper', bg="#3399ff", padx=10, pady=5, command=pass_p, width=10)                                            # player button
output=Label(window, width=20, fg='red', text='Whats your call?')                                                                        # computer's move
match = Button(window,text='Match result',command=serie)                                                                                 # series result check button
series=Label(window, width=20, fg='blue', text='The result of series is:')                                                               # result of series match
scissor.pack(side='left')
rock.pack(side='left')
paper.pack(side='left')
output.pack(side='left')
match.pack()
series.pack()
window.mainloop()
