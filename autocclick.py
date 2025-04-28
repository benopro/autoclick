import pyautogui
import threading
import time
import tkinter as tk
from tkinter import messagebox
import keyboard  # Thư viện mới thêm để bắt phím

running = False  # Biến trạng thái

def start_clicking():
    global running
    running = True

    def click_loop():
        try:
            while running:
                pyautogui.click()
                time.sleep(float(entry.get()))
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    threading.Thread(target=click_loop).start()

def stop_clicking():
    global running
    running = False

def listen_for_esc():
    while True:
        keyboard.wait('esc')
        stop_clicking()
        messagebox.showinfo("Thông báo", "Đã dừng auto click bằng ESC")

def on_close():
    stop_clicking()
    window.destroy()

# Tạo giao diện
window = tk.Tk()
window.title("Auto Clicker")
window.geometry("300x180")

label = tk.Label(window, text="Thời gian giữa 2 lần click (giây):")
label.pack(pady=5)

entry = tk.Entry(window)
entry.insert(0, "0.5")  # mặc định 0.5s
entry.pack(pady=5)

start_button = tk.Button(window, text="Bắt đầu", command=start_clicking)
start_button.pack(pady=5)

stop_button = tk.Button(window, text="Dừng lại", command=stop_clicking)
stop_button.pack(pady=5)

exit_label = tk.Label(window, text="(Ấn ESC để dừng nhanh)", fg="red")
exit_label.pack(pady=5)

window.protocol("WM_DELETE_WINDOW", on_close)

# Tạo luồng mới để lắng nghe phím ESC
threading.Thread(target=listen_for_esc, daemon=True).start()

window.mainloop()
