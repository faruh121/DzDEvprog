import tkinter as tk

light_bg = "#f0f0f0"
light_text = "#000000"
dark_bg = "#2e2e2e"
dark_text = "#ffffff"

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Окно входа")
        self.root.geometry("300x200")
        self.root.configure(bg=light_bg)
        

        self.dark_mode = tk.IntVar(value=0)


        tk.Label(root, text="Логин:", bg=light_bg, fg=light_text).pack(pady=5)
        self.entry_login = tk.Entry(root)
        self.entry_login.pack()

        tk.Label(root, text="Пароль:", bg=light_bg, fg=light_text).pack(pady=5)
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack()


        tk.Button(root, text="Вход").pack(pady=5)
        tk.Button(root, text="Настройки", command=self.open_settings).pack()


    def open_settings(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Настройки")
        settings_window.geometry("200x150")
        settings_window.configure(bg=light_bg)

   
        check = tk.Checkbutton(settings_window, text="Темная тема", variable=self.dark_mode,
                               command=self.toggle_theme, bg=light_bg, fg=light_text)
        check.pack(pady=10)

   
        tk.Button(settings_window, text="Назад", command=settings_window.destroy).pack(pady=5)


    def toggle_theme(self):
        if self.dark_mode.get():
            self.root.configure(bg=dark_bg)
            for widget in self.root.winfo_children():
                if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
                    widget.config(bg=dark_bg, fg=dark_text)
        else:
            self.root.configure(bg=light_bg)
            for widget in self.root.winfo_children():
                if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
                    widget.config(bg=light_bg, fg=light_text)


root = tk.Tk()
app = App(root)
root.mainloop()