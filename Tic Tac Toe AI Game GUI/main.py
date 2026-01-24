# ============================================================
# TIC TAC TOE AI GAME
# ------------------------------------------------------------
# Modes:
# Easy        AI plays randomly
# Hard        AI thinks only 1 move ahead (win or block)
# Unbeatable  AI uses Minimax (perfect play, never loses)
#
# Player  = X (Blue)
# AI      = O (Red)
# ============================================================

import tkinter as tk
from tkinter import messagebox
import random

# ---------------- GAME STATE ----------------

# Board layout:
# [0][1][2]
# [3][4][5]
# [6][7][8]
board = [""] * 9

# Current difficulty mode
current_mode = "Easy"

# Score for each mode (Player vs AI)
scores = {
    "Easy": {"Player": 0, "AI": 0},
    "Hard": {"Player": 0, "AI": 0},
    "Unbeatable": {"Player": 0, "AI": 0}
}

# ---------------- BASIC HELPERS ----------------

def get_empty_positions(current_board):
    """Return all empty positions from the board."""
    return [index for index, value in enumerate(current_board) if value == ""]


def check_game_result(current_board):
    """Check if Player (X), AI (O) has won, or if it is a DRAW."""
    winning_patterns = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),   # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),   # Columns
        (0, 4, 8), (2, 4, 6)               # Diagonals
    ]

    for first, second, third in winning_patterns:
        if (current_board[first] == current_board[second] ==
            current_board[third] != ""):
            return current_board[first]   # "X" or "O"

    if "" not in current_board:
        return "DRAW"

    return None


# ---------------- UNBEATABLE AI (MINIMAX) ----------------
# This AI looks at ALL future possibilities.
# It always chooses:
# - A winning path if possible
# - Otherwise a guaranteed draw

def minimax(current_board, is_ai_turn, depth):
    game_result = check_game_result(current_board)

    if game_result == "O":      # AI wins
        return 10 - depth
    elif game_result == "X":    # Player wins
        return depth - 10
    elif game_result == "DRAW":
        return 0

    if is_ai_turn:
        best_score = -1000
        for position in get_empty_positions(current_board):
            current_board[position] = "O"
            score = minimax(current_board, False, depth + 1)
            current_board[position] = ""
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = 1000
        for position in get_empty_positions(current_board):
            current_board[position] = "X"
            score = minimax(current_board, True, depth + 1)
            current_board[position] = ""
            best_score = min(best_score, score)
        return best_score


def get_unbeatable_ai_move():
    """Find the best possible move using full Minimax."""
    best_score = -1000
    best_position = None

    for position in get_empty_positions(board):
        board[position] = "O"
        score = minimax(board, False, 0)
        board[position] = ""

        if score > best_score:
            best_score = score
            best_position = position

    return best_position

# ---------------- HARD MODE AI ----------------
# Thinks only one step ahead:
# 1. Can AI win now?
# 2. Can Player win next? Block it.
# 3. Otherwise choose random.

def get_hard_ai_move():
    # 1. Check if AI can win immediately
    for position in get_empty_positions(board):
        board[position] = "O"
        if check_game_result(board) == "O":
            board[position] = ""
            return position
        board[position] = ""

    # 2. Check if Player can win next turn and block it
    for position in get_empty_positions(board):
        board[position] = "X"
        if check_game_result(board) == "X":
            board[position] = ""
            return position
        board[position] = ""

    # 3. Otherwise, random move
    return random.choice(get_empty_positions(board))

# ---------------- EASY MODE AI ----------------
# Plays completely randomly (no thinking)

def get_easy_ai_move():
    return random.choice(get_empty_positions(board))

# ---------------- AI MOVE ----------------

def ai_move():
    if current_mode == "Easy":
        chosen_position = get_easy_ai_move()
    elif current_mode == "Hard":
        chosen_position = get_hard_ai_move()
    else:  # Unbeatable
        chosen_position = get_unbeatable_ai_move()

    board[chosen_position] = "O"
    buttons[chosen_position]["text"] = "O"
    buttons[chosen_position]["bg"] = "#ff7675"  # Red for AI
    check_game()

