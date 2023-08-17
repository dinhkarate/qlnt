<<<<<<< HEAD
import tkinter as tk
from tkinter import messagebox
#from tkcalendar import DateEntry

class InputWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Nhập thông tin khách hàng")

        self.label_first = tk.Label(self, text="Tên:")
        self.label_first.pack()
        self.entry_first = tk.Entry(self)
        self.entry_first.pack()

        self.label_last = tk.Label(self, text="Họ:")
        self.label_last.pack()
        self.entry_last = tk.Entry(self)
        self.entry_last.pack()

        self.label_cccd = tk.Label(self, text="CCCD:")
        self.label_cccd.pack()
        self.entry_cccd = tk.Entry(self)
        self.entry_cccd.pack()

        self.label_sdt = tk.Label(self, text="Số điện thoại:")
        self.label_sdt.pack()
        self.entry_sdt = tk.Entry(self)
        self.entry_sdt.pack()

        # Thêm lịch ngày tháng cho BirthDay
        # self.label_birthday = tk.Label(self, text="Ngày sinh:")
        # self.label_birthday.pack()
        # self.entry_birthday = DateEntry(self, date_pattern='dd/mm/yyyy')
        # self.entry_birthday.pack()
        # Để dành có khi còn dùng
        
        self.btn_confirm = tk.Button(self, text="Xác nhận", command=self.on_confirm)
        self.btn_confirm.pack()

    def on_confirm(self):
        first = self.entry_first.get()
        last = self.entry_last.get()
        cccd = self.entry_cccd.get()
        sdt = self.entry_sdt.get()

        print(khach_hang)
        self.destroy()
=======
import tkinter as tk
from tkinter import messagebox
#from tkcalendar import DateEntry

class InputWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Nhập thông tin khách hàng")

        self.label_first = tk.Label(self, text="Tên:")
        self.label_first.pack()
        self.entry_first = tk.Entry(self)
        self.entry_first.pack()

        self.label_last = tk.Label(self, text="Họ:")
        self.label_last.pack()
        self.entry_last = tk.Entry(self)
        self.entry_last.pack()

        self.label_cccd = tk.Label(self, text="CCCD:")
        self.label_cccd.pack()
        self.entry_cccd = tk.Entry(self)
        self.entry_cccd.pack()

        self.label_sdt = tk.Label(self, text="Số điện thoại:")
        self.label_sdt.pack()
        self.entry_sdt = tk.Entry(self)
        self.entry_sdt.pack()

        # Thêm lịch ngày tháng cho BirthDay
        # self.label_birthday = tk.Label(self, text="Ngày sinh:")
        # self.label_birthday.pack()
        # self.entry_birthday = DateEntry(self, date_pattern='dd/mm/yyyy')
        # self.entry_birthday.pack()
        # Để dành có khi còn dùng
        
        self.btn_confirm = tk.Button(self, text="Xác nhận", command=self.on_confirm)
        self.btn_confirm.pack()

    def on_confirm(self):
        first = self.entry_first.get()
        last = self.entry_last.get()
        cccd = self.entry_cccd.get()
        sdt = self.entry_sdt.get()

        print(khach_hang)
        self.destroy()
>>>>>>> 2980f569ef0d68128605192c6fa4df3f5808ad73
