import tkinter as tk
from tkinter import colorchooser, ttk, filedialog
from PIL import Image, ImageDraw, ImageGrab
import sys

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("간단한 그림판")

        self.canvas = tk.Canvas(root, width=800, height=600, bg='white')
        self.canvas.pack()

        self.color = 'black'
        self.colors = ['black', 'red', 'blue', 'green']
        self.current_color = tk.StringVar(value=self.colors[0])

        self.color_menu = ttk.OptionMenu(root, self.current_color, *self.colors, command=self.change_color)
        self.color_menu.pack(pady=10)

        self.size_slider = ttk.Scale(root, from_=1, to=10, orient='horizontal', command=self.change_size)
        self.size_slider.pack(pady=10)

        self.clear_button = ttk.Button(root, text="초기화", command=self.clear_canvas)
        self.clear_button.pack(pady=10)

        self.save_button = ttk.Button(root, text="저장", command=self.save_image)
        self.save_button.pack(pady=10)

        self.color_chooser_button = ttk.Button(root, text="색 선택", command=self.open_color_chooser)
        self.color_chooser_button.pack(pady=10)

        self.canvas.bind("<B1-Motion>", self.paint)

    def change_color(self, event):
        self.color = self.current_color.get()

    def change_size(self, event):
        self.size = int(self.size_slider.get())

    def paint(self, event):
        x1, y1 = (event.x - self.size), (event.y - self.size)
        x2, y2 = (event.x + self.size), (event.y + self.size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def clear_canvas(self):
        self.canvas.delete("all")

    def save_image(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG files", "*.png")])
            if file_path:
                x = self.root.winfo_rootx() + self.canvas.winfo_x()
                y = self.root.winfo_rooty() + self.canvas.winfo_y()
                x1 = x + self.canvas.winfo_width()
                y1 = y + self.canvas.winfo_height()
                ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)
                print(f"이미지가 {file_path}에 저장되었습니다.")
        except Exception as e:
            print(f"에러 발생: {e}")

    def open_color_chooser(self):
        color = colorchooser.askcolor(initialcolor=self.color)
        if color:
            self.color = color[1]

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
