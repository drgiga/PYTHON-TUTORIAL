import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class Notepad:
    text_area = None
    def __init__(self):
        # Creating tkinter main window
        win = tk.Tk()
        win.title("ScrolledText Widget")

        # Title Label
        ttk.Label(win,
                text = "My Notepad",
                font = ("Times New Roman", 15),
                background = 'white',
                foreground = "black").grid(column = 0,
                                            row = 0)

        # Creating scrolled text
        # area widget
        self.text_area = scrolledtext.ScrolledText(win,
                                            wrap = tk.WORD,
                                            width = 40,
                                            height = 10,
                                            font = ("Times New Roman",
                                                    15))

        self.text_area.grid(column = 0, pady = 10, padx = 10)

        # Placing cursor in the text area
        self.text_area.focus()
        
        win.mainloop()

    def setText(self,inputText):
        inputText = self.text_area.insert(tk.END, inputText)
        self.inputText = inputText
    def getText(self):
        return print(self.inputText)
    
obj1 = Notepad()
obj1.setText("fgfdgdfgdfgdfgdfg")
obj1.getText()
