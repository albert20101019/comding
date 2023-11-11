import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk


def generate_qr_code():
    global qr_image, qr_photo
    url = entry.get()
    if url:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_photo = ImageTk.PhotoImage(qr_image)
        qr_label.config(image=qr_photo)
        qr_label.image = qr_photo

        result_label.config(text="QR 코드 생성이 완료되었습니다.")
    else:
        messagebox.showwarning("URL 입력 필요", "URL을 입력해주세요.")


def save_qr_code():
    if 'qr_image' in globals():
        qr_image.save("qrcode.png")
        messagebox.showinfo("저장 완료", "QR 코드가 저장되었습니다.")
    else:
        messagebox.showwarning("저장할 QR 코드 없음", "먼저 QR 코드를 생성해주세요.")


# GUI 생성
root = tk.Tk()
root.title("QR 코드 생성기")

label = tk.Label(root, text="링크를 입력하세요:")
label.pack()

entry = tk.Entry(root, width=30)
entry.pack()

generate_button = tk.Button(root, text="QR 코드 생성", command=generate_qr_code)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

qr_label = tk.Label(root)
qr_label.pack()

save_button = tk.Button(root, text="저장", command=save_qr_code)
save_button.pack()

root.mainloop()
