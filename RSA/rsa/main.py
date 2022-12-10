from tkinter import *
from tkinter import messagebox as mb
from typing import Optional

from RSA.rsa.tools import get_prime, euler_function
from RSA.rsa.validation import bit_validation
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


def generate():
    p.delete(0, END)
    q.delete(0, END)
    e.delete(0, END)
    d.delete(0, END)
    n.delete(0, END)
    f_n.delete(0, END)
    bit_len.delete(0, END)
    try:
        bit_int = bit_validation(bit.get())
    except ValidationError as exc:
        mb.showerror(title="Ошибка при вводе", message=str(exc))
        return
    bit_len.insert(0, str(bit_int // 7))
    p_prime = get_prime(bit_int)
    p.insert(0, str(p_prime))
    q_prime = get_prime(bit_int)
    while q_prime == p_prime:
        q_prime = get_prime(bit_int)
    q.insert(0, str(q_prime))
    f_n.insert(0, str(euler_function(p_prime, q_prime)))
    e.insert()
    d.insert()
    n.insert()


def crypt():
    pass


def decrypt():
    pass


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
win.geometry("700x500")
win.resizable(False, False)


p_label = Label(win, bg=win['bg'], text="p =")
p_label.place(relx=0.01, rely=0.06, relheight=0.03, relwidth=0.1)

p = Entry(win, bg="white", font=23)
p.place(relx=0.08, rely=.06, relwidth=0.13, relheight=0.04)

q_label = Label(win, bg=win['bg'], text="q =")
q_label.place(relx=0.01, rely=0.11, relheight=0.03, relwidth=0.1)

q = Entry(win, bg="white", font=23)
q.place(relx=0.08, rely=.11, relwidth=0.13, relheight=0.04)

e_label = Label(win, bg=win['bg'], text="e =")
e_label.place(relx=0.01, rely=0.16, relheight=0.03, relwidth=0.1)

e = Entry(win, bg="white", font=23)
e.place(relx=0.08, rely=.16, relwidth=0.13, relheight=0.04)

d_label = Label(win, bg=win['bg'], text="d =")
d_label.place(relx=0.01, rely=0.21, relheight=0.03, relwidth=0.1)

d = Entry(win, bg="white", font=23)
d.place(relx=0.08, rely=.21, relwidth=0.13, relheight=0.04)

n_label = Label(win, bg=win['bg'], text="n =")
n_label.place(relx=0.01, rely=0.26, relheight=0.03, relwidth=0.1)

n = Entry(win, bg="white", font=23)
n.place(relx=0.08, rely=.26, relwidth=0.13, relheight=0.04)

f_n_label = Label(win, bg=win['bg'], text="f(n) =")
f_n_label.place(relx=0.01, rely=0.31, relheight=0.03, relwidth=0.1)

f_n = Entry(win, bg="white", font=23)
f_n.place(relx=0.08, rely=.31, relwidth=0.13, relheight=0.04)

generate_button = Button(win, text="Сгенерировать", command=generate)
generate_button.place(relx=0.07, rely=0.37, relwidth=0.15, relheight=0.04)

bit_label = Label(win, bg=win['bg'], text="bit =")
bit_label.place(relx=0.01, rely=0.45, relheight=0.03, relwidth=0.1)

bit = Entry(win, bg="white", font=23)
bit.place(relx=0.08, rely=0.45, relwidth=0.13, relheight=0.04)

bit_len_label = Label(win, bg=win['bg'], text="length =")
bit_len_label.place(relx=0.01, rely=0.5, relheight=0.03, relwidth=0.1)

bit_len = Entry(win, bg="white", font=23)
bit_len.place(relx=0.08, rely=0.5, relwidth=0.13, relheight=0.04)

input_text = Text(win, bg="white", font=23)
input_text.place(relx=0.24, rely=0.06, relwidth=.75, relheight=0.26)

crypt_button = Button(win, text="Зашифровать", command=crypt)
crypt_button.place(relx=0.3, rely=0.33, relwidth=0.28, relheight=0.05)

crypt_button = Button(win, text="Расшифровать", command=decrypt)
crypt_button.place(relx=0.65, rely=0.33, relwidth=0.28, relheight=0.05)

encrypt_text = Text(win, bg="white", font=23)
encrypt_text.place(relx=0.24, rely=0.39, relwidth=.75, relheight=0.26)

decrypt_text = Text(win, bg="white", font=23)
decrypt_text.place(relx=0.24, rely=0.66, relwidth=.75, relheight=0.26)

if __name__ == "__main__":
    win.mainloop()
