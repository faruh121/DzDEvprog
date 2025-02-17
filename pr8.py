import tkinter as tk
import random

# Настройки окна
WIDTH, HEIGHT = 500, 400
SHIP_SPEED = 10
COMET_SPEED = 5

class SpaceGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Космическая игра")
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        
        # Создание холста
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        # Генерация звезд
        self.create_stars()

        # Добавление космолета
        self.ship = self.canvas.create_oval(220, 300, 280, 360, fill="blue")

        # Добавление кометы
        self.comet = self.canvas.create_oval(100, 50, 130, 80, fill="red")

        # Движение объектов
        self.move_ship()
        self.move_comet()

    # Функция генерации звезд
    def create_stars(self):
        for _ in range(50):
            x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            self.canvas.create_oval(x, y, x+2, y+2, fill="white")

    # Функция движения космолета
    def move_ship(self):
        dx, dy = random.choice([-SHIP_SPEED, SHIP_SPEED]), random.choice([-SHIP_SPEED, SHIP_SPEED])
        x1, y1, x2, y2 = self.canvas.coords(self.ship)

        # Проверяем границы
        if x1 + dx < 0 or x2 + dx > WIDTH:
            dx = -dx
        if y1 + dy < 0 or y2 + dy > HEIGHT:
            dy = -dy

        self.canvas.move(self.ship, dx, dy)
        self.root.after(200, self.move_ship)

    # Функция движения кометы
    def move_comet(self):
        dx, dy = random.choice([-COMET_SPEED, COMET_SPEED]), random.choice([-COMET_SPEED, COMET_SPEED])
        x1, y1, x2, y2 = self.canvas.coords(self.comet)

        # Проверяем границы
        if x1 + dx < 0 or x2 + dx > WIDTH:
            dx = -dx
        if y1 + dy < 0 or y2 + dy > HEIGHT:
            dy = -dy

        self.canvas.move(self.comet, dx, dy)
        self.root.after(150, self.move_comet)

# Запуск игры
root = tk.Tk()
game = SpaceGame(root)
root.mainloop()