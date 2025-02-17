
import tkinter as tk
from tkinter import messagebox
import random

class RPGGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Пошаговая Ролевая Игра")
        self.root.geometry("400x300")
        self.money = 500
        self.has_key = False
        self.current_window = None
        self.start_screen()

    # Функция для обновления окна
    def update_window(self, new_window_func):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = tk.Frame(self.root)
        self.current_window.pack(fill="both", expand=True)
        new_window_func()

    # Стартовая локация
    def start_screen(self):
        self.update_window(self.start_screen_content)

    def start_screen_content(self):
        tk.Label(self.current_window, text="Добро пожаловать в игру!", font=("Arial", 14)).pack(pady=20)
        tk.Button(self.current_window, text="Начать игру", command=self.fork_location).pack(pady=10)

    # Развилка с выбором локаций
    def fork_location(self):
        self.update_window(self.fork_location_content)

    def fork_location_content(self):
        tk.Label(self.current_window, text="Выберите путь:", font=("Arial", 12)).pack(pady=10)
        tk.Button(self.current_window, text="Замок", command=self.castle_location).pack(pady=5)
        tk.Button(self.current_window, text="Магазин", command=self.shop_location).pack(pady=5)
        tk.Button(self.current_window, text="Заработок", command=self.work_location).pack(pady=5)

    # Локация замка
    def castle_location(self):
        self.update_window(self.castle_location_content)

    def castle_location_content(self):
        tk.Label(self.current_window, text="Вы у ворот замка!", font=("Arial", 12)).pack(pady=10)

        if self.has_key:
            messagebox.showinfo("Победа!", "Вы открыли дверь золотым ключом и выиграли!")
            self.root.quit()
        else:
            tk.Button(self.current_window, text="Попытаться взломать", command=self.try_break_in).pack(pady=5)
            tk.Button(self.current_window, text="Назад", command=self.fork_location).pack(pady=5)

    def try_break_in(self):
        if random.randint(0, 1) == 0:
            messagebox.showinfo("Успех!", "Вы взломали дверь и победили!")
            self.root.quit()
        else:
            messagebox.showerror("Поражение!", "Охрана вас поймала, и вы проиграли!")
            self.restart_game()

    # Магазин (покупка ключа)
    def shop_location(self):
        self.update_window(self.shop_location_content)

    def shop_location_content(self):
        tk.Label(self.current_window, text="Магазин", font=("Arial", 12)).pack(pady=10)
        tk.Label(self.current_window, text=f"Ваши деньги: {self.money} монет").pack()

        if self.money >= 1000 and not self.has_key:
            tk.Button(self.current_window, text="Купить золотой ключ (1000 монет)", command=self.buy_key).pack(pady=5)
        elif self.has_key:
            tk.Label(self.current_window, text="Вы уже купили ключ.").pack()

        tk.Button(self.current_window, text="Назад", command=self.fork_location).pack(pady=5)

    def buy_key(self):
        self.money -= 1000
        self.has_key = True
        messagebox.showinfo("Покупка", "Вы купили золотой ключ!")
        self.fork_location()


    def work_location(self):
        self.update_window(self.work_location_content)

    def work_location_content(self):
        tk.Label(self.current_window, text="Заработок", font=("Arial", 12)).pack(pady=10)
        tk.Label(self.current_window, text=f"Ваши деньги: {self.money} монет").pack()
        tk.Label(self.current_window, text="Угадайте число от 0 до 6:").pack()

        self.guess_entry = tk.Entry(self.current_window)
        self.guess_entry.pack()

        tk.Button(self.current_window, text="Проверить", command=self.check_guess).pack(pady=5)
        tk.Button(self.current_window, text="Назад", command=self.fork_location).pack(pady=5)

    def check_guess(self):
        try:
            user_guess = int(self.guess_entry.get())
            if 0 <= user_guess <= 6:
                correct_number = random.randint(0, 6)
                if user_guess == correct_number:
                    self.money *= 2
                    messagebox.showinfo("Успех!", f"Вы угадали! Теперь у вас {self.money} монет.")
                else:
                    self.money -= random.randint(100, 200)
                    messagebox.showwarning("Провал!", f"Вы не угадали. У вас осталось {self.money} монет.")

                if self.money <= 0:
                    messagebox.showerror("Поражение!", "Вы проиграли, у вас нет денег.")
                    self.restart_game()
                else:
                    self.work_location()
            else:
                messagebox.showwarning("Ошибка", "Введите число от 0 до 6!")
        except ValueError:
            messagebox.showwarning("Ошибка", "Введите корректное число!")


    def restart_game(self):
        self.money = 500
        self.has_key = False
        self.start_screen()


if name == "__main__":
    root = tk.Tk()
    game = RPGGame(root)
    root.mainloop()