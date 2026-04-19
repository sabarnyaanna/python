from tkinter import *
import tkinter.filedialog


def LoadFile(ev):
    # Виправлено: діалогове вікно викликається через askopenfilename
    fn = tkinter.filedialog.askopenfilename(
        filetypes=[('Text files', '.txt'), ('All files', '*')]
    )

    if not fn:  # Перевірка, якщо користувач натиснув "Скасувати"
        return

    textbox.delete('1.0', 'end')
    # Додано encoding='utf-8' для підтримки кирилиці
    with open(fn, 'rt', encoding='utf-8') as f:
        textbox.insert('1.0', f.read())


root = Tk()
root.title("Simple Text Loader")

# Панель для кнопок
panelFrame = Frame(root, height=30, bg='blue')
panelFrame.pack(side='top', fill='x')

# Фрейм для тексту
textFrame = Frame(root)
textFrame.pack(side='bottom', fill='both', expand=True)

# Текстове поле та скроллбар
textbox = Text(textFrame, font='Arial 12', wrap='word')
scrollbar = Scrollbar(textFrame)

# Зв'язка скроллбара та тексту
scrollbar.config(command=textbox.yview)
textbox.config(yscrollcommand=scrollbar.set)

textbox.pack(side='left', fill='both', expand=True)
scrollbar.pack(side='right', fill='y')

# Кнопка завантаження
loadBtn = Button(panelFrame, text='Open')
loadBtn.bind("<Button-1>", LoadFile)
# Використовуйте place обережно, або змініть на pack/grid
loadBtn.place(x=10, y=5, width=60, height=20)

root.mainloop()