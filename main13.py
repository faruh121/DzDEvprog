import tkinter as tk

def on_button_click():
    print("Кнопка нажата")

def on_enter(event):
    print("Курсор вошел в границы кнопки")

def on_leave(event):
    print("Курсор покинул кнопку")


root = tk.Tk()
root.title("Пример Tkinter")

button = tk.Button(root, text="Нажми меня", command=on_button_click)
button.pack(pady=20)


button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

root.mainloop()