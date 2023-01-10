from tkinter import *
from PIL import Image, ImageTk
from enum import Enum

class Boxes:
    'The individual boxes within the board'
    numFilled = 0                                               # Number of boxes filled 
    values = [['Blank' for j in range(3)] for i in range(3)]    # Values of all the boxes on the board
    
    def __init__(self, x, y):
        self.img = ImageTk.PhotoImage(Image.open("Blank.png"))
        self.button = Button(image=self.img, padx=28, pady=20, command=lambda: self.clicked())  
        self.x = x 
        self.y = y 
        self.button.grid(row=x+2, column=y)

    def clicked(self):
        Boxes.numFilled += 1
        # Player 1 has clicked 
        if Boxes.numFilled %2 == 1:
            self.img = ImageTk.PhotoImage(Image.open("X.png"))
            Boxes.values[self.x][self.y] = 'X'
        else:
            self.img = ImageTk.PhotoImage(Image.open("O.png"))
            Boxes.values[self.x][self.y] = 'O'
        self.button.config(state='disabled', image=self.img)

        # A player can only win after 5 turns, then check if there is a win
        if Boxes.numFilled >= 5 and checkWin():
            # The previous player is (Box.numFilled - 1)%2
            winner.config(text="Player "+ (str)((Boxes.numFilled - 1)%2 + 1)+" Wins!")
            disableBoard()
        elif Boxes.numFilled == 9:
            winner.config(text="Draw")
            disableBoard()
        else:
            # Even numFilled is player 1 and Odd numFilled is player 2
            currPlayer.config(text="Player "+ (str)(Boxes.numFilled%2 + 1)+"'s Turn!")

    def restart():
        # Change all values back to the default Button
        box11.img = ImageTk.PhotoImage(Image.open("Blank.png"))
        box11.button.config(image=box11.img, state='normal')
        
        box12.img = ImageTk.PhotoImage(Image.open("Blank.png"))
        box12.button.config(image=box12.img, state='normal')
        
        box13.img = ImageTk.PhotoImage(Image.open("Blank.png"))
        box13.button.config(image=box13.img, state='normal')

        box21.img = ImageTk.PhotoImage(Image.open("Blank.png"))
        box21.button.config(image=box21.img, state='normal')
        
        box22.img = ImageTk.PhotoImage(Image.open("Blank.png"))
        box22.button.config(image=box22.img, state='normal')
        
        box23.img = ImageTk.PhotoImage(Image.open("Blank.png"))
        box23.button.config(image=box23.img, state='normal')

        box31.img = ImageTk.PhotoImage(Image.open("Blank.png"))
        box31.button.config(image=box31.img, state='normal')
        
        box32.img = ImageTk.PhotoImage(Image.open("Blank.png"))
        box32.button.config(image=box32.img, state='normal')
        
        box33.img = ImageTk.PhotoImage(Image.open("Blank.png"))
        box33.button.config(image=box33.img, state='normal')

        #Reset number count and values
        Boxes.numFilled = 0
        Boxes.values = [['Blank' for j in range(3)] for i in range(3)]
        currPlayer.config(text="Player "+ (str)(Boxes.numFilled%2 + 1)+"'s Turn!")
        winner.config(text="")

def checkWin():
    #Check the diagonal rows for a win
    if Boxes.values[0][0]==Boxes.values[1][1] and Boxes.values[1][1]==Boxes.values[2][2] and Boxes.values[1][1]!='Blank':
        return True
        
    if Boxes.values[0][2]==Boxes.values[1][1] and Boxes.values[1][1]==Boxes.values[2][0] and Boxes.values[0][2]!='Blank':
        return True 
    
    for i in range(3):
        #Check the rows for a win
        if Boxes.values[i][0]==Boxes.values[i][1] and Boxes.values[i][1]==Boxes.values[i][2] and Boxes.values[i][0]!='Blank':
            return True

    for i in range(3):
        #Check the columns for a win
        if Boxes.values[0][i]==Boxes.values[1][i] and Boxes.values[1][i]==Boxes.values[2][i] and Boxes.values[0][i]!='Blank':
            return True
    
    #Else there exists no wins
    return False

def disableBoard():
    box11.button.config(state='disabled')
    box12.button.config(state='disabled')
    box13.button.config(state='disabled')

    box21.button.config(state='disabled')
    box22.button.config(state='disabled')
    box23.button.config(state='disabled')

    box31.button.config(state='disabled')
    box32.button.config(state='disabled')
    box33.button.config(state='disabled')
        
root = Tk()
root.title('Tic Tac Toe')

title = Label(text="TIC TAC TOE", justify='center')
title.grid(row=0, column=0, columnspan=3)

currPlayer = Label(text="Player "+ (str)(Boxes.numFilled%2 + 1)+"'s Turn!", justify='center')
currPlayer.grid(row=1, column=0, columnspan=3)

winner = Label(text="", justify='center')
winner.grid(row=5, column=0, columnspan=3)

#Creating the individual boxes on the Board 
box11 = Boxes(0,0)
box12 = Boxes(0,1)
box13 = Boxes(0,2)

box21 = Boxes(1,0)
box22 = Boxes(1,1)
box23 = Boxes(1,2)

box31 = Boxes(2,0)
box32 = Boxes(2,1)
box33 = Boxes(2,2)

restartBttn = Button(root, text = "RESTART", command= lambda: Boxes.restart())
restartBttn.grid(row=6, column=0, columnspan=3)

root.mainloop()
