from tkinter import *
from tkinter import messagebox as mb
from typing import Optional

from exceptions import ValidationError
from RSA.rsa.cipher import code_to_text, parse_codes, rsa_cipher, text_to_code
from RSA.rsa.tools import (euler_function, get_prime, get_private_key,
                           get_public_key)
from RSA.rsa.validation import bit_validation, params_validation


def get_input_data() -> Optional[tuple[int, int, int, int]]:
    try:
        return params_validation(p.get(), q.get(), e.get()) + (bit_validation(bit.get()),)
    except ValidationError as exc:
        mb.showerror(title="Ошибка при вводе", message=str(exc))
        return


def generate():
    p.delete(0, END)
    q.delete(0, END)
    e.delete(0, END)
    try:
        bit_int = bit_validation(bit.get())
    except ValidationError as exc:
        mb.showerror(title="Ошибка при вводе", message=str(exc))
        return
    p_prime = get_prime(bit_int)
    p.insert(0, str(p_prime))
    q_prime = get_prime(bit_int)
    while q_prime == p_prime:
        q_prime = get_prime(bit_int)
    q.insert(0, str(q_prime))
    public_key = get_public_key(euler_function(p_prime, q_prime))
    e.insert(0, str(public_key))


def prepare_config():
    data = get_input_data()
    if data is None:
        return
    _p, _q, _e, _bit_int = data
    # d.delete(0, END)
    # n.delete(0, END)
    # f_n.delete(0, END)
    # bit_len.delete(0, END)

    # bit_len.insert(0, str(_bit_int // 8))
    # f_n.insert(0, str(euler_function(_p, _q)))
    # d.insert(0, str(get_private_key(euler_function(_p, _q), _e)))
    bit_len.set(str(_bit_int // 8))
    f_n.set(str(euler_function(_p, _q)))
    d.set(str(get_private_key(euler_function(_p, _q), _e)))
    n.set(str(_p * _q))


def crypt():
    prepare_config()
    text = input_text.get(1.0, END)
    _e, _n = int(e.get()), int(n.get())
    codes = text_to_code(text, int(bit_len.get()))
    ciphered_codes = rsa_cipher(codes, _e, _n)
    encrypt_text.delete(1.0, END)
    encrypt_text.insert(1.0, ' '.join(map(str, ciphered_codes)))


def decrypt():
    data = get_input_data()
    if data is None:
        return
    text = encrypt_text.get(1.0, END).strip()
    _d, _n = int(d.get()), int(n.get())
    encrypted_codes = parse_codes(text)
    codes = rsa_cipher(encrypted_codes, _d, _n)
    decrypt_text.delete(1.0, END)
    decrypt_text.insert(1.0, code_to_text(codes, int(bit_len.get())))


win = Tk()


win["bg"] = "#fafafa"
win.title("RSA")
win.geometry("700x500")
win.resizable(False, False)


p_label = Label(win, bg=win['bg'], text="p =")
p_label.place(relx=0.01, rely=0.06, relheight=0.03, relwidth=0.1)

p = Entry(win, bg="white", font=23)
p.place(relx=0.08, rely=0.06, relwidth=0.13, relheight=0.04)

q_label = Label(win, bg=win['bg'], text="q =")
q_label.place(relx=0.01, rely=0.11, relheight=0.03, relwidth=0.1)

q = Entry(win, bg="white", font=23)
q.place(relx=0.08, rely=0.11, relwidth=0.13, relheight=0.04)

e_label = Label(win, bg=win['bg'], text="e =")
e_label.place(relx=0.01, rely=0.16, relheight=0.03, relwidth=0.1)

e = Entry(win, bg="white", font=23)
e.place(relx=0.08, rely=0.16, relwidth=0.13, relheight=0.04)

d_label = Label(win, bg=win['bg'], text="d =")
d_label.place(relx=0.01, rely=0.21, relheight=0.03, relwidth=0.1)

d = StringVar()
d_entry = Entry(win, bg="white", font=23, textvariable=d, state="readonly")
d_entry.place(relx=0.08, rely=0.21, relwidth=0.13, relheight=0.04)

n_label = Label(win, bg=win['bg'], text="n =")
n_label.place(relx=0.01, rely=0.26, relheight=0.03, relwidth=0.1)

n = StringVar()
n_entry = Entry(win, bg="white", font=23, textvariable=n, state="readonly")
n_entry.place(relx=0.08, rely=0.26, relwidth=0.13, relheight=0.04)

f_n_label = Label(win, bg=win['bg'], text="f(n) =")
f_n_label.place(relx=0.01, rely=0.31, relheight=0.03, relwidth=0.1)

f_n = StringVar()
f_n_entry = Entry(win, bg="white", font=23, textvariable=f_n, state="readonly")
f_n_entry.place(relx=0.08, rely=0.31, relwidth=0.13, relheight=0.04)

generate_button = Button(win, text="Сгенерировать", command=generate)
generate_button.place(relx=0.07, rely=0.37, relwidth=0.15, relheight=0.04)

bit_label = Label(win, bg=win['bg'], text="bit =")
bit_label.place(relx=0.01, rely=0.45, relheight=0.03, relwidth=0.1)

bit = Entry(win, bg="white", font=23)
bit.place(relx=0.08, rely=0.45, relwidth=0.13, relheight=0.04)

bit_len_label = Label(win, bg=win['bg'], text="length =")
bit_len_label.place(relx=0.01, rely=0.5, relheight=0.03, relwidth=0.1)

bit_len = StringVar()
bit_len_entry = Entry(win, bg="white", font=23, textvariable=bit_len, state="readonly")
bit_len_entry.place(relx=0.08, rely=0.5, relwidth=0.13, relheight=0.04)

input_text = Text(win, bg="white", font=23)
input_text.place(relx=0.24, rely=0.06, relwidth=0.75, relheight=0.26)

crypt_button = Button(win, text="Зашифровать", command=crypt)
crypt_button.place(relx=0.3, rely=0.33, relwidth=0.28, relheight=0.05)

crypt_button = Button(win, text="Расшифровать", command=decrypt)
crypt_button.place(relx=0.65, rely=0.33, relwidth=0.28, relheight=0.05)

encrypt_text = Text(win, bg="white", font=23)
encrypt_text.place(relx=0.24, rely=0.39, relwidth=0.75, relheight=0.26)

decrypt_text = Text(win, bg="white", font=23)
decrypt_text.place(relx=0.24, rely=0.66, relwidth=0.75, relheight=0.26)

if __name__ == "__main__":
    win.mainloop()
