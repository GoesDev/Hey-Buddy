import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Hey Buddy!")

frm = ttk.Frame(root, padding=10)
frm.grid()


def clear_widgets():
    """
    Function that clears widgets on the screen
    """
    for widget in frm.winfo_children():
        widget.destroy()


def window_main():
    """
    Função que cria a janela principal do app
    """

    ttk.Button(frm, text="Pomodoro").grid(column=1, row=0)

    ttk.Label(frm, text="21:44").grid(column=1, row=1)

    ttk.Button(frm, text="START").grid(column=0, row=2)
    ttk.Button(frm, text="RESET").grid(column=2, row=2)

    ttk.Label(frm, text="2x Game Chess").grid(column=0, row=3, columnspan=3)


window_main()

root.mainloop()
