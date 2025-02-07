import multiprocessing
import os
import tkinter as tk
from tkinter import messagebox

def run_file(file):
    """Chạy file Python bằng os.system"""
    print(f"Đang chạy {file}...")
    os.system(f"python {file}")

def run_lay_anh():
    """Chạy chương trình lấy ảnh trước"""
    print("Bắt đầu lấy ảnh...")
    os.system("python lay_anh.py")
    print("Lấy ảnh xong!")

    # Sau khi lấy ảnh xong, mở giao diện lựa chọn
    open_gui()

def open_gui():
    """Hiển thị giao diện lựa chọn"""
    root = tk.Tk()
    root.title("Giao diện chính")
    root.geometry("300x200")

    tk.Label(root, text="Chọn chế độ:", font=("Arial", 12)).pack(pady=10)

    def run_di_anh():
        messagebox.showinfo("Thông báo", "Đang chạy nhận diện...")
        root.destroy()
        run_file("di_anh.py")

    def run_zoom():
        messagebox.showinfo("Thông báo", "Đang chạy chế độ zoom...")
        root.destroy()
        run_file("zoom.py")

    tk.Button(root, text="Nhận diện vật thể", command=run_di_anh, width=20).pack(pady=5)
    tk.Button(root, text="Zoom vật thể", command=run_zoom, width=20).pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    # Chạy lấy ảnh trước
    run_lay_anh()
