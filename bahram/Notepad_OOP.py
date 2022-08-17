import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class Notepad:
    # Creating tkinter main window
    win = tk.Tk()
    title = win.title("ScrolledText Widget")


    def createLable(self,ttk):
        self.ttk = ttk
        self.ttk.Label(self.win,
		text = "My Notepad",
		font = ("Times New Roman", 15),
		background = 'white',
		foreground = "black").grid(column = 0,
									row = 0)
    def createTextArea(self,win,width,height):
        win = tk
        win = win.Tk()
        text_area = scrolledtext.ScrolledText(win,
									wrap = tk.WORD,
									width = width,
									height = height,
									font = ("Times New Roman",
											15))
        text_area.grid(column = 0, pady = 10, padx = 10)
        # Placing cursor in the text area
        text_area.focus()
        win.mainloop()

obj1 = Notepad()
obj1.createLable(ttk)
obj1.createTextArea(bin,50,20)

