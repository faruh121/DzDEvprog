import tkinter as tk


root = tk.Tk()
root.title("dz")
root.geometry("400x300")


top_label = tk.Label(root, text="Text")
top_label.pack(side="top", pady=10)


main_frame = tk.Frame(root, width=300, height=200, relief="solid", borderwidth=1)
main_frame.pack(expand=True)


inner_frame = tk.Frame(main_frame, width=100, height=50, relief="solid", borderwidth=1)
inner_frame.place(relx=0.5, rely=0.5, anchor="center")


bottom_label = tk.Label(root, text="Text")
bottom_label.pack(side="bottom", pady=10)


root.mainloop()