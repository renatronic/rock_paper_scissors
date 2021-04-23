from tkinter import *
import random

# main window
root = Tk()
root.iconbitmap(r'C:/Users/m64/Downloads/python/rock_paper_scissors/img/rock.ico')
root.title('Rock Paper Scissors')
root.resizable(width = False, height = False)

click = True


# importing images
hand_rock_img = PhotoImage(file = r'C:/Users/m64/Downloads/python/rock_paper_scissors/img/hand_rock.png')
hand_paper_img = PhotoImage(file = r'C:/Users/m64/Downloads/python/rock_paper_scissors/img/hand_paper.png')
hand_scissors_img = PhotoImage(file = r'C:/Users/m64/Downloads/python/rock_paper_scissors/img/hand_scissors.png')

rock_img = PhotoImage(file = r'C:/Users/m64/Downloads/python/rock_paper_scissors/img/rock.png')
paper_img = PhotoImage(file = r'C:/Users/m64/Downloads/python/rock_paper_scissors/img/paper.png')
scissors_img = PhotoImage(file = r'C:/Users/m64/Downloads/python/rock_paper_scissors/img/scissors.png')

win_img = PhotoImage(file = r'C:/Users/m64/Downloads/python/rock_paper_scissors/img/win.png')
loose_img = PhotoImage(file = r'C:/Users/m64/Downloads/python/rock_paper_scissors/img/loose.png')
tie_img = PhotoImage(file = r'C:/Users/m64/Downloads/python/rock_paper_scissors/img/tie.png')


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

    button_rock.grid(row = 0, column = 0)
    button_paper.grid(row = 0, column = 1)
    button_scissors.grid(row = 0, column = 2)

def computer_pick():
    choice = random.choice(['rock', 'paper', 'scissors'])
    return choice

def you_pick(your_choice):
    global click

    comp_pick = computer_pick()

    if click == True:
        if your_choice == 'rock':
            button_rock.configure(image = rock_img)
            if comp_pick == 'rock':
                button_paper.configure(image = rock_img)
                button_scissors.configure(image = tie_img)
                click = False
            elif comp_pick == 'paper':
                button_paper.configure(image = paper_img)
                button_scissors.configure(image = loose_img)
                click = False
            else:
                button_paper.configure(image = scissors_img)
                button_scissors.configure(image = win_img)
                click = False

        elif your_choice == 'paper':
            button_paper.configure(image = paper_img)
            if comp_pick == 'rock':
                button_rock.configure(image = rock_img)
                button_scissors.configure(image = win_img)
                click = False
            elif comp_pick == 'paper':
                button_rock.configure(image = paper_img)
                button_scissors.configure(image = tie_img)
                click = False
            else:
                button_rock.configure(image = scissors_img)
                button_scissors.configure(image = loose_img)
                click = False
                
        elif your_choice == 'scissors':
            button_scissors.configure(image = scissors_img)
            if comp_pick == 'rock':
                button_paper.configure(image = rock_img)
                button_rock.configure(image = loose_img)
                click = False
            elif comp_pick == 'paper':
                button_paper.configure(image = paper_img)
                button_rock.configure(image = win_img)
                click = False
            else:
                button_paper.configure(image = scissors_img)
                button_rock.configure(image = tie_img)
                click = False
    else:
        if your_choice == 'rock' or your_choice == 'paper' or your_choice == 'scissors':
            button_rock.configure(image = hand_rock_img)
            button_paper.configure(image = hand_paper_img)
            button_scissors.configure(image = hand_scissors_img)
            click = True

play()

root.mainloop()