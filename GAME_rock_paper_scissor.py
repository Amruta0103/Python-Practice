# ROCK-PAPER-SCISSORS GAME WITH THE RESULT OF THE SERIES PLAYED IN TKINTER

import tkinter
import random
stats = [5]

def get_winner(call):
    if random.random() <= (1 / 3):
        throw = "rock"
    elif (1 / 3) < random.random() <= (2 / 3):
        throw = "scissor"
    else:
        throw = "paper"

    if(throw == "rock" and call == "paper") or (throw == "paper" and call == "scissor") or (throw == "scissor" and call == "rock"):
        stats.append('W')
        result = 'YOU WON!!!'
    elif throw == call:
        stats.append('D')
        result = "It's a DRAW"
    else:
        stats.append('L')
        result = 'YOU LOST!'

    global output
    output.config(text="Comp did:" + throw + "\n" + result)
def pass_s():
    get_winner("scissor")
def pass_r():
    get_winner("rock")
def pass_p():
    get_winner("paper")

def serie():
    for i in stats: lst = i
    if stats.count('L') > stats.count('W'):
        results = "You lost the series."
    elif stats.count('L') == stats.count('W'):
        results = "Series is Draw"
    else:
        results = "You WON the series"


    global series
    series.config(text=results)


from tkinter import *
window = Tk()

scissor = Button(window, text='Scissors', bg="#ff9999", padx=10, pady=5, command=pass_s, width=10)
rock = Button(window, text='Rock', bg="#80ff80", padx=10, pady=5, command=pass_r, width=10)
paper = Button(window, text='Paper', bg="#3399ff", padx=10, pady=5, command=pass_p, width=10)
output=Label(window, width=20, fg='red', text='Whats your call?')
match = Button(window,text='Match result',command=serie)
series=Label(window, width=20, fg='blue', text='The result of series is:')
scissor.pack(side='left')
rock.pack(side='left')
paper.pack(side='left')
output.pack(side='left')
match.pack()
series.pack()
window.mainloop()