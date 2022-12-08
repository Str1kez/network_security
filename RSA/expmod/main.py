from tkinter import *
from tkinter import messagebox as mb
from typing import Optional

from exceptions import ValidationError
from RSA.expmod.tools import fast_bin_pow
from RSA.validation import expmod_validation


def get_input_data() -> Optional[tuple[int, int, int]]:
    n = number.get()
    e = exp.get()
    m = mod.get()
    try:
        n, e, m = expmod_validation(n, e, m)
    except ValidationError as e:
        mb.showerror(title="Ошибка при вводе", message=str(e))
        return
    return n, e, m


def set_processed_text(text: str):
    result.delete("0", END)
    result.insert("0", text)


def solve():
    data = get_input_data()
    if data is None:
        return
    n, e, m = data
    result_exp = fast_bin_pow(n, e, m)
    set_processed_text(str(result_exp))


win = Tk()


win["bg"] = "#fafafa"
win.title("Возведение в степень по модулю")
win.geometry("400x250")
win.resizable(False, False)


number_label = Label(win, bg=win['bg'], text="Число:")
number_label.place(relx=0.15, rely=0.05, relheight=0.07, relwidth=0.3)

number = Entry(win, bg="white", font=23)
number.place(relx=0.15, rely=0.13, relwidth=0.5, relheight=0.1)

# Ввод exp
exp_label = Label(win, text="Степень:", background=win["bg"])
exp_label.place(relx=0.15, rely=0.25, relwidth=0.3, relheight=0.07)
exp = Entry(win, bg="white", font=23)
exp.place(relx=0.15, rely=0.35, relwidth=0.5, relheight=0.1)

mod_label = Label(win, text="Mod", background=win['bg'])
mod_label.place(relx=0.15, rely=0.47, relwidth=0.3, relheight=0.07)
mod = Entry(win, bg='white', font=23)
mod.place(relx=0.15, rely=0.57, relwidth=0.5, relheight=0.1)

# Выбор функции
solve_button = Button(win, text="Решить!", command=solve)
solve_button.place(relx=0.15, rely=0.7, relwidth=0.3, relheight=0.1)

result = Entry(win, bg="white", font=23)
result.place(relx=0.15, rely=0.85, relwidth=0.5, relheight=0.1)


if __name__ == "__main__":
    win.mainloop()
