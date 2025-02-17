import tkinter as tk
from tkinter import messagebox


def clear_listbox():
    listbox.delete(0, tk.END)

def show_selected():
    selected_items = listbox.curselection()  
    if not selected_items:
        messagebox.showinfo("Выбор", "Ничего не выбрано.")
        return

    selected_text = [listbox.get(i) for i in selected_items]  
    messagebox.showinfo("Выбранные элементы", "\n".join(selected_text))


root = tk.Tk()
root.title("Программа с Listbox")
root.geometry("300x400")


listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
elements = ["Элемент 1", "Элемент 2", "Элемент 3", "Элемент 4", "Элемент 5"]
for element in elements:
    listbox.insert(tk.END, element)
listbox.pack(pady=20)


clear_button = tk.Button(root, text="Очистить Listbox", command=clear_listbox)
clear_button.pack(pady=10)


show_button = tk.Button(root, text="Показать выбранные элементы", command=show_selected)
show_button.pack(pady=10)


root.mainloop()