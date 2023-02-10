from tkinter import *
from tkinter import messagebox as mb


def generate():
    pass


def migrate():
    pass


def calculate():
    pass


win = Tk()

win["bg"] = "#fafafa"
win.title("Diffie-Hellman")
win.geometry("600x500")
win.resizable(False, False)


a_label = Label(win, bg=win['bg'], text="a =")
a_label.place(relx=0.01, rely=0.06, relheight=0.04, relwidth=0.1)

a = Entry(win, bg="white", font=23)
a.place(relx=0.08, rely=0.06, relwidth=0.26, relheight=0.04)

q_label = Label(win, bg=win['bg'], text="q =")
q_label.place(relx=0.01, rely=0.13, relheight=0.04, relwidth=0.1)

q = StringVar()
q_entry = Entry(win, bg="white", font=23, textvariable=q, state="readonly")
q_entry.place(relx=0.08, rely=0.13, relwidth=0.26, relheight=0.04)

p_label = Label(win, bg=win['bg'], text="p =")
p_label.place(relx=0.01, rely=0.21, relheight=0.04, relwidth=0.1)

p = StringVar()
p_entry = Entry(win, bg="white", font=23, textvariable=p, state="readonly")
p_entry.place(relx=0.08, rely=0.21, relwidth=0.26, relheight=0.04)

generate_button = Button(win, text="Сгенерировать", command=generate)
generate_button.place(relx=0.36, rely=0.06, relwidth=0.26, relheight=0.04)

q_bit_label = Label(win, bg=win['bg'], text="= size of q")
q_bit_label.place(relx=0.62, rely=0.13, relheight=0.04, relwidth=0.1)

q_bit = Entry(win, bg="white", font=23)
q_bit.place(relx=0.36, rely=0.13, relwidth=0.26, relheight=0.04)

p_bit_label = Label(win, bg=win['bg'], text="= size of p")
p_bit_label.place(relx=0.62, rely=0.21, relheight=0.04, relwidth=0.1)

p_bit = Entry(win, bg="white", font=23)
p_bit.place(relx=0.36, rely=0.21, relwidth=0.26, relheight=0.04)

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
