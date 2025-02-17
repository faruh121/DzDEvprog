import tkinter as tk
from tkinter import Canvas, PhotoImage

def exit_app():
    root.destroy()


root = tk.Tk()
root.title("Faruh")  
root.geometry("500x500")  
root.resizable(False, False)  


try:
    root.iconbitmap("icon.ico")
except:
    print("Иконка не найдена, используйте существующую или проверьте путь")


label1 = tk.Label(root, text="Добро пожаловать в крутую программу!", font=("Arial", 14))
label1.pack(pady=10)


label2 = tk.Label(root, text="Автор: Юсупов Фарух рпо3/23", font=("Arial", 12))
label2.pack(pady=5)

canvas = Canvas(root, width=500, height=375)
canvas.pack(pady=10)

try:
    img = PhotoImage(file="images.jpg")
    canvas.create_image(60, 0, anchor=tk.NW, image=img)
except:
    print("Изображение не найдено, проверьте путь")


exit_button = tk.Button(root, text="Выход", command=exit_app, font=("Arial", 12), bg="lightgray")
exit_button.pack(side="bottom", pady=20)


root.mainloop()