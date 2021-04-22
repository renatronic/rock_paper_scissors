from tkinter import *
import random

root = Tk()
root.iconbitmap('rock.ico')
root.title('Rock Paper Scissors')
root.resizable(width = False, height = False)

click = True


# images
hand_rock = PhotoImage(file = 'hand_rock.png')
hand_paper = PhotoImage(file = 'hand_paper.png')
hand_scissors = PhotoImage(file = 'hand_scissors.png')

rock = PhotoImage(file = 'rock.png')
paper = PhotoImage(file = 'paper.png')
scissors = PhotoImage(file = 'scissors.png')

win = PhotoImage(file = 'win.png')
loose = PhotoImage(file = 'loose.png')
tie = PhotoImage(file = 'tie.png')


# buttons
button_rock = ''
button_paper = ''
button_scissors = ''


# functions
def play():
    pass

def computer_pick():
    pass

def you_puck():
    pass

root.mainloop()