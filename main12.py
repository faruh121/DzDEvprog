import tkinter as tk


root = tk.Tk()
root.title("Интерфейс с grid")
root.geometry("400x300")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)


top_label = tk.Label(root, text="Привет", font=("Arial", 14), bg="lightgray", width=20, height=2)
top_label.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)


middle_label = tk.Label(root, text="Как дела?", font=("Arial", 12), bg="white", width=10, height=2, relief="solid")
middle_label.grid(row=1, column=0, columnspan=2, sticky="n", pady=10)


bottom_label = tk.Label(root, text="Пока", font=("Arial", 14), bg="lightgray", width=20, height=2)
bottom_label.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)


root.mainloop()