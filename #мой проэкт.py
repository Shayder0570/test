from tkinter import *
from math import sqrt


def solver(a, b, c):
    D = b * b - 4 * a * c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2 * a)

        x2 = (-b - sqrt(D)) / (2 * a)

        text = 'D = %s \n x1 = %s \n x2 = %s \n' % (D, x1, x2)
    else:
        text = 'D = %s \nЭто уравнени не имеет корней' % D
    return text


def inserter(value):
    output.delete('0.0', END)
    output.insert('0.0', value)


def handler():
    try:
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        inserter(solver(a_val, b_val, c_val))
    except ValueError:
        inserter('А вы точно всё ввели ?')

#ОКНО

w = Tk()
w.title('Решалка')
w.geometry('500x150+300+300')
w.resizable(width=True, height=True)
w.config(bg = '#1B45A7')
f_top = Frame(w)
f_bot = Frame(w)
f_top.pack()
f_bot.pack()

#СТРОКИ ВВОДА

a = Entry(f_top, width=5, font='Arial 16')
a.pack(side=LEFT, pady=10, padx=10)

a_lab = Label(f_top, text='x² +', font='Arial 16').pack(side=LEFT, pady=10)

b = Entry(f_top, width=5, font='Arial 16')
b.pack(side=LEFT, pady=10)

b_lab = Label(f_top, text='x +', font='Arial 16').pack(side=LEFT, pady=10)

c = Entry(f_top, width=5, font='Arial 16')
c.pack(side=LEFT, pady=10)

c_lab = Label(f_top, text='= 0', font='Arial 16').pack(side=LEFT, pady=10)

btn = Button(f_top, text='Ответ', font='Arial 17 bold', command=handler).pack(side=LEFT, pady=10, padx=10)

output = Text(f_bot, bg='blue', fg='yellow', font='Arial 17')
output.pack(expand=1, fill=BOTH, side=LEFT)




w.mainloop()