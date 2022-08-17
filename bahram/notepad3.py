import socket 
import tkinter, tkinter.scrolledtext

class GUI(tkinter.Frame):
    temp = None
    def __init__(self, master = None):
        super().__init__()
        self.master = master
        self.pack()

        

        self.chat_text = tkinter.scrolledtext.ScrolledText(self.master)
        #self.chat_text.insert(tkinter.END, "self.temp")
        self.chat_text.pack()

        """self.entry_text = tkinter.StringVar()
        self.entry = tkinter.Entry(master, textvariable = self.entry_text)
        self.entry.pack()

        self.entry.bind("<Return>", self.send_message)"""

    def set_message(self,input):
        self.chat_text.insert(tkinter.END, input)
    def get_message(self):
        return print(self.chat_text)   


x = tkinter.Tk()
gui = GUI(x)
gui.set_message("Hello My name is Davoud. I'm Learning Python Programming Language.")
gui.mainloop()

