from tkinter import *

root = Tk()
root.title("Menu Resize Demo")

def sq1():
    fra.config(width=200, height=200)
    print('Resized to 200x200')

def sq2():
    fra.config(width=400, height=400)
    print('Resized to 400x400')

# Створюємо фрейм
fra = Frame(root, width=300, height=100, bg="Black")
# КРИТИЧНО: забороняємо фрейму стискатися під вміст
fra.pack_propagate(False)
fra.pack()

# Налаштування меню
m = Menu(root)
root.config(menu=m)

cm = Menu(m, tearoff=0)
m.add_cascade(label="File", menu=cm)

sm = Menu(m, tearoff=0)
m.add_cascade(label="Edit", menu=sm)
sm.add_command(label="200x200", command=sq1)
sm.add_command(label="400x400", command=sq2)

root.mainloop()