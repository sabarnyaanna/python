from tkinter import *


def printer(event):
    # Коли ми використовуємо .bind(), Tkinter автоматично передає об'єкт 'event'
    x = var.get()
    print(f"Значення змінної: {x}")


root = Tk()
root.title("Scale Demo")

var = IntVar()
var.set(5)

# Слайдери, прив'язані до однієї змінної 'var'
sca1 = Scale(root, orient=VERTICAL, length=200,
             from_=0, to=10, tickinterval=2, resolution=1,
             variable=var)

sca2 = Scale(root, orient=HORIZONTAL, length=200,
             from_=0, to=10, tickinterval=2, resolution=1,
             variable=var)

lab = Label(root, text='Лабораторна робота \n Graphical User Interface',
            font='Arial 18')

but = Button(root, text='Узнать значение переменной', width=30, height=3,
             bg='grey', fg='red', font='Arial 12')

# ВИПРАВЛЕНО: додано '<Button-1>' (ліва кнопка миші)
but.bind('<Button-1>', printer)

lab.pack()
sca1.pack()
sca2.pack()
but.pack()

root.mainloop()