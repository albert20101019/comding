import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def crawl_naver_shopping():
    search_query = entry.get()
    driver = webdriver.Chrome(ChromeDriverManager().install())

    try:
        driver.get("https://shopping.naver.com/")
        search_box = driver.find_element(By.CSS_SELECTOR, "input[id='query']")
        search_box.send_keys(search_query)
        search_box.submit()

        time.sleep(4)  # 페이지가 로딩될 때까지 대기

        product_names = driver.find_elements(By.CSS_SELECTOR, "div.basicList_title__3P9Q7 > a")
        prices = driver.find_elements(By.CSS_SELECTOR, "span.price_num__2WUXn")
        reviews = driver.find_elements(By.CSS_SELECTOR, "a.basicList_detail__27Krk")

        result_text.delete(1.0, tk.END)  # 이전 결과 지우기

        for name, price, review in zip(product_names, prices, reviews):
            result_text.insert(tk.END, f"상품명: {name.text}, 가격: {price.text}, 리뷰수: {review.text}\n")
    finally:
        driver.quit()

# GUI 생성
root = tk.Tk()
root.title("네이버 쇼핑 검색")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label = ttk.Label(frame, text="검색어:")
label.grid(row=0, column=0)

entry = ttk.Entry(frame, width=30)
entry.grid(row=0, column=1)

search_button = ttk.Button(frame, text="검색", command=crawl_naver_shopping)
search_button.grid(row=0, column=2)

result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()
