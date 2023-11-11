import tkinter as tk
from tkinter import filedialog
import pygame
import time

bgcolor = "#B2F4E4"
buttoncolor = "#e4b2f4"
buttonfcolor = "#000000"
buttonfonr = ("Helvetica",10)

def playmusic():
    pygame.mixer.init()
    pygame.mixer.music.load(selectedfile)
    pygame.mixer.music.play()
    update_time()

def update_time():
    current = pygame.mixer.music.get_pos() / 1000
    time_label.config(text=f"현제시간:{int(current)} 초")
    root.after(1000,update_time)

def openfile():
    global selectedfile
    selectedfile = filedialog.askopenfilename(
        filetypes=[("MP3 files","*.mp3")]
    )
def openfile():
    global selectedfile
    selectedfile = filedialog.askopenfilename(
        filetypes=[("MP3 files","*.mp3")]
    )
    playmusic()
def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()
    time_label.config(text = "현제 시간 : 0초")

root = tk.Tk()
root.title("mp3 player")
root.geometry("800x100")

selectedfile = ""
root.configure(bg=bgcolor)

play_button = tk.Button(
    root,
    text = "재생",
    command=playmusic,
    font=buttonfonr,
    bg=buttoncolor,
    fg=buttonfcolor,
    padx=20,
    pady = 10
)
play_button.pack(side=tk.LEFT, padx = 10)

pause_button = tk.Button(
    root,
    text = "멈춤",
    command=pause_music,
    font=buttonfonr,
    bg=buttoncolor,
    fg=buttonfcolor,
    padx=20,
    pady = 10
)
pause_button.pack(side=tk.LEFT, padx = 10)

unpause_button = tk.Button(
    root,
    text = "재재생",
    command=unpause_music,
    font=buttonfonr,
    bg=buttoncolor,
    fg=buttonfcolor,
    padx=20,
    pady = 10
)
unpause_button.pack(side=tk.LEFT, padx = 10)

time_label = tk.Label(
    root,
    text="현제시간0초",
    font=buttonfonr,
    bg=bgcolor,
)
time_label.pack(side=tk.LEFT, padx=10)

open_button = tk.Button(
    root,
    text = "파일열기",
    command=openfile,
    font = buttonfonr,
    bg=buttoncolor,
    fg=buttonfcolor,
    padx = 20,
    pady = 10
)
open_button.pack(side=tk.RIGHT,padx=10)

quit_button = tk.Button(
    root,
    text = "종료",
    command=root.destroy,
    font = buttonfonr,
    bg=buttoncolor,
    fg=buttonfcolor,
    padx = 20,
    pady = 10
)
quit_button.pack(side=tk.RIGHT,padx=10)

root.mainloop()