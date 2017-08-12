# this just a starter for anyone

from tkinter import *
from tkinter import messagebox as mbx


class basic_app:
    
    """ sets up environment """
    
    def __init__(self, master):
        self.click = Button(master, text="click", command = self.sayhello)
        self.click.grid(row=1, column=1)

        
    """app functions"""
    
    def sayhello(self):
        mbx.showinfo("click registered","hello")


root = Tk()
obj = basic_app(root)
root.mainloop()
