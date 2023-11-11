import tkinter as tk
from datetime import datetime, timedelta


class Stopwatch:
    def __init__(self, master):
        self.master = master
        self.running = False
        self.start_time = None
        self.records = []

        self.time_display = tk.Label(master, text="00:00:00.000", font=("Helvetica", 36))
        self.time_display.pack(pady=20)

        self.start_button = tk.Button(master, text="Start", command=self.start_stop)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.record_button = tk.Button(master, text="Record", command=self.record_time)
        self.record_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.record_display = tk.Listbox(master, width=30, height=10)
        self.record_display.pack(pady=10)

        self.update()

    def start_stop(self):
        self.running = not self.running
        if self.running:
            self.start_button.config(text="Stop")
            self.record_button.config(state="normal")
            if not self.start_time:
                self.start_time = datetime.now()
            self.update()
        else:
            self.start_button.config(text="Start")
            self.record_button.config(state="disabled")
            self.update()

    def record_time(self):
        if self.running:
            elapsed_time = datetime.now() - self.start_time
            time_str = "{:02d}:{:02d}:{:02d}.{:03d}".format(
                elapsed_time.seconds // 3600,
                (elapsed_time.seconds % 3600) // 60,
                elapsed_time.seconds % 60,
                elapsed_time.microseconds // 1000
            )
            self.records.insert(0, time_str)  # 기록을 최신순으로 추가
            self.record_display.delete(0, tk.END)  # 기존 목록 삭제
            for record in self.records:
                self.record_display.insert(tk.END, record)

    def reset(self):
        self.running = False
        self.start_time = None
        self.time_display.config(text="00:00:00.000")
        self.records = []
        self.record_display.delete(0, tk.END)

    def update(self):
        if self.running:
            elapsed_time = datetime.now() - self.start_time
            time_str = "{:02d}:{:02d}:{:02d}.{:03d}".format(
                elapsed_time.seconds // 3600,
                (elapsed_time.seconds % 3600) // 60,
                elapsed_time.seconds % 60,
                elapsed_time.microseconds // 1000
            )
            self.time_display.config(text=time_str)
        self.master.after(1, self.update)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("스톱워치")
    stopwatch = Stopwatch(root)
    root.mainloop()
