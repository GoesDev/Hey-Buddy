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


global counter
counter = tk.StringVar()


def start_counter():
    seconds = 1 * 60

    def count():
        nonlocal seconds
        if seconds > 0:
            mins, secs = divmod(seconds, 60)
            timer = f'{mins:02}:{secs:02}'
            counter.set(timer)
            print(timer)
            seconds -= 1
            root.after(1000, count)
        else:
            counter.set('00:00')

    count()


def window_main():
    """
    Função que cria a janela principal do app
    """
    # Corrija a definição de var_string
    counter.set("00:00")

    ttk.Button(frm, text="Pomodoro").grid(column=1, row=0)
    ttk.Label(frm, textvariable=counter).grid(column=1, row=1)
    ttk.Button(frm, text="START",
               command=start_counter).grid(column=0, row=2)
    ttk.Button(frm, text="RESET").grid(column=2, row=2)
    ttk.Label(frm, text="-->").grid(column=0, row=3)
    ttk.Label(frm, text="2x Game Chess").grid(column=1, row=3)
    ttk.Label(frm, text="2/2").grid(column=2, row=3)

    # Crie os widgets na janela


window_main()

root.mainloop()
