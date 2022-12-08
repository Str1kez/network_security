from tkinter import *
from tkinter import messagebox as mb
from typing import Optional

from exceptions import ValidationError
from RSA.euclidean.tools import euclidean_algorithm
from RSA.validation import euclidean_validation


def get_input_data() -> Optional[tuple[int, int]]:
    first, second = a.get(), b.get()
    try:
        first, second = euclidean_validation(first, second)
    except ValidationError as e:
        mb.showerror(title="Ошибка при вводе", message=str(e))
        return
    return first, second


def set_processed_text(first: str, second: str):
    s.delete("0", END)
    t.delete("0", END)
    s.insert("0", first)
    t.insert("0", second)


def solve():
    data = get_input_data()
    if data is None:
        return
    a, b = data
    s, t = euclidean_algorithm(a, b)
    set_processed_text(str(s), str(t))


win = Tk()


win["bg"] = "#fafafa"
win.title("Расширенный алгоритм Евклида")
win.geometry("400x250")
win.resizable(False, False)


a_label = Label(win, bg=win['bg'], text="Число a:")
a_label.place(relx=0.15, rely=0.03, relheight=0.07, relwidth=0.3)

a = Entry(win, bg="white", font=23)
a.place(relx=0.15, rely=0.1, relwidth=0.5, relheight=0.1)

# Ввод exp
b_label = Label(win, text="Число b:", background=win["bg"])
b_label.place(relx=0.15, rely=0.22, relwidth=0.3, relheight=0.07)
b = Entry(win, bg="white", font=23)
b.place(relx=0.15, rely=0.32, relwidth=0.5, relheight=0.1)

solve_button = Button(win, text="Решить!", command=solve)
solve_button.place(relx=0.15, rely=0.44, relwidth=0.3, relheight=0.07)

s_label = Label(win, text="s", background=win['bg'])
s_label.place(relx=0.15, rely=0.53, relwidth=0.3, relheight=0.07)
s = Entry(win, bg='white', font=23)
s.place(relx=0.15, rely=0.62, relwidth=0.5, relheight=0.1)

# Выбор функции

t_label = Label(win, text="t", background=win['bg'])
t_label.place(relx=0.15, rely=0.74, relwidth=0.3, relheight=0.07)
t = Entry(win, bg="white", font=23)
t.place(relx=0.15, rely=0.82, relwidth=0.5, relheight=0.1)


if __name__ == "__main__":
    win.mainloop()
