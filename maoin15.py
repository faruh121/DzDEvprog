# Разработать программу, содержащую основное окно с двумя кнопками, по нажатию на которые открываются разные окна произвольного содержания (не пустые).
# В дз отправить исходный код и интерфейс программы (скриншот).
import tkinter as tk
from tkinter import messagebox


def open_window1():
    window1 = tk.Toplevel(root)
    window1.title("Первое окно")
    window1.geometry("300x200")
    label1 = tk.Label(window1, text="Это первое окно!", font=("Arial", 16))
    label1.pack(pady=20)
    button1 = tk.Button(window1, text="Закрыть", command=window1.destroy)
    button1.pack(pady=10)


def open_window2():
    window2 = tk.Toplevel(root)
    window2.title("Второе окно")
    window2.geometry("300x200")
    label2 = tk.Label(window2, text="Это второе окно!", font=("Arial", 16))
    label2.pack(pady=20)
    button2 = tk.Button(window2, text="Закрыть", command=window2.destroy)
    button2.pack(pady=10)


root = tk.Tk()
root.title("Основное окно")
root.geometry("400x300")


button1 = tk.Button(root, text="Открыть первое окно", command=open_window1)
button1.pack(pady=20)

button2 = tk.Button(root, text="Открыть второе окно", command=open_window2)
button2.pack(pady=20)


root.mainloop()