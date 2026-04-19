from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

def close_win():
    if askyesno("Exit", "Do you want to quit?"):
        root.destroy()

def about():
    # Виправлено розрив рядка
    showinfo("Editor", "This is text editor.\n(test version)")

def _open():
    op = askopenfilename()
    if op: # Перевірка, чи не скасував користувач вибір
        txt.delete(1.0, END) # Очищуємо поле перед відкриттям
        with open(op, "r", encoding='utf-8') as f:
            txt.insert(END, f.read())

def _save():
    sa = asksaveasfilename()
    if sa:
        letter = txt.get(1.0, END)
        # Додано encoding='utf-8' для підтримки української мови
        with open(sa, "w", encoding='utf-8') as f:
            f.write(letter)

root = Tk()
root.title("Python Editor")

m = Menu(root)
root.config(menu=m)

# Меню File
fm = Menu(m, tearoff=0)
m.add_cascade(label="File", menu=fm)
fm.add_command(label="Open...", command=_open)
fm.add_command(label="Save...", command=_save)
fm.add_separator()
fm.add_command(label="Exit", command=close_win)

# Меню Help
hm = Menu(m, tearoff=0)
m.add_cascade(label="Help", menu=hm)
hm.add_command(label="About", command=about)

txt = Text(root, width=50, height=20, font=("Arial", 12))
txt.pack(fill=BOTH, expand=True)

root.mainloop()