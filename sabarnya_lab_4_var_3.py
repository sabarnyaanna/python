from tkinter import *
from tkinter.messagebox import askokcancel

# Клас Quitter (зазвичай у файлі quitter.py)
class Quitter(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.ask_to_quit)
        widget.pack(side=RIGHT, expand=YES, fill=BOTH)

    def ask_to_quit(self):
        ans = askokcancel('Verify exit', "Really quit?")
        if ans:
            self.master.destroy()

# Основна логіка
def fetch():
    print('Input => "%s"' % ent.get())

root = Tk()
root.title("Entry Demo")

# Поле вводу
ent = Entry(root)
ent.insert(0, 'Have a cigar')
ent.pack(side=TOP, fill=X)
ent.focus()

# ВИПРАВЛЕНО: додано '<Return>' для обробки натискання Enter
ent.bind('<Return>', (lambda event: fetch()))

# Кнопка Fetch
btn = Button(root, text='Fetch', command=fetch)
btn.pack(side=LEFT)

# Кнопка Quit (використовуємо наш клас)
Quitter(root).pack(side=RIGHT)

root.mainloop()