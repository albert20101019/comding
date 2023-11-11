import tkinter as tk
import random

def create_board(rows, cols, num_mines):
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    mines = random.sample(range(rows*cols), num_mines)
    for mine in mines:
        row = mine // cols
        col = mine % cols
        board[row][col] = -1
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if 0 <= r < rows and 0 <= c < cols and board[r][c] != -1:
                    board[r][c] += 1
    return board

def reveal(board, revealed, row, col):
    if revealed[row][col] or board[row][col] == -1:
        return
    revealed[row][col] = True
    if board[row][col] == 0:
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if 0 <= r < len(board) and 0 <= c < len(board[0]):
                    reveal(board, revealed, r, c)

def toggle_flag(i, j):
    if not revealed[i][j]:
        if flags[i][j]:
            buttons[i][j].config(text='')
            flags[i][j] = False
        else:
            buttons[i][j].config(text='F')
            flags[i][j] = True

def update_buttons():
    for i in range(rows):
        for j in range(cols):
            if revealed[i][j]:
                buttons[i][j].config(text=str(board[i][j]))
                buttons[i][j].config(state='disabled', relief='sunken')
            else:
                buttons[i][j].config(state='normal', relief='raised')

def check_win():
    for i in range(rows):
        for j in range(cols):
            if board[i][j] != -1 and not revealed[i][j]:
                return False
    return True

def click_button(i, j):
    if board[i][j] == -1:
        buttons[i][j].config(text='X', relief='sunken')
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == -1:
                    buttons[r][c].config(text='X')
        label.config(text='지뢰를 밟았습니다! 게임 종료.')
        new_game_button.grid(row=0, column=cols, columnspan=2)
    elif board[i][j] == 0:
        reveal(board, revealed, i, j)
        update_buttons()
        if check_win():
            label.config(text=f'지뢰를 모두 찾았습니다! 총 {num_mines}개의 지뢰가 있습니다. 게임 종료.')
            new_game_button.grid(row=0, column=cols, columnspan=2)
    else:
        buttons[i][j].config(text=str(board[i][j]))
        buttons[i][j].config(state='disabled', relief='sunken')
        if check_win():
            label.config(text=f'지뢰를 모두 찾았습니다! 총 {num_mines}개의 지뢰가 있습니다. 게임 종료.')
            new_game_button.grid(row=0, column=cols, columnspan=2)

def create_buttons():
    buttons = []
    for i in range(rows):
        row_buttons = []
        for j in range(cols):
            btn = tk.Button(frame, width=4, height=2, command=lambda i=i, j=j: click_button(i, j))
            btn.grid(row=i, column=j)
            btn.bind('<Button-3>', lambda event, i=i, j=j: toggle_flag(i, j))
            row_buttons.append(btn)
        buttons.append(row_buttons)
    return buttons


def play_game():
    global board, revealed, flags, rows, cols, num_mines
    num_mines = random.randint(1, rows * cols // 4)  # 랜덤하게 지뢰 개수 생성
    board = create_board(rows, cols, num_mines)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]
    flags = [[False for _ in range(cols)] for _ in range(rows)]
    global buttons
    buttons = create_buttons()

    # 전체 지뢰 개수 알림 추가
    total_mines_label.config(text=f"전체 지뢰 개수: {num_mines}")

    new_game_button.grid_forget()  # 새 게임 버튼 숨기기

    window.mainloop()


def start_new_game():
    new_game_button.grid_forget()  # 새 게임 버튼 숨기기
    play_game()

# 메인 창 생성
window = tk.Tk()
window.title('지뢰찾기')

# 게임 설정 입력 받기
rows = random.randint(5, 10)  # 랜덤하게 행 수 생성
cols = random.randint(5, 10)  # 랜덤하게 열 수 생성

# 게임 시작 버튼 생성
frame = tk.Frame(window)
frame.grid(row=0, column=0, padx=10, pady=10)
start_button = tk.Button(frame, text='게임 시작', command=play_game)
start_button.grid(row=0, column=0, columnspan=cols)

# 결과 표시 레이블 생성
label = tk.Label(window, text='')
label.grid(row=1, column=0, pady=(0, 10))

# 전체 지뢰 개수 표시 레이블 생성
total_mines_label = tk.Label(window, text='')
total_mines_label.grid(row=2, column=0)

# 새 게임 시작 버튼 생성
new_game_button = tk.Button(frame, text='새 게임 시작', command=start_new_game)

window.mainloop()

