import tkinter as tk
from random import choice


def play(choice_user):
    choices = ["Камень", "Ножницы", "Бумага"]
    choice_computer = choice(choices)
    result_text.set(f"Компьютер выбрал: {choice_computer}")

    if choice_user == choice_computer:
        result.set("Ничья!")
    elif (choice_user == "Камень" and choice_computer == "Ножницы") or \
         (choice_user == "Ножницы" and choice_computer == "Бумага") or \
         (choice_user == "Бумага" and choice_computer == "Камень"):
        result.set("Вы победили!")
    else:
        result.set("Вы проиграли!")


root = tk.Tk()
root.title("Камень, ножницы, бумага")
root.geometry("400x300")
root.resizable(False, False)


title_label = tk.Label(root, text="Камень, ножницы, бумага", font=("Arial", 14, "bold"))
title_label.pack(pady=10)


btn_frame = tk.Frame(root)
btn_frame.pack()

for option in ["Камень", "Ножницы", "Бумага"]:
    btn = tk.Button(btn_frame, text=option, font=("Arial", 12), command=lambda opt=option: play(opt))
    btn.pack(side="left", padx=10)


result_text = tk.StringVar()
result_text.set("Сделайте выбор!")
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 12))
result_label.pack(pady=10)

result = tk.StringVar()
result_label2 = tk.Label(root, textvariable=result, font=("Arial", 12, "bold"))
result_label2.pack(pady=5)


author_label = tk.Label(root, text="Автор: ЮСупов Ф, 23/3", font=("Arial", 10))
author_label.pack(side="bottom", pady=10)

root.mainloop()