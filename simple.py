#this just a starter for anyone 
from tkinter import *
from tkinter import messagebox as mbx

class basic_app:
    def __init__(self, master):
        self.clickme = Button(master, text="click" command=self.sayhello)
        self.click.grid(row=1, column=1)
        
        
    def sayhello(self):
        mbx.showinfo("hello")
        
    
    
    
    
    
root = Tk()
obj = basic_app(root)
root.mainloop()
