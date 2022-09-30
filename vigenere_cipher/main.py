from tkinter import *
from tkinter import messagebox as mb

from tools import ValidationError, validate, vigenere_cipher


def get_input_text() -> tuple[str, str] | None:
    text_list = input_text.get("1.0", END).strip().split('\n')
    text = ''.join(text_list)
    key = key_entry.get()
    is_en = lang_var.get()
    try:
        validate(text, key, is_en)
    except ValidationError as e:
        mb.showerror(title='Ошибка при вводе',
                     message=str(e))
        return
    return text, key


def set_processed_text(text: str):
    output_text.delete("1.0", END)
    output_text.insert("1.0", text)


def crypt():
    data = get_input_text()
    if data is None:
        return
    text, key = data
    set_processed_text(vigenere_cipher(text, key, lang_var.get()))


def decrypt():
    data = get_input_text()
    if data is None:
        return
    text, key = data
    set_processed_text(vigenere_cipher(text, key, lang_var.get(), decr=-1))


win = Tk()


win['bg'] = '#fafafa'
win.title('Шифр Виженера')
win.geometry('600x450')
win.resizable(False, False)


# Основа для ввода текста
frame_top = Frame(win, bg='red')
frame_top.place(relx=.15, rely=.075, relwidth=.7, relheight=.3)

input_label = Label(frame_top, bg=win['bg'], text='Введите текст', font=20)
input_label.place(relheight=.2, relwidth=1)

input_text = Text(frame_top, bg='white', font=23)
input_text.place(rely=.2, relwidth=1, relheight=.8)

# Выбор опций и функции
frame_middle = Frame(win, bg=win['bg'])
frame_middle.place(relx=.15, rely=.375, relwidth=.7, relheight=.25)

# Выбор языка
lang_var = IntVar()

ru_button = Radiobutton(frame_middle, text='Русский', variable=lang_var, value=0,
                        background=win['bg'], relief=GROOVE)
en_button = Radiobutton(frame_middle, text='Английский', variable=lang_var, value=1,
                        background=win['bg'], relief=GROOVE)
ru_button.place(relx=.05, rely=.15, relwidth=.3)
en_button.place(relx=.05, rely=.6, relwidth=.3)

# Ввод ключа
key_frame = Frame(frame_middle, bg='black')
key_frame.place(relx=.37, rely=.11, relheight=.27, relwidth=.58)
key_label = Label(key_frame, text='Ключ:', background=win['bg'])
key_label.place(relwidth=.3, relheight=1)
key_entry = Entry(key_frame)
key_entry.place(relx=.3, relwidth=.7, relheight=1)

# Выбор функции
crypt_button = Button(frame_middle, text='Зашифровать', command=crypt)
decrypt_button = Button(frame_middle, text='Расшифровать', command=decrypt)
crypt_button.place(relx=.37, rely=.55)
decrypt_button.place(relx=.67, rely=.55)

# Основа для вывода текста
frame_bottom = Frame(win, bg='blue')
frame_bottom.place(relx=.15, rely=.625, relwidth=.7, relheight=.3)

output_text = Text(frame_bottom, bg='white', font=23)
output_text.place(relwidth=1, relheight=1)


if __name__ == '__main__':
    win.mainloop()
