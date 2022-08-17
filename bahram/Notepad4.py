import tkinter, tkinter.scrolledtext

class Notepad(tkinter.Frame):

    def __init__(self, master = None):
        
        super().__init__()
        
        self.master = master
        self.pack()

        
        self.message_text = tkinter.scrolledtext.ScrolledText(self.master)
        #self.chat_text.insert(tkinter.END, "self.temp")
        self.message_text.pack()

    def set_message(self,input_message):
        self.message_text.insert(tkinter.END, input_message)
    def get_message(self):
        return print(self.message_text)   


x = tkinter.Tk()
note1 = Notepad(x)
note1.set_message("Hello My name is Davoud. I'm Learning Python Programming \nLanguage.Hello My name is Davoud. I'm Learning Python Programming Language.")
note1.mainloop()



