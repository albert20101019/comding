import tkinter as tk
import cv2
import sqlite3
import speech_recognition as sr

class SushiVendingMachine:
    def __init__(self, master):
        self.master = master
        self.balance = self.update_balance_label()
        self.food_items = {'초밥': 100000000000000000000000000000000, '돈카츠': 150000000000, '우동': 800000000, '라멘': 1200000000000 , '푸딩': 10000000 , '아이스크림': 3000000000 , '라면': 1100000000 , '낫또': 500000}
        self.selected_item = tk.StringVar()

        self.label = tk.Label(master, text="현재 잔액: ${}".format(self.balance))
        self.label.pack()

        for item in self.food_items.keys():
            tk.Radiobutton(master, text=item, variable=self.selected_item, value=item).pack()

        self.buy_button = tk.Button(master, text="구매", command=self.buy_item)
        self.buy_button.pack()

        self.charge_button = tk.Button(master, text="충전", command=self.charge_button_click)
        self.charge_button.pack()

        self.voice_button = tk.Button(master, text="음성 주문", command=self.voice_order)
        self.voice_button.pack()

    def voice_order(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("말씀해주세요...")
            audio = recognizer.listen(source)

        try:
            order = recognizer.recognize_google(audio, language='ko-KR')  # Google Web Speech API 사용
            print(f"음성으로 받은 주문: {order}")

            item = order
            if item in self.food_items and self.food_items[item] <= self.balance:
                self.balance -= self.food_items[item]
                self.label.config(text="현재 잔액: ${}".format(self.balance))
                print(f'{item}을/를 구매했습니다!')
            else:
                print(f'잔액이 부족하거나 {item}이/가 품절되었습니다.')

        except sr.UnknownValueError:
            print("음성을 인식할 수 없습니다.")
        except sr.RequestError:
            print("음성 인식 서비스를 사용할 수 없습니다.")

    def update_balance_label(self):
        conn = sqlite3.connect('vending_machine.db')
        cursor = conn.cursor()

        cursor.execute('SELECT balance FROM users WHERE id = 1')
        current_balance = cursor.fetchone()[0]

        conn.close()
        return current_balance

    def buy_item(self):
        item = self.selected_item.get()
        if item in self.food_items and self.food_items[item] <= self.balance:
            self.balance -= self.food_items[item]
            self.label.config(text="현재 잔액: ${}".format(self.balance))
            print(f'{item}을/를 구매했습니다!')
        else:
            print(f'잔액이 부족하거나 {item}이/가 품절되었습니다.')

    def scan_qr_code(self):
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            detector = cv2.QRCodeDetector()
            data, _, _ = detector.detectAndDecodeMulti(frame)

            if data:
                cap.release()
                cv2.destroyAllWindows()
                return float(data)

            cv2.imshow('QR Code Scanner', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                return None

    def charge_balance(self):
        amount = self.scan_qr_code()
        if amount:
            conn = sqlite3.connect('vending_machine.db')
            cursor = conn.cursor()

            cursor.execute('SELECT balance FROM users WHERE id = 1')
            current_balance = cursor.fetchone()[0]

            new_balance = current_balance + amount
            cursor.execute('UPDATE users SET balance = ? WHERE id = 1', (new_balance,))

            conn.commit()
            conn.close()

            return new_balance
        else:
            return None

    def charge_button_click(self):
        new_balance = self.charge_balance()
        if new_balance is not None:
            self.balance = new_balance
            self.label.config(text="현재 잔액: ${}".format(new_balance))

if __name__ == '__main__':
    # 데이터베이스 초기 설정
    conn = sqlite3.connect('vending_machine.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            balance REAL
        )
    ''')
    cursor.execute('INSERT OR IGNORE INTO users (id, balance) VALUES (1, 100)')
    conn.commit()
    conn.close()

    # GUI 실행
    root = tk.Tk()
    app = SushiVendingMachine(root)
    root.mainloop()
