from tkinter import *
import random

def total_eradication(buttons):
    for btn in buttons:
        btn.destroy()
def r_click():
    total_eradication(buttons)
    lbl = Label(root, text="Ты угадал!", font=("Arial Bold", 40), bg=random.choice(color))
    lbl.place(x=300, y=350)

def f_click():
    total_eradication(buttons)
    lbl = Label(root, text="Ты не угадал>:(", font=("Arial Bold", 40), bg=random.choice(color))
    lbl.place(x=300, y=350)

def check(options):
    result = random.choice(options)
    options.remove(result)
    return result

color = ['red', 'green', 'blue', 'pink', 'orange', 'yellow']
colors = ['gold', 'cyan', 'green2', 'RosyBrown1', 'white']
options = ['Жми сюда', 'Это правильно', 'Чего ты ждешь', 'А может я']
buttons = []

root = Tk()

root.title("Игра в угадайку")

root.geometry("1000x800")

root["bg"] = random.choice(color)

d = random.randint(0, 4)
for i in range(4):
    if i == d:
        btn = Button(root, bg=random.choice(color), text=check(options), font=("Arial Bold", 20), command=r_click)
    else:
        btn = Button(root, bg=random.choice(color), text=check(options), font=("Arial Bold", 20), command=f_click)
    a = x=random.randint(0, 900)
    b = x=random.randint(0, 700)
    btn.place(x=a, y=b)
    buttons.append(btn)

root.mainloop()
