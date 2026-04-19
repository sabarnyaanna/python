from tkinter import *

root = Tk()
root.title("My Editor") # Додаємо заголовок вікна

# Створюємо головне меню
m = Menu(root)
root.config(menu=m)

# Створюємо вкладку "File"
fm = Menu(m, tearoff=0) # tearoff=0 прибирає пунктирну лінію
m.add_cascade(label="File", menu=fm)
fm.add_command(label="Open...")
fm.add_command(label="New")
fm.add_command(label="Save...")
fm.add_separator() # Додає роздільну лінію для зручності
fm.add_command(label="Exit", command=root.destroy) # Прив'язуємо закриття вікна

# Створюємо вкладку "Help"
hm = Menu(m, tearoff=0)
m.add_cascade(label="Help", menu=hm)
hm.add_command(label="Help")
hm.add_command(label="About")

# Важливо: mainloop має викликатися саме так
root.mainloop()