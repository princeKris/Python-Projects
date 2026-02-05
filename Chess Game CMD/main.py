import os
import time

# unicode chess pieces
# uppercase -> black | lowercase -> white
PIECES = {
    "K": "\u265A", "Q": "\u265B", "R": "\u265C",
    "B": "\u265D", "N": "\u265E", "P": "\u265F",

    "k": "\u2654", "q": "\u2655", "r": "\u2656",
    "b": "\u2657", "n": "\u2658", "p": "\u2659",

    ".": "."
}

# clear terminal
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# starting board
def create_board():
    return [
        list("rnbqkbnr"),
        list("pppppppp"),
        list("........"),
        list("........"),
        list("........"),
        list("........"),
        list("PPPPPPPP"),
        list("RNBQKBNR")
    ]

# print board
def print_board(board):
    print("  a b c d e f g h")
    for i, row in enumerate(board):
        print(8 - i, end=" ")
        for cell in row:
            print(PIECES[cell], end=" ")
        print(8 - i)
    print("  a b c d e f g h")

# parse input like e2 e4
def parse_move(move):
    s, e = move.split()
    sr = 8 - int(s[1])
    sc = ord(s[0]) - 97
    er = 8 - int(e[1])
    ec = ord(e[0]) - 97
    return sr, sc, er, ec

# move piece (no rules)
def move_piece(board, sr, sc, er, ec):
    board[er][ec] = board[sr][sc]
    board[sr][sc] = "."

# game loop
def play():
    board = create_board()
    turn = "White"

    while True:
        clear_screen()
        print_board(board)
        print(f"\n{turn}'s move (e2 e4)")
        print("type 'exit' to quit")

        move = input(">> ").strip().lower()
        if move == "exit":
            clear_screen()
            print("game ended ")
            break

        try:
            sr, sc, er, ec = parse_move(move)
            move_piece(board, sr, sc, er, ec)
            turn = "Black" if turn == "White" else "White"
        except:
            print("invalid move format")
            time.sleep(1.2)

# start game
if __name__ == "__main__":
    play()