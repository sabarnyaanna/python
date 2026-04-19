from tkinter import *
from tkinter.messagebox import askokcancel

class Quitter(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        # Прив'язуємо команду до нашого методу
        widget = Button(self, text='Quit', command=self.ask_to_quit)
        widget.pack(side=RIGHT, expand=YES, fill=BOTH)

    def ask_to_quit(self):
        ans = askokcancel('Verify exit', "Really quit?")
        if ans:
            # self.destroy() закриває вікно та завершує програму
            self.master.destroy()

if __name__ == '__main__':
    root = Tk() # Краще явно створювати кореневе вікно
    Quitter(root).mainloop()