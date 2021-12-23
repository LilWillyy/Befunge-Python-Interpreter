import tkinter as tk
import BefungeInterpreter as BFI

class UI:
    def __init__(self):
        self.app = tk.Tk()
        self.app.geometry("1000x1000")

        self.columns = 25
        self.rows = 40
        self.c = 0
        self.r = 0
        self.textboxes = []

        self.code_output = []
        self.NUMS = "1234567890"
   
    def createUI(self):
        for i in range(self.columns): # Creating the Second Dimension for the array.
            self.textboxes.append([])
        for i in range(len(self.textboxes)): # Set up the Input for the UI.
            for j in range(self.rows):
                x = tk.Entry(self.app, width=2)
                x.grid(column=j, row=i)

                self.textboxes[i].append(x)
        
        runBtn = tk.Button(self.app, text="RUN PROGRAM", command=self.runProgram)
        runBtn.grid(column=40) # Make the button that runs the program.
   
    def moveRight(self, event):
        if self.c != self.columns - 1: self.c += 1
        self.textboxes[self.r][self.c].focus()

    def moveLeft(self, event):
        if self.c != 0: self.c -= 1
        self.textboxes[self.r][self.c].focus()

    def moveUp(self, event):
        if self.r != 0: self.r -= 1
        self.textboxes[self.r][self.c].focus()

    def moveDown(self, event):
        if self.r != self.rows - 1: self.r += 1
        self.textboxes[self.r][self.c].focus()

    def getChar(self, i: int, j: int):
        chr = self.textboxes[i][j].get()
        if not chr: return ' '

        if chr[0] in self.NUMS: return int(chr[0])
        else: return chr[0]

    def runProgram(self):
        for i in range(len(self.textboxes)):
            self.code_output.append([])
            for j in range(len(self.textboxes[i])):
                chr = self.getChar(i, j)
                self.code_output[i].append(chr)
        BFI.run(self.code_output)
        self.app.destroy()
        
    def mainloop(self):
        self.app.bind('<Up>', self.moveUp)
        self.app.bind('<Down>', self.moveDown)
        self.app.bind('<Right>', self.moveRight)
        self.app.bind('<Left>', self.moveLeft)

        self.app.mainloop()
        

ui = UI()
ui.createUI()
ui.mainloop()

"""
   !!!IMPORTANT: MAKE THIS A CLASS SO IMPORT WILL WORK
"""



