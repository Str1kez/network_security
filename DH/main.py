from tkinter import *
from tkinter import messagebox as mb
from typing import Callable

from DH.tools import bsgs, get_primitive_root, get_safe_prime
from DH.validation import bsgs_validation, diffie_hellman_validation
from exceptions import ValidationError
from RSA.expmod import fast_bin_pow


def validate_data(func: Callable, *args) -> tuple[int, ...] | None:
    try:
        return func(*args)
    except ValidationError as exc:
        mb.showerror(title="Ошибка при вводе", message=str(exc))
        return


def generate():
    data = validate_data(diffie_hellman_validation, a_entry.get(), g_bit_entry.get(), p_bit_entry.get())
    if data is None:
        return
    a, g_bit, p_bit = data
    _p = get_safe_prime(p_bit)
    _g = get_primitive_root(g_bit, _p)
    p.set(str(_p))
    g.set(str(_g))
    _y = fast_bin_pow(_g, a, _p)
    y.set(str(_y))


def migrate():
    y_log_entry.delete(0, END)
    g_log_entry.delete(0, END)
    p_log_entry.delete(0, END)
    y_log_entry.insert(0, y.get())
    g_log_entry.insert(0, g.get())
    p_log_entry.insert(0, p.get())


def calculate():
    data = validate_data(bsgs_validation, y_log_entry.get(), g_log_entry.get(), p_log_entry.get())
    if data is None:
        return
    y, g, p = data
    a = bsgs(g, y, p)
    if a is None:
        return
    a_log_entry.delete(0, END)
    a_log_entry.insert(0, str(a))


win = Tk()

win["bg"] = "#fafafa"
win.title("Diffie-Hellman")
win.geometry("600x500")
win.resizable(False, False)


a_label = Label(win, bg=win['bg'], text="a =")
a_label.place(relx=0.01, rely=0.06, relheight=0.04, relwidth=0.1)

a_entry = Entry(win, bg="white", font=23)
a_entry.place(relx=0.08, rely=0.06, relwidth=0.26, relheight=0.04)

g_label = Label(win, bg=win['bg'], text="g =")
g_label.place(relx=0.01, rely=0.13, relheight=0.04, relwidth=0.1)

g = StringVar()
g_entry = Entry(win, bg="white", font=23, textvariable=g, state="readonly")
g_entry.place(relx=0.08, rely=0.13, relwidth=0.26, relheight=0.04)

p_label = Label(win, bg=win['bg'], text="p =")
p_label.place(relx=0.01, rely=0.21, relheight=0.04, relwidth=0.1)

p = StringVar()
p_entry = Entry(win, bg="white", font=23, textvariable=p, state="readonly")
p_entry.place(relx=0.08, rely=0.21, relwidth=0.26, relheight=0.04)

generate_button = Button(win, text="Сгенерировать", command=generate)
generate_button.place(relx=0.36, rely=0.06, relwidth=0.26, relheight=0.04)

g_bit_label = Label(win, bg=win['bg'], text="= size of g")
g_bit_label.place(relx=0.62, rely=0.13, relheight=0.04, relwidth=0.1)

g_bit_entry = Entry(win, bg="white", font=23)
g_bit_entry.place(relx=0.36, rely=0.13, relwidth=0.26, relheight=0.04)

p_bit_label = Label(win, bg=win['bg'], text="= size of p")
p_bit_label.place(relx=0.62, rely=0.21, relheight=0.04, relwidth=0.1)

p_bit_entry = Entry(win, bg="white", font=23)
p_bit_entry.place(relx=0.36, rely=0.21, relwidth=0.26, relheight=0.04)

y_label = Label(win, bg=win['bg'], text="y =")
y_label.place(relx=0.01, rely=0.29, relheight=0.04, relwidth=0.1)

y = StringVar()
y_entry = Entry(win, bg="white", font=23, textvariable=y, state="readonly")
y_entry.place(relx=0.08, rely=0.29, relwidth=0.54, relheight=0.04)

migrate_button = Button(win, text="Перенести", command=migrate)
migrate_button.place(relx=0.08, rely=0.4, relwidth=0.54, relheight=0.04)

# 1.2

y_log_label = Label(win, bg=win['bg'], text="y =")
y_log_label.place(relx=0.01, rely=0.5, relheight=0.04, relwidth=0.1)

y_log_entry = Entry(win, bg="white", font=23)
y_log_entry.place(relx=0.08, rely=0.5, relwidth=0.26, relheight=0.04)

g_log_label = Label(win, bg=win['bg'], text="g =")
g_log_label.place(relx=0.01, rely=0.58, relheight=0.04, relwidth=0.1)

g_log_entry = Entry(win, bg="white", font=23)
g_log_entry.place(relx=0.08, rely=0.58, relwidth=0.26, relheight=0.04)

p_log_label = Label(win, bg=win['bg'], text="p =")
p_log_label.place(relx=0.01, rely=0.66, relheight=0.04, relwidth=0.1)

p_log_entry = Entry(win, bg="white", font=23)
p_log_entry.place(relx=0.08, rely=0.66, relwidth=0.26, relheight=0.04)

calculate_button = Button(win, text="Считать", command=calculate)
calculate_button.place(relx=0.36, rely=0.5, relwidth=0.26, relheight=0.04)

a_log_label = Label(win, bg=win['bg'], text="= a")
a_log_label.place(relx=0.59, rely=0.58, relheight=0.04, relwidth=0.1)

a_log_entry = Entry(win, bg="white", font=23)
a_log_entry.place(relx=0.36, rely=0.58, relwidth=0.26, relheight=0.04)


if __name__ == "__main__":
    win.mainloop()
