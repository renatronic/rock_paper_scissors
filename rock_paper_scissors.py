from tkinter import *
import random

# main window
root = Tk()
root.iconbitmap(r'C:/Users/m64/Downloads/python/rock_paper_scissors/rock.ico')
root.title('Rock Paper Scissors')
root.resizable(width = False, height = False)

click = True


# importing images
hand_rock_img = PhotoImage(file = r'C:/Users/m64/Downloads/python/rock_paper_scissors/hand_rock.png')
hand_paper_img = PhotoImage(file = r'C:/Users/m64/Downloads/python/rock_paper_scissors/hand_paper.png')
hand_scissors_img = PhotoImage(file = r'C:/Users/m64/Downloads/python/rock_paper_scissors/hand_scissors.png')

rock_img = PhotoImage(file = r'C:/Users/m64/Downloads/python/rock_paper_scissors/rock.png')
paper_img = PhotoImage(file = r'C:/Users/m64/Downloads/python/rock_paper_scissors/paper.png')
scissors_img = PhotoImage(file = r'C:/Users/m64/Downloads/python/rock_paper_scissors/scissors.png')

win_img = PhotoImage(file = r'C:/Users/m64/Downloads/python/rock_paper_scissors/win.png')
loose_img = PhotoImage(file = r'C:/Users/m64/Downloads/python/rock_paper_scissors/loose.png')
tie_img = PhotoImage(file = r'C:/Users/m64/Downloads/python/rock_paper_scissors/tie.png')


# creating buttons
button_rock = ''
button_paper = ''
button_scissors = ''


# defining functions
def play():
    global button_rock, button_paper, button_scissors
    
    button_rock = Button(root, image = hand_rock_img, command = lambda:you_pick('rock'))
    button_paper = Button(root, image = hand_paper_img, command = lambda:you_pick('paper'))
    button_scissors = Button(root, image = hand_scissors_img, command = lambda:you_pick('scissors'))

    button_rock.grid(root, row = 0, column = 0)
    button_paper.grid(root, row = 0, column = 1)
    button_scissors.grid(root, row = 0, column = 2)

def computer_pick():
    choice = random.choice(['rock', 'paper', 'scissors'])
    return choice

def you_pick():
    global click

    comp_pick = computer_pick()


root.mainloop()