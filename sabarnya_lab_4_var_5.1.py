from tkinter import *

def create_tree_window(title, text, width, height):
    window = Toplevel()
    window.title(title)
    window.config(bg="black")
    window.geometry(f"{width}x{height}")
    label = Label(
        window,
        text=text,
        fg="white",
        bg="black",
        font=("Times New Roman", 20, "italic bold")
    )
    label.pack(expand=True)

root = Tk()
root.title("Lumberjack demo")
root.geometry("250x100")
Label(root, text="Main window").pack(pady=5)
Button(root, text="Quit All", command=root.quit).pack(pady=5)
create_tree_window("Sing..", "The Larch!", 250, 150)
create_tree_window("Sing..", "The Pine!", 250, 150)
create_tree_window("Sing..", "The Giant Redwood!", 450, 150)

root.mainloop()