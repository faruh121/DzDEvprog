import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Крестики-нолики")
root.geometry("300x350")
root.resizable(False, False)


current_player = "X"
board = [""] * 9  


def make_move(index):
    global current_player
    
    if board[index] == "" and not check_winner():
        board[index] = current_player
        buttons[index].config(text=current_player, state="disabled")

        winner = check_winner()
        if winner:
            messagebox.showinfo("Игра окончена", f"Победитель: {winner}")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"


def check_winner():
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)             
    ]

    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]  

    if "" not in board:
        messagebox.showinfo("Игра окончена", "Ничья!")
        reset_game()
        return None

    return None


def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for button in buttons:
        button.config(text="", state="normal")


buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command=lambda i=i: make_move(i))
    btn.grid(row=i // 3, column=i % 3)
    buttons.append(btn)


author_label = tk.Label(root, text="Юсупов Ф, 23/3", font=("Arial", 10))
author_label.grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()