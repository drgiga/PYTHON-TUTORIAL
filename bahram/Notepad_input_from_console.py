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
        self.input_message = input_message
    def get_message(self):
        return self.input_message  


x = tkinter.Tk()
cmd_text = input('Please Write a Message: > ')
note1 = Notepad(x)
note1.set_message(cmd_text)
note1.mainloop()
output = note1.get_message()
print(output)



