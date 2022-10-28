from random import choice
from tkinter import *
from tkinter import messagebox

import numpy as np
from tools import decode, encode, text_in_binary, xor

from exceptions import ValidationError
from validation import xor_validate


def update_text(text_field: Text, data: str):
    text_field.delete(1.0, END)
    text_field.insert(1.0, data)


def encryption_text():
    source = text_origin.get(1.0, END).strip()
    en_key = key.get(1.0, END).strip()
    try:
        xor_validate(source, en_key, bin_key.get(1.0, END).strip())
    except ValidationError as e:
        messagebox.showerror(title="Ошибка", message=str(e))
        return
    update_text(text_bin_origin, text_in_binary(source))
    if en_key:
        update_text(bin_key, text_in_binary(en_key))
    cipher = xor(text_bin_origin.get(1.0, END).strip(), bin_key.get(1.0, END).strip())
    update_text(text_bin_received, cipher)
    update_text(text_received, encode(cipher))


def decryption():
    bin_text = text_bin_received.get(1.0, END).strip()
    en_key = key.get(1.0, END).strip()
    try:
        xor_validate(bin_text, en_key, bin_key.get(1.0, END).strip())
    except ValidationError as e:
        messagebox.showerror(title="Ошибка", message=str(e))
        return
    decoded = xor(bin_text, bin_key.get(1.0, END).strip())
    update_text(text_bin_decrypt, decoded)
    update_text(text_decrypt, decode(decoded))


def gen_key():
    key.delete(1.0, END)
    text_bin_received.delete(1.0, END)
    text_received.delete(1.0, END)
    origin_text = text_origin.get(1.0, END).strip()
    if not origin_text:
        messagebox.showerror(title="Ошибка", message="Вы не ввели текст")
        return
    binary_text_size = len(text_in_binary(origin_text))
    my_key = np.random.randint(0, 2, binary_text_size)
    if abs(np.sum(my_key == 1) - np.sum(my_key == 0)) > 1:
        ones = np.sum(my_key == 1) - binary_text_size // 2
        while ones:
            index = choice(np.argwhere(my_key == (ones > 0)))
            my_key[index] = ones < 0
            ones += 1 if ones < 0 else -1
    my_key = "".join(str(x) for x in my_key)
    update_text(bin_key, my_key)


root = Tk()
frame = Frame(root)
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
root.title("Гаммирование")
root.geometry("550x650")

title_origin = Label(frame, text="Исходный текст", padx=15)
title_origin.grid(row=0, column=0, stick="w")
text_origin = Text(frame, width=60, height=4, wrap=WORD)
text_origin.grid(row=1, column=0, columnspan=4, stick="we")

title_bin_origin = Label(frame, text="Двоичное представление текста", padx=15)
title_bin_origin.grid(row=2, column=0, stick="w")
text_bin_origin = Text(frame, width=60, height=4, wrap=WORD)
text_bin_origin.grid(row=3, column=0, columnspan=4, stick="we")

title_key = Label(frame, text="Ключ", padx=15)
title_key.grid(row=4, column=0, stick="w")
key = Text(frame, width=10, height=1, wrap=WORD)
key.grid(row=5, column=0, columnspan=2, stick="we")

btn_gen = Button(frame, text="Сгенерировать", bg="#708090", command=gen_key)
btn_gen.grid(row=5, column=2, stick="w")

title_bin_key = Label(frame, text="Двоичное представление ключа", padx=15)
title_bin_key.grid(row=6, column=0, stick="w")
bin_key = Text(frame, width=10, height=1, wrap=WORD)
bin_key.grid(row=7, column=0, columnspan=2, stick="we")

btn_crypt = Button(
    frame,
    text="Зашифровать",
    activebackground="#7FFFD4",
    bg="#E0FFFF",
    command=encryption_text,
)
btn_crypt.grid(row=8, column=0, stick="w")

title_received = Label(frame, text="Полученное сообщение", padx=15)
title_received.grid(row=9, column=0, stick="w")
text_received = Text(frame, width=60, height=4, wrap=WORD)
text_received.grid(row=10, column=0, columnspan=4, stick="we")

title_bin_received = Label(frame, text="Двоичное представление полученного сообщения", padx=15)
title_bin_received.grid(row=11, column=0, stick="w")
text_bin_received = Text(frame, width=60, height=4, wrap=WORD)
text_bin_received.grid(row=12, column=0, columnspan=4, stick="we")

btn_decrypt = Button(
    frame,
    text="Расшифровать",
    activebackground="#FF6347",
    bg="#FFA07A",
    command=decryption,
)
btn_decrypt.grid(row=13, column=0, stick="w")

title_decrypt = Label(frame, text="Расшифрованное сообщение", padx=15)
title_decrypt.grid(row=14, column=0, stick="w")
text_decrypt = Text(frame, width=60, height=4, wrap=WORD)
text_decrypt.grid(row=15, column=0, columnspan=4, stick="we")

title_bin_decrypt = Label(frame, text="Двоичное представление расшифрованного сообщения", padx=15)
title_bin_decrypt.grid(row=16, column=0, stick="w")
text_bin_decrypt = Text(frame, width=60, height=4, wrap=WORD)
text_bin_decrypt.grid(row=17, column=0, columnspan=4, stick="we")


root.grid_columnconfigure(0, minsize=200)
root.grid_columnconfigure(1, minsize=100)

root.mainloop()  # запуск постоянного цикла