# ---------------- PLAYER MOVE ----------------

def player_move(position):
    if board[position] == "":
        board[position] = "X"
        buttons[position]["text"] = "X"
        buttons[position]["bg"] = "#74b9ff"  # Blue for Player

        if not check_game():
            root.after(300, ai_move)

# ---------------- GAME RESULT HANDLING ----------------

def check_game():
    game_result = check_game_result(board)

    if game_result:
        if game_result == "DRAW":
            message_text = "It's a Draw!"
        else:
            message_text = f"{game_result} Wins!"

            if game_result == "X":
                scores[current_mode]["Player"] += 1
            else:
                scores[current_mode]["AI"] += 1

            update_scoreboard()

        user_choice = messagebox.askyesno(
            "Game Over",
            f"{message_text}\n\nMode: {current_mode}\n\nPlay Again?"
        )

        if user_choice:
            reset_board()
        else:
            root.destroy()

        return True

    return False

# ---------------- RESET BOARD ----------------

def reset_board():
    global board
    board = [""] * 9
    for button in buttons:
        button["text"] = ""
        button["bg"] = "#2d3436"

# ---------------- MODE SWITCH ----------------

def set_mode(selected_mode):
    global current_mode
    current_mode = selected_mode
    mode_label.config(text=f"Mode: {selected_mode}")
    reset_board()

# ---------------- SCOREBOARD ----------------

def update_scoreboard():
    score_label.config(
        text=(
            f"  🧑‍💻:{scores['Easy']['Player']}  🤖:{scores['Easy']['AI']}   |   "
            f"  🧑‍💻:{scores['Hard']['Player']}  🤖:{scores['Hard']['AI']}   |   "
            f"  🧑‍💻:{scores['Unbeatable']['Player']}  🤖:{scores['Unbeatable']['AI']}"
        )
    )

# ---------------- GUI SETUP ----------------

root = tk.Tk()
root.title("Tic Tac Toe AI")
root.configure(bg="#1e272e")

# Title
title_label = tk.Label(
    root,
    text="TIC TAC TOE AI",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#1e272e"
)
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Mode label
mode_label = tk.Label(
    root,
    text="Mode: Easy",
    font=("Arial", 12),
    fg="yellow",
    bg="#1e272e"
)
mode_label.grid(row=1, column=0, columnspan=3)
# Scoreboard
score_label = tk.Label(
    root,
    text="🧑‍💻:0  🤖:0   |   🧑‍💻:0  🤖:0   |    🧑‍💻:0  🤖:0",
    font=("Segoe UI Emoji", 12),
    fg="lightgreen",
    bg="#1e272e"
)
score_label.grid(row=2, column=0, columnspan=3, pady=5)

# Mode buttons
mode_button_frame = tk.Frame(root, bg="#1e272e")
mode_button_frame.grid(row=3, column=0, columnspan=3, pady=5)

tk.Button(
    mode_button_frame, text="Easy", width=10, bg="#00b894",
    command=lambda: set_mode("Easy")
).grid(row=0, column=0, padx=5)

tk.Button(
    mode_button_frame, text="Hard", width=10, bg="#fdcb6e",
    command=lambda: set_mode("Hard")
).grid(row=0, column=1, padx=5)

tk.Button(
    mode_button_frame, text="Unbeatable", width=10, bg="#d63031", fg="white",
    command=lambda: set_mode("Unbeatable")
).grid(row=0, column=2, padx=5)

# Game board buttons
buttons = []
for position in range(9):
    button = tk.Button(
        root,
        text="",
        font=("Arial", 28, "bold"),
        width=4,
        height=2,
        bg="#2d3436",
        fg="white",
        command=lambda pos=position: player_move(pos)
    )
    button.grid(row=(position // 3) + 4, column=position % 3, padx=5, pady=5)
    buttons.append(button)

root.mainloop()