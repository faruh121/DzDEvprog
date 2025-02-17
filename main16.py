import tkinter as tk
from tkinter import messagebox


def confirm_selection():
    selected_checkbuttons = []
    for i, var in enumerate(check_vars):
        if var.get():
            selected_checkbuttons.append(f"Вариант {i + 1}")

    selected_radiobutton = radio_var.get()


    message = "Выбранные Checkbutton:\n" + "\n".join(selected_checkbuttons) + "\n\n"
    message += f"Выбранный Radiobutton: Вариант {selected_radiobutton}" if selected_radiobutton else "Radiobutton не выбран"


    count = len(selected_checkbuttons)
    message += f"\n\nКоличество выбранных Checkbutton: {count}"


    messagebox.showinfo("Результаты выбора", message)


root = tk.Tk()
root.title("Выбор вариантов")
root.geometry("300x300")


check_vars = [tk.IntVar() for _ in range(3)]
check_labels = ["Вариант 1", "Вариант 2", "Вариант 3"]


for i, label in enumerate(check_labels):
    checkbutton = tk.Checkbutton(root, text=label, variable=check_vars[i])
    checkbutton.pack(anchor='w')


radio_var = tk.IntVar()


radio_labels = ["Радио 1", "Радио 2", "Радио 3"]
for i, label in enumerate(radio_labels):
    radiobutton = tk.Radiobutton(root, text=label, variable=radio_var, value=i + 1)
    radiobutton.pack(anchor='w')


confirm_button = tk.Button(root, text="Подтвердить", command=confirm_selection)
confirm_button.pack(pady=20)


root.mainloop()