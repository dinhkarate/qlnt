<<<<<<< HEAD
import tkinter as tk
from tkinter import messagebox, ttk, font
from tkinter import *
from dateutil.parser import parse
import datetime

from add_window_khachhang import InputWindow
#from treeview import treeview, giadien, gianuoc
from app_database_structure import *

def on_configure(event):
    # Configure the canvas scroll region to be the size of the buttons area
    canvas.configure(scrollregion=canvas.bbox("all"))

def red_button(original_button, room_id):
    hoadon = get_hoadon_by_so_phong(room_id)
    found_zero = False
    
    for hoadon_moithang in hoadon:
        if hoadon_moithang[7] == 0:
            original_button.config(bg="red")
            found_zero = True
            break
            
    if not found_zero:
        original_button.config(bg="SystemButtonFace")

def thaydoigia():
    popup = tk.Toplevel(root)
    popup.geometry("300x200")
    popup.title("Thay đổi giá")

    label1 = tk.Label(popup, text="Giá điện:")
    label1.pack(pady=5)
    
    entry1 = tk.Entry(popup)
    entry1.pack(pady=5)
    current_price_id = get_latest_giadiennuoc_id()
    giadiennuoc = select_giadiennuoc_by_id(current_price_id)
    entry1.insert(0, giadiennuoc[1])
    # giadiennuoc = [(id, giadien, gianuoc)]

    # Label và Entry để nhập màu mới cho nền button
    label2 = tk.Label(popup, text="Giá nước:")
    label2.pack(pady=5)
    
    entry2 = tk.Entry(popup)
    entry2.pack(pady=5)
    entry2.insert(0, giadiennuoc[2])

    def xacnhan_button():
        giadien = entry1.get()
        gianuoc = entry2.get()
        insert_giadiennuoc(giadien, gianuoc)
        popup.destroy()

    xacnhan = tk.Button(popup, text="Xác nhận", command=xacnhan_button)
    xacnhan.pack(pady=10)

def add_button():
    global num_buttons_added
    popup = tk.Toplevel(root)
    popup.geometry("300x200")
    popup.title("Thêm phòng")
    
    # Label và Entry để nhập giá trị mới cho tên button
    label1 = tk.Label(popup, text="Mã phòng:")
    label1.pack(pady=5)
    
    entry1 = tk.Entry(popup)
    entry1.pack(pady=5)

    # Label và Entry để nhập màu mới cho nền button
    label2 = tk.Label(popup, text="Tiền thuê:")
    label2.pack(pady=5)
    
    entry2 = tk.Entry(popup)
    entry2.pack(pady=5)
    
    # Button để xác nhận chỉnh sửa và cập nhật tên và màu của button
    def update_button_name_and_color():
        new_name = entry1.get()
        giaphong = entry2.get()

        insert_phong(new_name, giaphong)
        #print(giaphong)
        #new_color = entry2.get()
        #if new_name:
            #button.config(text=f"\n  {new_name}  \n")
        
        #if new_color:
        #    button.config(bg=new_color)

        global button_labels
        new_button_label = f"Button {len(button_labels) + 1}"
        button_labels.append(new_button_label)
        
        btn_id = len(buttons) + 1

        new_button = tk.Button(button_frame, text=new_name + "\n\nTrống", width=10, height=5, command=lambda idx=len(button_labels): edit_button(new_button, idx, giaphong, new_name))
        #new_button.config(command=lambda: edit_button(new_button, giaphong))  # Gán hàm edit_button tương ứng cho nút mới
        # new_button.grid(row=num_buttons_added // 4, column=num_buttons_added % 4, padx=10, pady=10)
        buttons.append(new_button)
        hidden_buttons.append(False)
        visible_buttons = [button for button, hidden in zip(buttons, hidden_buttons) if not hidden]
        for i, button in enumerate(visible_buttons):
            button.grid(row=i // 5, column=i % 5, padx=5, pady=5)

        button_id_dict[new_button] = btn_id
        
        canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

        button_info = button.grid_info()  # Lấy thông tin vị trí
        row = button_info["row"]  # Lấy giá trị của thuộc tính "row"
        column = button_info["column"]  # Lấy giá trị của thuộc tính "column"
        original_positions.append((row, column))  # Thêm vào danh sách
        popup.destroy()

    
    update_button = tk.Button(popup, text="Thêm phòng", command=update_button_name_and_color)
    update_button.pack(pady=10)
    num_buttons_added += 1
    #print(num_buttons_added)
    #print(buttons)
    #print(hidden_buttons)
    #print(button_labels)

def get_btn_id_from_button(button):
    return button_id_dict.get(button, None)

def payment_info(button, sophong):
    treeview(button, sophong)

def get_first_name(full_name):
    # Tách chuỗi nhập thành danh sách các từ
    name_parts = full_name.split()

    # Lấy tên từ phần tử cuối cùng của danh sách
    first_name = name_parts[-1]

    return first_name

def get_last_name(full_name):
    # Tách chuỗi nhập thành danh sách các từ
    name_parts = full_name.split()

    # Lấy họ từ phần tử đầu tiên của danh sách
    last_name = name_parts[0]

    return last_name

def edit_button(button, btn_id, giaphong, sophong):
        popup = tk.Toplevel(root)
        popup.title("Nhập thông tin người thuê")
        
        # Label và Entry để nhập giá trị mới cho tên button
        label1 = tk.Label(popup, text="Họ Tên:")
        label1.pack(pady=5)
        
        entry1 = tk.Entry(popup)
        entry1.pack(pady=5)

        # Label và Entry để nhập màu mới cho nền button
        label2 = tk.Label(popup, text="CCCD:")
        label2.pack(pady=5)
        
        entry2 = tk.Entry(popup)
        entry2.pack(pady=5)

        # Label và Entry để nhập màu mới cho nền button
        label3 = tk.Label(popup, text="Số điện thoại:")
        label3.pack(pady=5)
        
        entry3 = tk.Entry(popup)
        entry3.pack(pady=5)



                
                # Button để xác nhận chỉnh sửa và cập nhật tên và màu của button
        def get_first_customer_id():
            latest_customer_info = get_latest_customer_info()
            if latest_customer_info:
                return latest_customer_info[0]
            else:
                return 1

        def update_button_name_and_color():
            hoten = entry1.get()
            cancuoc = entry2.get()
            sdt = entry3.get()
            first_name = get_first_name(hoten)
            
            # Database
            
            
            customer_id = insert_khachhang2(hoten, cancuoc, sdt)  # Lấy ID của khách hàng đầu tiên
            
            update_phong(sophong, int(giaphong), customer_id)
            
            if hoten:
                button.config(text=f"{sophong}\n\n{first_name}")
                button.config(command=lambda: payment_info(button, sophong))
            
            popup.destroy()

        update_button = tk.Button(popup, text="Cập nhật", command=update_button_name_and_color)
        update_button.pack(pady=10)


def sort_the_fucking_button_ok():
    visible_buttons = [(button, position) for button, hidden, position in zip(buttons, hidden_buttons, range(1, len(buttons) + 1)) if not hidden]
    #original_positions = []
    for i, (button, position) in enumerate(visible_buttons):
        button.grid(row=i // 5, column=i % 5, padx=5, pady=5)
        button_info = button.grid_info()  # Lấy thông tin vị trí
        row = button_info["row"]  # Lấy giá trị của thuộc tính "row"
        column = button_info["column"]  # Lấy giá trị của thuộc tính "column"
        original_positions[position - 1] = (row, column)  # Thay thế vị trí tương ứng trong original_positions
    #Làm đến đây mới thấy có cái tham chiếu của C++ thì nhàn
    #mỗi tội Python thì ko có, vẫn làm được nhưng phức tạp
    #bà mẹ nó sắp xong rồi mà còn gặp con mẹ này
    




def disable_button(btn):
    btn.config(state=tk.DISABLED)

def enable_button(btn):
    btn.config(state=tk.NORMAL)

def reorganize_buttons():
    current_number_room = get_all_so_phong()
    visible_buttons = [button for button, hidden in zip(buttons, hidden_buttons) if not hidden]
    for i, so_phong in enumerate(current_number_room):
        phong_tro = select_phong_by_id(so_phong)
        if check_phong_has_khachhang(so_phong):
            red_button(visible_buttons[i], so_phong)


    red_buttons = [button for button, hidden in zip(buttons, hidden_buttons) if not hidden and button.cget('bg') == 'red']
    other_buttons = [button for button, hidden in zip(buttons, hidden_buttons) if not hidden and button.cget('bg') != 'red']
    for i, button in enumerate(red_buttons + other_buttons):
        button.grid(row=i // 5, column=i % 5, padx=5, pady=5)
        #print(button)
    sort_button.config(text="Quay lại", command=restore_positions)
    disable_button(add_button_button)
    
# Create a function to restore buttons to their original positions
def restore_positions():
    original_buttons = [button for button, hidden in zip(original_positions, hidden_buttons) if not hidden]
    visible_buttons = [button for button, hidden in zip(buttons, hidden_buttons) if not hidden]
    button_indices = [1]
    #print("zzzzzzzzzzzzzzzzzzzzzzzz")
    for visible in visible_buttons:
        visible = str(visible)
        index = visible.split("button")[-1]
        #index = int(index)
        if index != "":
            button_indices.append(index)
    #print("zzzzzzzzzzzzzzzzzzzzzzzz")
    #print(button_indices)
    #print(original_buttons)
    #print(buttons)
    for i, pos in enumerate(original_buttons):
        row = pos[0]
        column = pos[1]
        j = int(button_indices[i]) - 1
        buttons[j].grid(row=row, column=column, padx=5, pady=5)
        buttons[j].config(bg="SystemButtonFace")
    sort_button.config(text="Hiện phòng\nchưa đóng tiền", command=reorganize_buttons)
    enable_button(add_button_button)

def delete_function(btn, btn_id):
    if not hidden_buttons[btn_id-1]:
        #print(f"Button {btn_id} clicked.")
        confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa mục đã chọn?")
        if confirm:
            buttons[btn_id-1].grid_remove()  # Hide the clicked button
            hidden_buttons[btn_id-1] = True
            # reorganize_buttons()  # Reorganize the buttons after hiding one

def create_delete_function(btn, idx):
    return lambda: delete_function(btn, idx)
            


def change_command_all_button():
    visible_buttons = [button for button, hidden in zip(buttons, hidden_buttons) if not hidden]
    for i, button in enumerate(visible_buttons):
        button.config(command=create_delete_function(button, len(button_labels)))
    title_label.config(text="Hãy chọn vào phòng cần xoá!")
    delete_button.config(text="Ngừng xoá", command=reverse_change_command)

def reverse_change_command():
    title_label.config(text="Quản lý nhà trọ")
    delete_button.config(text="Xoá phòng", command=change_command_all_button)
    visible_buttons = [button for button, hidden in zip(buttons, hidden_buttons) if not hidden]
    for i, button in enumerate(visible_buttons):
        button.config(command=lambda idx=i, btn=button: edit_button(btn, idx))

def test():
    visible_buttons = [button for button, hidden in zip(buttons, hidden_buttons) if not hidden]
    #print(button_labels)
    #print("/n")
    #print(visible_buttons)


#Treeview Area -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View

def get_real_time():
    # Lấy thời gian thực hiện tại
    now = datetime.datetime.now()

    # Lấy thông tin về thời gian hiện tại
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second

    # Trả về thông tin thời gian thực dưới dạng chuỗi
    real_time_str = f"{day}/{month}/{year}"
    return real_time_str

def treeview(original_button, room_id):
    def insert_data_to_treeview():
        thongtinphong.get_input_data()
        tree.insert('', 'end', values=())

    def add_item():
        # Tạo cửa sổ "Add" đa trường
        add_window = tk.Toplevel(root)
        add_window.title("Thêm tháng")


        # Tạo các nhãn và hộp văn bản cho từng trường
        fields = ["Tháng", "Số điện", "Số nước"]
        entries = []
        for field in fields:
            tk.Label(add_window, text=field).pack()
            entry = tk.Entry(add_window)
            entry.pack()
            entries.append(entry)

        # Tạo nút "Add" trong cửa sổ "Add"
        def add_item():
            data = [entry.get() for entry in entries]
            tiengiaodien = float(data[1]) * giadien  # Tính tiền giá điện
            tiengianuoc = float(data[2]) * gianuoc  # Tính tiền giá nước
            tongtien = tiengiaodien + tiengianuoc
            tongtien2 = tongtien
            tongtien4 = int((tongtien2)) + int(room_info[1])
            tongtien3 = format_currency(tongtien4)
            data.append(tongtien3)  # Thêm tổng tiền vào danh sách dữ liệu
            thoi_gian_thuc = get_real_time()
            thang_hoa_don = data[0]
            insert_hoadon(customer_info[0], room_info[0], room_info[1], tiengiaodien, tiengianuoc, thoi_gian_thuc, False, thang_hoa_don)
            if tongtien != 0:
                data.append("Chưa thanh toán")
            tree.insert('', 'end', values=data)
            add_window.destroy()

        add_button = tk.Button(add_window, text="Thêm tháng", command=add_item)
        add_button.pack()

#Định dạng 1000000 sang 1.000.000đ
    def format_currency(number):
        # Định dạng số thành chuỗi với dấu phân cách ',' mỗi 3 chữ số
        formatted_number = "{:,.0f}".format(number)
        # Thay thế dấu phân cách mặc định (,) bằng dấu chấm (.)
        formatted_number = formatted_number.replace(",", ".")
        # Thêm ký tự 'đ' vào cuối chuỗi
        formatted_number += "đ"
        return formatted_number

#Ngược lại 1.000.000đ sang 1000000
    def parse_currency(currency_string):
        # Xóa ký tự 'đ' cuối chuỗi
        currency_string = currency_string.rstrip('đ')
        # Xóa dấu chấm phân cách để trở về dạng chuỗi gốc
        currency_string = currency_string.replace(".", "")
        # Chuyển chuỗi thành số
        try:
            number = float(currency_string)
            return number
        except ValueError:
            #print("Invalid currency format!")
            return None

    def edit_item():
        # Lấy danh sách các phần tử được chọn trong treeview
        giatri = tree.selection()
        selected_item = tree.item(giatri)['values']
        # Duyệt qua từng phần tử đã chọn và sử dụng phương thức 'selection_set' để chọn cả hàng
        #print(selected_item)
        if selected_item:

            index = tree.index(giatri)
            def delete_hoa_don_by_index(index):
                hoa_don_list = get_hoadon_by_so_phong(sophong)  # Lấy danh sách hoá đơn dựa trên số phòng
                if index < 0 or index >= len(hoa_don_list):
                    return False

                hoa_don_to_update = hoa_don_list[index]

                # Xác định các giá trị của hoá đơn cần xóa
                khachhang_id = hoa_don_to_update[1]
                so_phong = hoa_don_to_update[2]
                tienphong = hoa_don_to_update[3]
                tiendien = hoa_don_to_update[4]
                tiennuoc = hoa_don_to_update[5]
                ngay_thanh_toan = hoa_don_to_update[6]
                thang_thanh_toan = hoa_don_to_update[7]


            # Tạo cửa sổ "Edit" đa trường
            edit_window = tk.Toplevel(root)
            edit_window.title("Sửa thông tin phòng trọ")

            # Tạo các nhãn và hộp văn bản cho từng trường và điền giá trị hiện tại vào các hộp văn bản
            fields = ["Tháng", "Số điện", "Số nước"]
            entries = []
            for idx, field in enumerate(fields):
                tk.Label(edit_window, text=field).pack()
                entry = tk.Entry(edit_window)
                entry.pack()
                entry.insert(0, str(selected_item[idx]))  # Điền giá trị hiện tại vào hộp văn bản
                entries.append(entry)

            # Tạo nút "Save" trong cửa sổ "Edit"
            def save_changes():
                new_data = [entry.get() for entry in entries]

                # Calculate the new total cost for the row
                tiengiaodien = float(new_data[1]) * giadien
                tiengianuoc = float(new_data[2]) * gianuoc

                def get_current_month():
                    current_date = datetime.datetime.now()
                    current_month = current_date.month
                    return current_month
                
                room_info = select_phong_by_id(room_id)
                customer_info = get_customer_info_by_phong(room_id)
                
                tongtien = tiengiaodien + tiengianuoc
                tongtien2 = tongtien
                tongtien3 = format_currency(int(tongtien2) + int(room_info[1]))
                new_data.append(tongtien3)


                thang_hoa_don = new_data[0]
                hoadon_id = get_hoadon_id_by_sophong(room_info[0])
                if index < 0 or index >= len(hoadon_id):
                    return False
                hoadon_id_update = hoadon_id[index]
                if tongtien !=0:
                    new_data.append(get_real_time())
                    update_hoadon(hoadon_id_update, customer_info[0], room_info[0], room_info[1], tiengiaodien, tiengianuoc, get_real_time(), True, thang_hoa_don)
                else:
                    new_data.append("Chưa thanh toán")
                    update_hoadon(hoadon_id_update, customer_info[0], room_info[0], room_info[1], tiengiaodien, tiengianuoc, "Chưa thanh toán", False, thang_hoa_don)
                # Get the currently selected item in the treeview
                selected_item = tree.selection()

                if selected_item:
                    # Update the values of the selected row only, not all rows
                    tree.item(selected_item, values=new_data)

                
                edit_window.destroy()

            save_button = tk.Button(edit_window, text="Lưu thay đổi", command=save_changes)
            save_button.pack()

    def delete_selected_row(): #Done
        selected_items = tree.selection()
        index = tree.index(selected_items)
        def delete_hoa_don_by_index(index):
            hoa_don_list = get_hoadon_by_so_phong(sophong)  # Lấy danh sách hoá đơn dựa trên số phòng
            if index < 0 or index >= len(hoa_don_list):
                return False

            hoa_don_to_delete = hoa_don_list[index]

            # Xác định các giá trị của hoá đơn cần xóa
            khachhang_id = hoa_don_to_delete[1]
            so_phong = hoa_don_to_delete[2]
            tienphong = hoa_don_to_delete[3]
            tiendien = hoa_don_to_delete[4]
            tiennuoc = hoa_don_to_delete[5]
            ngay_thanh_toan = hoa_don_to_delete[6]
            thang_thanh_toan = hoa_don_to_delete[7]
            thang_hoa_don = hoa_don_to_delete[8]
            delete_hoadon(khachhang_id, so_phong, tienphong, tiendien, tiennuoc, ngay_thanh_toan, thang_thanh_toan, thang_hoa_don)

        if selected_items:
            # Hiển thị popup xác nhận
            confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa mục đã chọn?")
            
            if confirm:
                delete_hoa_don_by_index(index)
                for item in selected_items:
                    tree.delete(item)


    def edit_customer_info(): #Done
        popup = tk.Toplevel(root)
        popup.title("Thông tin người thuê")
        
        # Label và Entry để nhập giá trị mới cho tên button
        label000 = tk.Label(popup, text="Phòng:")
        label000.pack(pady=5)
        
        entry000 = tk.Entry(popup)
        entry000.pack(pady=5)
        entry000.insert(0, sophong)

        label001 = tk.Label(popup, text="Giá:")
        label001.pack(pady=5)
        
        entry001 = tk.Entry(popup)
        entry001.pack(pady=5)
        entry001.insert(0, giaphong)

        label111 = tk.Label(popup, text="Họ Tên:")
        label111.pack(pady=5)
        
        
        entry111 = tk.Entry(popup)
        entry111.pack(pady=5)
        entry111.insert(0, hoten)

        # Label và Entry để nhập màu mới cho nền button
        label222 = tk.Label(popup, text="CCCD:")
        label222.pack(pady=5)
        
        entry222 = tk.Entry(popup)
        entry222.pack(pady=5)
        entry222.insert(0, cancuoc)

        # Label và Entry để nhập màu mới cho nền button
        label333 = tk.Label(popup, text="Số điện thoại:")
        label333.pack(pady=5)
        
        entry333 = tk.Entry(popup)
        entry333.pack(pady=5)
        entry333.insert(0, sdt)
        def xacnhan_button():
            sophong = entry000.get()
            giaphong = entry001.get()
            hoten = entry111.get()
            cancuoc = entry222.get()
            sdt = entry333.get()

            
            update_data(customer_info[0], sophong, giaphong, hoten, cancuoc, sdt)

            
            popup.destroy()
            label0.config(text="Phòng: " + sophong)
            label01.config(text="Giá: " + str(giaphong))
            label1.config(text="Họ và tên: " + hoten)
            label2.config(text="CCCD: " + cancuoc)
            label3.config(text="SĐT: " + sdt)
            original_button.config(text=str(sophong)+"\n\n"+get_first_name(str(hoten)), command=lambda: payment_info(original_button, sophong))
        xacnhan = tk.Button(popup, text="Xác nhận", command=xacnhan_button)
        xacnhan.pack(pady=10)

    def destroy_button(): #Done
        confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa phòng này?")
        if confirm:
            btn_id = get_btn_id_from_button(original_button)
            #print(btn_id)
            #print(buttons[btn_id-1])
            buttons[btn_id-1].grid_remove()  
            # Hide the clicked button
            hidden_buttons[btn_id-1] = True
            #print(buttons[btn_id-1])
            customer_info = get_customer_info_by_phong(room_id)

            delete_customer_with_related_info(customer_info[0])

            sort_the_fucking_button_ok()

            root.destroy()

    def clear_treeview(): #Done
        confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa toàn bộ hoá đơn?")
        if confirm:
            hoa_don_list = get_hoadon_by_so_phong(sophong)  # Lấy danh sách hoá đơn dựa trên số phòng
            tree.delete(*tree.get_children())
            for hoa_don_to_delete in hoa_don_list:
                khachhang_id = hoa_don_to_delete[1]
                so_phong = hoa_don_to_delete[2]
                tienphong = hoa_don_to_delete[3]
                tiendien = hoa_don_to_delete[4]
                tiennuoc = hoa_don_to_delete[5]
                ngay_thanh_toan = hoa_don_to_delete[6]
                thang_thanh_toan = hoa_don_to_delete[7]
                thang_hoa_don = hoa_don_to_delete[8]
                delete_hoadon(khachhang_id, so_phong, tienphong, tiendien, tiennuoc, ngay_thanh_toan, thang_thanh_toan, thang_hoa_don)
            
            


    def is_past_month(date_string):
        try:
            date_datetime = datetime.strptime(date_string, '%d/%m/%Y')
            current_datetime = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            return date_datetime < current_datetime

        except ValueError:
            return False

    def check_current():
        for date in hoadon:
            if is_past_month(date[6]):
                button.config(bg="red")

    def dongtien():
        selected_items = tree.selection()
        index = tree.index(selected_items)
        if selected_items:
            room_info = select_phong_by_id(room_id)
            hoa_don_list = get_hoadon_by_so_phong(room_info[0])
            
            if index < 0 or index >= len(hoa_don_list):
                return False
            
            hoa_don_to_update = hoa_don_list[index]
            tiengianuoc = hoa_don_to_update[4]
            tiengiaodien = hoa_don_to_update[5]
            ngay_thanh_toan = hoa_don_to_update[6]
            thang_hoa_don = hoa_don_to_update[8]
            #print(ngay_thanh_toan)
            thang_thanh_toan = hoa_don_to_update[7]  # Index of the 8th column in the list
            hoadon_id = get_hoadon_id_by_sophong(room_info[0])
            if index < 0 or index >= len(hoadon_id):
                return False
            hoadon_id_update = hoadon_id[index]
            
            if thang_thanh_toan == True:  # Check if thang_thanh_toan is True
                update_hoadon(hoadon_id_update, customer_info[0], room_info[0], room_info[1], tiengiaodien, tiengianuoc, ngay_thanh_toan, False, thang_hoa_don)
                thanhtoan = list(tree.item(selected_items, "values"))  # Convert tuple to list
                thanhtoan[4] = "Chưa thanh toán"  # Update the 5th column value
                tree.item(selected_items, values=thanhtoan)  # Update Treeview item with new values
                #red_button(original_button, room_info[0])
            else:
                update_hoadon(hoadon_id_update, customer_info[0], room_info[0], room_info[1], tiengiaodien, tiengianuoc, get_real_time(), True, thang_hoa_don)
                thanhtoan = list(tree.item(selected_items, "values"))  # Convert tuple to list
                thanhtoan[4] = get_real_time()  # Update the 5th column value
                tree.item(selected_items, values=thanhtoan)  # Update Treeview item with new values
                #red_button(original_button, room_info[0])


            
    
    room_info = select_phong_by_id(room_id)
    customer_info = get_customer_info_by_phong(room_id)

    #print(room_info)
    #print(customer_info)

    current_price_id = get_latest_giadiennuoc_id()
    giadiennuoc = select_giadiennuoc_by_id(current_price_id)
    giadien = giadiennuoc[1]
    gianuoc = giadiennuoc[2]

    sophong = room_info[0]
    giaphong = room_info[1]
    hoten = customer_info[1]
    cancuoc = customer_info[2]
    sdt = customer_info[3]




    hoadon = get_hoadon_by_so_phong(room_id)
    data = []
    for hoadon_info in hoadon:
        value_2 = format_currency(int(hoadon_info[3] + hoadon_info[4] + hoadon_info[5]))
        value_4 = hoadon_info[4] / giadien
        value_5 = hoadon_info[5] / gianuoc
        value_6 = str(hoadon_info[6])
        value_7 = parse(value_6)
        value_8 = hoadon_info[8]
        flag = hoadon_info[7]
        if flag:
            data.append((value_8, value_4, value_5, value_2, value_6))
        else:
            data.append((value_8, value_4, value_5, value_2, "Chưa thanh toán"))



    #check_current()

    # Tạo giao diện đồ họa tkinter
    root = tk.Tk()
    root.title("Quản lý phòng trọ")

    label_frame = tk.Frame(root)
    label_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=50, pady=10)

    # Tiêu đề Label
    header_font = font.Font(size=12, weight="bold")
    header_label = tk.Label(label_frame, text="Thông tin người thuê", font=header_font)
    header_label.pack(pady=5, anchor="w")


    # Tạo các label và button
    label0 = tk.Label(label_frame, text="Phòng: " + str(sophong))
    label0.pack(pady=10, anchor="w")

    label01 = tk.Label(label_frame, text="Giá: " + str(giaphong))
    label01.pack(pady=10, anchor="w")


    label1 = tk.Label(label_frame, text="Họ và tên: " + hoten)
    label1.pack(pady=10, anchor="w")

    label2 = tk.Label(label_frame, text="CCCD: " + cancuoc)
    label2.pack(pady=10, anchor="w")

    label3 = tk.Label(label_frame, text="SĐT: " + sdt)
    label3.pack(pady=10, anchor="w")


    tree_frame = tk.Frame(root)
    tree_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)


    # Tiêu đề Treeview
    tree_header_font = font.Font(size=12, weight="bold")
    tree_header_label = tk.Label(tree_frame, text="Lịch sử thanh toán", font=tree_header_font)
    tree_header_label.pack()

    # Tạo Treeview và thêm các cột
    tree = ttk.Treeview(tree_frame, columns=("Tháng", "Số điện", "Số nước", "Tổng tiền", "Đóng tiền"), show="headings")
    tree.heading("#1", text="Tháng")
    tree.heading("#2", text="Số điện")
    tree.heading("#3", text="Số nước")
    tree.heading("#4", text="Tổng tiền")
    tree.heading("#5", text="Đóng tiền")

    for child in tree.get_children():
        tree.set(child, "#4", format_currency_cell(tree.set(child, "#4")))

    # Đưa treeview vào thanh cuộn
    tree_scroll = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
    tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    tree.configure(yscrollcommand=tree_scroll.set)

    # Đưa treeview vào giao diện
    tree.pack(fill=tk.BOTH, expand=True)



    # Thêm dữ liệu mẫu

    

    
    #[
    #    ("101", 500, 100, 50, 650),
    #    ("102", 600, 120, 60, 780),
    #    ("103", 550, 110, 55, 715),
    #]
    for record in data:
        tree.insert("", tk.END, values=record)

    button_frame = tk.Frame(tree_frame)
    button_frame.pack(pady=10)

    button_label_frame = tk.Frame(label_frame)
    button_label_frame.pack(pady=10)

    add_button = tk.Button(button_frame, text="Thêm", command=add_item)
    add_button.pack(side=tk.LEFT, padx=5)

    delete_button = tk.Button(button_frame, text="Xóa", command=delete_selected_row)
    delete_button.pack(side=tk.LEFT, padx=5)

    update_button = tk.Button(button_frame, text="Cập nhật", command=edit_item)
    update_button.pack(side=tk.LEFT, padx=5)

    clear_button = tk.Button(button_frame, text="Xoá lịch sử thanh toán", command=clear_treeview)
    clear_button.pack(side=tk.LEFT, padx=5)

    destroy_button = tk.Button(button_frame, text="Xoá phòng", command=destroy_button)
    destroy_button.pack(side=tk.LEFT, padx=5)

    dongtien_button = tk.Button(button_frame, text="Đóng tiền", command=dongtien)
    dongtien_button.pack(side=tk.LEFT, padx=5)

    update_customer_button = tk.Button(button_label_frame, text="Sửa thông tin người thuê", command=edit_customer_info)
    update_customer_button.pack(side=tk.LEFT, padx=5)


    #red_button(original_button, room_id)
    # Tạo nút "Chỉnh sửa" và "Lưu thay đổi"
    #edit_button = tk.Button(root, text="Chỉnh sửa", command=edit_item)
    #add_button = tk.Button(root, text="Thêm", command=add_item)
    #delete_button = tk.Button(root, text="Xóa", command=delete_selected_row)


    # Đặt vị trí các widget trong giao diện
    #tree.grid(row=0, column=0, columnspan=6, padx=10, pady=10)
    #edit_button.grid(row=2, column=1, pady=5, sticky="E")
    #add_button.grid(row=2, column=2, pady=5, sticky="E")
    #delete_button.grid(row=2, column=3, pady=5, sticky="E")

    #tree.tag_configure("highlighted", background="yellow")

    root.mainloop()
#Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View  -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View  -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View















        

root = tk.Tk()
root.title("Quản lý nhà trọ")
root.geometry("500x500")
root.minsize(500, 500)    # Đặt kích thước tối thiểu
root.maxsize(500, 500)    # Đặt kích thước tối đa
#label
title_label = tk.Label(root, text="Quản lý nhà trọ", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

button_frame2 = tk.Frame(root)
button_frame2.pack(side=tk.TOP, anchor=tk.NE, pady=10)

add_button_button = tk.Button(button_frame2, text="Thêm Phòng", command=add_button, width=12, height=3)
thaydoigia_button = tk.Button(button_frame2, text="Thay đổi giá\nđiện/nước", command=thaydoigia, width=12, height=3)
sort_button = tk.Button(button_frame2, text="Hiện phòng\nchưa đóng tiền", command=reorganize_buttons, width=12, height=3)
#delete_button = tk.Button(root, text="Xoá phòng", command=change_command_all_button)
#test_button = tk.Button(root, text="Test", command=test)

#Pack
add_button_button.grid(row=0, column=2, padx=10)
thaydoigia_button.grid(row=0, column=1, padx=10)
sort_button.grid(row=0, column=0, padx=10)
#delete_button.pack(side=tk.TOP, anchor=tk.NE, pady=10)
#test_button.pack(side=tk.TOP, anchor=tk.NE, pady=10)


# Create a Scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a Canvas to contain the buttons and link it to the Scrollbar
canvas = tk.Canvas(root, yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=canvas.yview)

# Tạo frame để chứa các nút
button_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=button_frame, anchor="nw")


# Mảng để lưu các thông tin đã nhập
button_id_dict = {}
button_labels = []
buttons = [] #Các button hiển thị
hidden_buttons = [] #Các button ẩn được liên kết với button hiển thị
original_positions = []  # Store the original positions of buttons
sorted_positions = []  # Store the positions after sorting
thongtinphongtro = []
num_buttons_added = 0

current_number_room = get_all_so_phong()

for i, so_phong in enumerate(current_number_room):

    button = tk.Button(button_frame)
    btn_id = len(buttons) + 1
    button_id_dict[button] = btn_id
    button.grid(row=i // 5, column=i % 5, padx=5, pady=5)
    buttons.append(button)
    hidden_buttons.append(False)
    
    #print(khach_hang_info[1])
    
    phong_tro = select_phong_by_id(so_phong)
    if check_phong_has_khachhang(so_phong):
        #print(phong_tro[1])
        #Á đù má vãi cả lò
        khach_hang_info = get_customer_info_by_phong(so_phong)
        ten = get_first_name(khach_hang_info[1])
        buttons[btn_id-1].config(text=str(so_phong) + "\n\n" + ten, width=10, height=5, command=lambda btn_id=btn_id, phong_tro=phong_tro: payment_info(buttons[btn_id-1], phong_tro[0]))
        #red_button(buttons[btn_id-1], so_phong)
        button_info = buttons[btn_id-1].grid_info()  # Lấy thông tin vị trí
        row = button_info["row"]  # Lấy giá trị của thuộc tính "row"
        column = button_info["column"]  # Lấy giá trị của thuộc tính "column"
        original_positions.append((row, column))  # Thêm vào danh sách
    else:
        buttons[btn_id-1].config(text=str(so_phong) + "\n\nTrống", width=10, height=5, command=lambda btn_id=btn_id, phong_tro=phong_tro: edit_button(buttons[btn_id-1], btn_id, so_phong, phong_tro[0]))

        button_info = buttons[btn_id-1].grid_info()  # Lấy thông tin vị trí
        row = button_info["row"]  # Lấy giá trị của thuộc tính "row"
        column = button_info["column"]  # Lấy giá trị của thuộc tính "column"
        original_positions.append((row, column))  # Thêm vào danh sách



# Bind the canvas configuration function to the canvas scroll event
canvas.bind("<Configure>", on_configure)

=======
import tkinter as tk
from tkinter import messagebox, ttk, font
from tkinter import *
from dateutil.parser import parse
import datetime

from add_window_khachhang import InputWindow
#from treeview import treeview, giadien, gianuoc
from app_database_structure import *

def on_configure(event):
    # Configure the canvas scroll region to be the size of the buttons area
    canvas.configure(scrollregion=canvas.bbox("all"))

def red_button(original_button, room_id):
    hoadon = get_hoadon_by_so_phong(room_id)
    found_zero = False
    
    for hoadon_moithang in hoadon:
        if hoadon_moithang[7] == 0:
            original_button.config(bg="red")
            found_zero = True
            break
            
    if not found_zero:
        original_button.config(bg="SystemButtonFace")

def thaydoigia():
    popup = tk.Toplevel(root)
    popup.geometry("300x200")
    popup.title("Thay đổi giá")

    label1 = tk.Label(popup, text="Giá điện:")
    label1.pack(pady=5)
    
    entry1 = tk.Entry(popup)
    entry1.pack(pady=5)
    current_price_id = get_latest_giadiennuoc_id()
    giadiennuoc = select_giadiennuoc_by_id(current_price_id)
    entry1.insert(0, giadiennuoc[1])
    # giadiennuoc = [(id, giadien, gianuoc)]

    # Label và Entry để nhập màu mới cho nền button
    label2 = tk.Label(popup, text="Giá nước:")
    label2.pack(pady=5)
    
    entry2 = tk.Entry(popup)
    entry2.pack(pady=5)
    entry2.insert(0, giadiennuoc[2])

    def xacnhan_button():
        giadien = entry1.get()
        gianuoc = entry2.get()
        insert_giadiennuoc(giadien, gianuoc)
        popup.destroy()

    xacnhan = tk.Button(popup, text="Xác nhận", command=xacnhan_button)
    xacnhan.pack(pady=10)

def add_button():
    global num_buttons_added
    popup = tk.Toplevel(root)
    popup.geometry("300x200")
    popup.title("Thêm phòng")
    
    # Label và Entry để nhập giá trị mới cho tên button
    label1 = tk.Label(popup, text="Mã phòng:")
    label1.pack(pady=5)
    
    entry1 = tk.Entry(popup)
    entry1.pack(pady=5)

    # Label và Entry để nhập màu mới cho nền button
    label2 = tk.Label(popup, text="Tiền thuê:")
    label2.pack(pady=5)
    
    entry2 = tk.Entry(popup)
    entry2.pack(pady=5)
    
    # Button để xác nhận chỉnh sửa và cập nhật tên và màu của button
    def update_button_name_and_color():
        new_name = entry1.get()
        giaphong = entry2.get()

        insert_phong(new_name, giaphong)
        #print(giaphong)
        #new_color = entry2.get()
        #if new_name:
            #button.config(text=f"\n  {new_name}  \n")
        
        #if new_color:
        #    button.config(bg=new_color)

        global button_labels
        new_button_label = f"Button {len(button_labels) + 1}"
        button_labels.append(new_button_label)
        
        btn_id = len(buttons) + 1

        new_button = tk.Button(button_frame, text=new_name + "\n\nTrống", width=10, height=5, command=lambda idx=len(button_labels): edit_button(new_button, idx, giaphong, new_name))
        #new_button.config(command=lambda: edit_button(new_button, giaphong))  # Gán hàm edit_button tương ứng cho nút mới
        # new_button.grid(row=num_buttons_added // 4, column=num_buttons_added % 4, padx=10, pady=10)
        buttons.append(new_button)
        hidden_buttons.append(False)
        visible_buttons = [button for button, hidden in zip(buttons, hidden_buttons) if not hidden]
        for i, button in enumerate(visible_buttons):
            button.grid(row=i // 5, column=i % 5, padx=5, pady=5)

        button_id_dict[new_button] = btn_id
        
        canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

        button_info = button.grid_info()  # Lấy thông tin vị trí
        row = button_info["row"]  # Lấy giá trị của thuộc tính "row"
        column = button_info["column"]  # Lấy giá trị của thuộc tính "column"
        original_positions.append((row, column))  # Thêm vào danh sách
        popup.destroy()

    
    update_button = tk.Button(popup, text="Thêm phòng", command=update_button_name_and_color)
    update_button.pack(pady=10)
    num_buttons_added += 1
    #print(num_buttons_added)
    #print(buttons)
    #print(hidden_buttons)
    #print(button_labels)

def get_btn_id_from_button(button):
    return button_id_dict.get(button, None)

def payment_info(button, sophong):
    treeview(button, sophong)

def get_first_name(full_name):
    # Tách chuỗi nhập thành danh sách các từ
    name_parts = full_name.split()

    # Lấy tên từ phần tử cuối cùng của danh sách
    first_name = name_parts[-1]

    return first_name

def get_last_name(full_name):
    # Tách chuỗi nhập thành danh sách các từ
    name_parts = full_name.split()

    # Lấy họ từ phần tử đầu tiên của danh sách
    last_name = name_parts[0]

    return last_name

def edit_button(button, btn_id, giaphong, sophong):
        popup = tk.Toplevel(root)
        popup.title("Nhập thông tin người thuê")
        
        # Label và Entry để nhập giá trị mới cho tên button
        label1 = tk.Label(popup, text="Họ Tên:")
        label1.pack(pady=5)
        
        entry1 = tk.Entry(popup)
        entry1.pack(pady=5)

        # Label và Entry để nhập màu mới cho nền button
        label2 = tk.Label(popup, text="CCCD:")
        label2.pack(pady=5)
        
        entry2 = tk.Entry(popup)
        entry2.pack(pady=5)

        # Label và Entry để nhập màu mới cho nền button
        label3 = tk.Label(popup, text="Số điện thoại:")
        label3.pack(pady=5)
        
        entry3 = tk.Entry(popup)
        entry3.pack(pady=5)



                
                # Button để xác nhận chỉnh sửa và cập nhật tên và màu của button
        def get_first_customer_id():
            latest_customer_info = get_latest_customer_info()
            if latest_customer_info:
                return latest_customer_info[0]
            else:
                return 1

        def update_button_name_and_color():
            hoten = entry1.get()
            cancuoc = entry2.get()
            sdt = entry3.get()
            first_name = get_first_name(hoten)
            
            # Database
            
            
            customer_id = insert_khachhang2(hoten, cancuoc, sdt)  # Lấy ID của khách hàng đầu tiên
            
            update_phong(sophong, int(giaphong), customer_id)
            
            if hoten:
                button.config(text=f"{sophong}\n\n{first_name}")
                button.config(command=lambda: payment_info(button, sophong))
            
            popup.destroy()

        update_button = tk.Button(popup, text="Cập nhật", command=update_button_name_and_color)
        update_button.pack(pady=10)


def sort_the_fucking_button_ok():
    visible_buttons = [(button, position) for button, hidden, position in zip(buttons, hidden_buttons, range(1, len(buttons) + 1)) if not hidden]
    #original_positions = []
    for i, (button, position) in enumerate(visible_buttons):
        button.grid(row=i // 5, column=i % 5, padx=5, pady=5)
        button_info = button.grid_info()  # Lấy thông tin vị trí
        row = button_info["row"]  # Lấy giá trị của thuộc tính "row"
        column = button_info["column"]  # Lấy giá trị của thuộc tính "column"
        original_positions[position - 1] = (row, column)  # Thay thế vị trí tương ứng trong original_positions
    #Làm đến đây mới thấy có cái tham chiếu của C++ thì nhàn
    #mỗi tội Python thì ko có, vẫn làm được nhưng phức tạp
    #bà mẹ nó sắp xong rồi mà còn gặp con mẹ này
    




def disable_button(btn):
    btn.config(state=tk.DISABLED)

def enable_button(btn):
    btn.config(state=tk.NORMAL)

def reorganize_buttons():
    current_number_room = get_all_so_phong()
    visible_buttons = [button for button, hidden in zip(buttons, hidden_buttons) if not hidden]
    for i, so_phong in enumerate(current_number_room):
        phong_tro = select_phong_by_id(so_phong)
        if check_phong_has_khachhang(so_phong):
            red_button(visible_buttons[i], so_phong)


    red_buttons = [button for button, hidden in zip(buttons, hidden_buttons) if not hidden and button.cget('bg') == 'red']
    other_buttons = [button for button, hidden in zip(buttons, hidden_buttons) if not hidden and button.cget('bg') != 'red']
    for i, button in enumerate(red_buttons + other_buttons):
        button.grid(row=i // 5, column=i % 5, padx=5, pady=5)
        #print(button)
    sort_button.config(text="Quay lại", command=restore_positions)
    disable_button(add_button_button)
    
# Create a function to restore buttons to their original positions
def restore_positions():
    original_buttons = [button for button, hidden in zip(original_positions, hidden_buttons) if not hidden]
    visible_buttons = [button for button, hidden in zip(buttons, hidden_buttons) if not hidden]
    button_indices = [1]
    #print("zzzzzzzzzzzzzzzzzzzzzzzz")
    for visible in visible_buttons:
        visible = str(visible)
        index = visible.split("button")[-1]
        #index = int(index)
        if index != "":
            button_indices.append(index)
    #print("zzzzzzzzzzzzzzzzzzzzzzzz")
    #print(button_indices)
    #print(original_buttons)
    #print(buttons)
    for i, pos in enumerate(original_buttons):
        row = pos[0]
        column = pos[1]
        j = int(button_indices[i]) - 1
        buttons[j].grid(row=row, column=column, padx=5, pady=5)
        buttons[j].config(bg="SystemButtonFace")
    sort_button.config(text="Hiện phòng\nchưa đóng tiền", command=reorganize_buttons)
    enable_button(add_button_button)

def delete_function(btn, btn_id):
    if not hidden_buttons[btn_id-1]:
        #print(f"Button {btn_id} clicked.")
        confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa mục đã chọn?")
        if confirm:
            buttons[btn_id-1].grid_remove()  # Hide the clicked button
            hidden_buttons[btn_id-1] = True
            # reorganize_buttons()  # Reorganize the buttons after hiding one

def create_delete_function(btn, idx):
    return lambda: delete_function(btn, idx)
            


def change_command_all_button():
    visible_buttons = [button for button, hidden in zip(buttons, hidden_buttons) if not hidden]
    for i, button in enumerate(visible_buttons):
        button.config(command=create_delete_function(button, len(button_labels)))
    title_label.config(text="Hãy chọn vào phòng cần xoá!")
    delete_button.config(text="Ngừng xoá", command=reverse_change_command)

def reverse_change_command():
    title_label.config(text="Quản lý nhà trọ")
    delete_button.config(text="Xoá phòng", command=change_command_all_button)
    visible_buttons = [button for button, hidden in zip(buttons, hidden_buttons) if not hidden]
    for i, button in enumerate(visible_buttons):
        button.config(command=lambda idx=i, btn=button: edit_button(btn, idx))

def test():
    visible_buttons = [button for button, hidden in zip(buttons, hidden_buttons) if not hidden]
    #print(button_labels)
    #print("/n")
    #print(visible_buttons)


#Treeview Area -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View

def get_real_time():
    # Lấy thời gian thực hiện tại
    now = datetime.datetime.now()

    # Lấy thông tin về thời gian hiện tại
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second

    # Trả về thông tin thời gian thực dưới dạng chuỗi
    real_time_str = f"{day}/{month}/{year}"
    return real_time_str

def treeview(original_button, room_id):
    def insert_data_to_treeview():
        thongtinphong.get_input_data()
        tree.insert('', 'end', values=())

    def add_item():
        # Tạo cửa sổ "Add" đa trường
        add_window = tk.Toplevel(root)
        add_window.title("Thêm tháng")


        # Tạo các nhãn và hộp văn bản cho từng trường
        fields = ["Tháng", "Số điện", "Số nước"]
        entries = []
        for field in fields:
            tk.Label(add_window, text=field).pack()
            entry = tk.Entry(add_window)
            entry.pack()
            entries.append(entry)

        # Tạo nút "Add" trong cửa sổ "Add"
        def add_item():
            data = [entry.get() for entry in entries]
            tiengiaodien = float(data[1]) * giadien  # Tính tiền giá điện
            tiengianuoc = float(data[2]) * gianuoc  # Tính tiền giá nước
            tongtien = tiengiaodien + tiengianuoc
            tongtien2 = tongtien
            tongtien4 = int((tongtien2)) + int(room_info[1])
            tongtien3 = format_currency(tongtien4)
            data.append(tongtien3)  # Thêm tổng tiền vào danh sách dữ liệu
            thoi_gian_thuc = get_real_time()
            thang_hoa_don = data[0]
            insert_hoadon(customer_info[0], room_info[0], room_info[1], tiengiaodien, tiengianuoc, thoi_gian_thuc, False, thang_hoa_don)
            if tongtien != 0:
                data.append("Chưa thanh toán")
            tree.insert('', 'end', values=data)
            add_window.destroy()

        add_button = tk.Button(add_window, text="Thêm tháng", command=add_item)
        add_button.pack()

#Định dạng 1000000 sang 1.000.000đ
    def format_currency(number):
        # Định dạng số thành chuỗi với dấu phân cách ',' mỗi 3 chữ số
        formatted_number = "{:,.0f}".format(number)
        # Thay thế dấu phân cách mặc định (,) bằng dấu chấm (.)
        formatted_number = formatted_number.replace(",", ".")
        # Thêm ký tự 'đ' vào cuối chuỗi
        formatted_number += "đ"
        return formatted_number

#Ngược lại 1.000.000đ sang 1000000
    def parse_currency(currency_string):
        # Xóa ký tự 'đ' cuối chuỗi
        currency_string = currency_string.rstrip('đ')
        # Xóa dấu chấm phân cách để trở về dạng chuỗi gốc
        currency_string = currency_string.replace(".", "")
        # Chuyển chuỗi thành số
        try:
            number = float(currency_string)
            return number
        except ValueError:
            #print("Invalid currency format!")
            return None

    def edit_item():
        # Lấy danh sách các phần tử được chọn trong treeview
        giatri = tree.selection()
        selected_item = tree.item(giatri)['values']
        # Duyệt qua từng phần tử đã chọn và sử dụng phương thức 'selection_set' để chọn cả hàng
        #print(selected_item)
        if selected_item:

            index = tree.index(giatri)
            def delete_hoa_don_by_index(index):
                hoa_don_list = get_hoadon_by_so_phong(sophong)  # Lấy danh sách hoá đơn dựa trên số phòng
                if index < 0 or index >= len(hoa_don_list):
                    return False

                hoa_don_to_update = hoa_don_list[index]

                # Xác định các giá trị của hoá đơn cần xóa
                khachhang_id = hoa_don_to_update[1]
                so_phong = hoa_don_to_update[2]
                tienphong = hoa_don_to_update[3]
                tiendien = hoa_don_to_update[4]
                tiennuoc = hoa_don_to_update[5]
                ngay_thanh_toan = hoa_don_to_update[6]
                thang_thanh_toan = hoa_don_to_update[7]


            # Tạo cửa sổ "Edit" đa trường
            edit_window = tk.Toplevel(root)
            edit_window.title("Sửa thông tin phòng trọ")

            # Tạo các nhãn và hộp văn bản cho từng trường và điền giá trị hiện tại vào các hộp văn bản
            fields = ["Tháng", "Số điện", "Số nước"]
            entries = []
            for idx, field in enumerate(fields):
                tk.Label(edit_window, text=field).pack()
                entry = tk.Entry(edit_window)
                entry.pack()
                entry.insert(0, str(selected_item[idx]))  # Điền giá trị hiện tại vào hộp văn bản
                entries.append(entry)

            # Tạo nút "Save" trong cửa sổ "Edit"
            def save_changes():
                new_data = [entry.get() for entry in entries]

                # Calculate the new total cost for the row
                tiengiaodien = float(new_data[1]) * giadien
                tiengianuoc = float(new_data[2]) * gianuoc

                def get_current_month():
                    current_date = datetime.datetime.now()
                    current_month = current_date.month
                    return current_month
                
                room_info = select_phong_by_id(room_id)
                customer_info = get_customer_info_by_phong(room_id)
                
                tongtien = tiengiaodien + tiengianuoc
                tongtien2 = tongtien
                tongtien3 = format_currency(int(tongtien2) + int(room_info[1]))
                new_data.append(tongtien3)


                thang_hoa_don = new_data[0]
                hoadon_id = get_hoadon_id_by_sophong(room_info[0])
                if index < 0 or index >= len(hoadon_id):
                    return False
                hoadon_id_update = hoadon_id[index]
                if tongtien !=0:
                    new_data.append(get_real_time())
                    update_hoadon(hoadon_id_update, customer_info[0], room_info[0], room_info[1], tiengiaodien, tiengianuoc, get_real_time(), True, thang_hoa_don)
                else:
                    new_data.append("Chưa thanh toán")
                    update_hoadon(hoadon_id_update, customer_info[0], room_info[0], room_info[1], tiengiaodien, tiengianuoc, "Chưa thanh toán", False, thang_hoa_don)
                # Get the currently selected item in the treeview
                selected_item = tree.selection()

                if selected_item:
                    # Update the values of the selected row only, not all rows
                    tree.item(selected_item, values=new_data)

                
                edit_window.destroy()

            save_button = tk.Button(edit_window, text="Lưu thay đổi", command=save_changes)
            save_button.pack()

    def delete_selected_row(): #Done
        selected_items = tree.selection()
        index = tree.index(selected_items)
        def delete_hoa_don_by_index(index):
            hoa_don_list = get_hoadon_by_so_phong(sophong)  # Lấy danh sách hoá đơn dựa trên số phòng
            if index < 0 or index >= len(hoa_don_list):
                return False

            hoa_don_to_delete = hoa_don_list[index]

            # Xác định các giá trị của hoá đơn cần xóa
            khachhang_id = hoa_don_to_delete[1]
            so_phong = hoa_don_to_delete[2]
            tienphong = hoa_don_to_delete[3]
            tiendien = hoa_don_to_delete[4]
            tiennuoc = hoa_don_to_delete[5]
            ngay_thanh_toan = hoa_don_to_delete[6]
            thang_thanh_toan = hoa_don_to_delete[7]
            thang_hoa_don = hoa_don_to_delete[8]
            delete_hoadon(khachhang_id, so_phong, tienphong, tiendien, tiennuoc, ngay_thanh_toan, thang_thanh_toan, thang_hoa_don)

        if selected_items:
            # Hiển thị popup xác nhận
            confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa mục đã chọn?")
            
            if confirm:
                delete_hoa_don_by_index(index)
                for item in selected_items:
                    tree.delete(item)


    def edit_customer_info(): #Done
        popup = tk.Toplevel(root)
        popup.title("Thông tin người thuê")
        
        # Label và Entry để nhập giá trị mới cho tên button
        label000 = tk.Label(popup, text="Phòng:")
        label000.pack(pady=5)
        
        entry000 = tk.Entry(popup)
        entry000.pack(pady=5)
        entry000.insert(0, sophong)

        label001 = tk.Label(popup, text="Giá:")
        label001.pack(pady=5)
        
        entry001 = tk.Entry(popup)
        entry001.pack(pady=5)
        entry001.insert(0, giaphong)

        label111 = tk.Label(popup, text="Họ Tên:")
        label111.pack(pady=5)
        
        
        entry111 = tk.Entry(popup)
        entry111.pack(pady=5)
        entry111.insert(0, hoten)

        # Label và Entry để nhập màu mới cho nền button
        label222 = tk.Label(popup, text="CCCD:")
        label222.pack(pady=5)
        
        entry222 = tk.Entry(popup)
        entry222.pack(pady=5)
        entry222.insert(0, cancuoc)

        # Label và Entry để nhập màu mới cho nền button
        label333 = tk.Label(popup, text="Số điện thoại:")
        label333.pack(pady=5)
        
        entry333 = tk.Entry(popup)
        entry333.pack(pady=5)
        entry333.insert(0, sdt)
        def xacnhan_button():
            sophong = entry000.get()
            giaphong = entry001.get()
            hoten = entry111.get()
            cancuoc = entry222.get()
            sdt = entry333.get()

            
            update_data(customer_info[0], sophong, giaphong, hoten, cancuoc, sdt)

            
            popup.destroy()
            label0.config(text="Phòng: " + sophong)
            label01.config(text="Giá: " + str(giaphong))
            label1.config(text="Họ và tên: " + hoten)
            label2.config(text="CCCD: " + cancuoc)
            label3.config(text="SĐT: " + sdt)
            original_button.config(text=str(sophong)+"\n\n"+get_first_name(str(hoten)), command=lambda: payment_info(original_button, sophong))
        xacnhan = tk.Button(popup, text="Xác nhận", command=xacnhan_button)
        xacnhan.pack(pady=10)

    def destroy_button(): #Done
        confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa phòng này?")
        if confirm:
            btn_id = get_btn_id_from_button(original_button)
            #print(btn_id)
            #print(buttons[btn_id-1])
            buttons[btn_id-1].grid_remove()  
            # Hide the clicked button
            hidden_buttons[btn_id-1] = True
            #print(buttons[btn_id-1])
            customer_info = get_customer_info_by_phong(room_id)

            delete_customer_with_related_info(customer_info[0])

            sort_the_fucking_button_ok()

            root.destroy()

    def clear_treeview(): #Done
        confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa toàn bộ hoá đơn?")
        if confirm:
            hoa_don_list = get_hoadon_by_so_phong(sophong)  # Lấy danh sách hoá đơn dựa trên số phòng
            tree.delete(*tree.get_children())
            for hoa_don_to_delete in hoa_don_list:
                khachhang_id = hoa_don_to_delete[1]
                so_phong = hoa_don_to_delete[2]
                tienphong = hoa_don_to_delete[3]
                tiendien = hoa_don_to_delete[4]
                tiennuoc = hoa_don_to_delete[5]
                ngay_thanh_toan = hoa_don_to_delete[6]
                thang_thanh_toan = hoa_don_to_delete[7]
                thang_hoa_don = hoa_don_to_delete[8]
                delete_hoadon(khachhang_id, so_phong, tienphong, tiendien, tiennuoc, ngay_thanh_toan, thang_thanh_toan, thang_hoa_don)
            
            


    def is_past_month(date_string):
        try:
            date_datetime = datetime.strptime(date_string, '%d/%m/%Y')
            current_datetime = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            return date_datetime < current_datetime

        except ValueError:
            return False

    def check_current():
        for date in hoadon:
            if is_past_month(date[6]):
                button.config(bg="red")

    def dongtien():
        selected_items = tree.selection()
        index = tree.index(selected_items)
        if selected_items:
            room_info = select_phong_by_id(room_id)
            hoa_don_list = get_hoadon_by_so_phong(room_info[0])
            
            if index < 0 or index >= len(hoa_don_list):
                return False
            
            hoa_don_to_update = hoa_don_list[index]
            tiengianuoc = hoa_don_to_update[4]
            tiengiaodien = hoa_don_to_update[5]
            ngay_thanh_toan = hoa_don_to_update[6]
            thang_hoa_don = hoa_don_to_update[8]
            #print(ngay_thanh_toan)
            thang_thanh_toan = hoa_don_to_update[7]  # Index of the 8th column in the list
            hoadon_id = get_hoadon_id_by_sophong(room_info[0])
            if index < 0 or index >= len(hoadon_id):
                return False
            hoadon_id_update = hoadon_id[index]
            
            if thang_thanh_toan == True:  # Check if thang_thanh_toan is True
                update_hoadon(hoadon_id_update, customer_info[0], room_info[0], room_info[1], tiengiaodien, tiengianuoc, ngay_thanh_toan, False, thang_hoa_don)
                thanhtoan = list(tree.item(selected_items, "values"))  # Convert tuple to list
                thanhtoan[4] = "Chưa thanh toán"  # Update the 5th column value
                tree.item(selected_items, values=thanhtoan)  # Update Treeview item with new values
                #red_button(original_button, room_info[0])
            else:
                update_hoadon(hoadon_id_update, customer_info[0], room_info[0], room_info[1], tiengiaodien, tiengianuoc, get_real_time(), True, thang_hoa_don)
                thanhtoan = list(tree.item(selected_items, "values"))  # Convert tuple to list
                thanhtoan[4] = get_real_time()  # Update the 5th column value
                tree.item(selected_items, values=thanhtoan)  # Update Treeview item with new values
                #red_button(original_button, room_info[0])


            
    
    room_info = select_phong_by_id(room_id)
    customer_info = get_customer_info_by_phong(room_id)

    #print(room_info)
    #print(customer_info)

    current_price_id = get_latest_giadiennuoc_id()
    giadiennuoc = select_giadiennuoc_by_id(current_price_id)
    giadien = giadiennuoc[1]
    gianuoc = giadiennuoc[2]

    sophong = room_info[0]
    giaphong = room_info[1]
    hoten = customer_info[1]
    cancuoc = customer_info[2]
    sdt = customer_info[3]




    hoadon = get_hoadon_by_so_phong(room_id)
    data = []
    for hoadon_info in hoadon:
        value_2 = format_currency(int(hoadon_info[3] + hoadon_info[4] + hoadon_info[5]))
        value_4 = hoadon_info[4] / giadien
        value_5 = hoadon_info[5] / gianuoc
        value_6 = str(hoadon_info[6])
        value_7 = parse(value_6)
        value_8 = hoadon_info[8]
        flag = hoadon_info[7]
        if flag:
            data.append((value_8, value_4, value_5, value_2, value_6))
        else:
            data.append((value_8, value_4, value_5, value_2, "Chưa thanh toán"))



    #check_current()

    # Tạo giao diện đồ họa tkinter
    root = tk.Tk()
    root.title("Quản lý phòng trọ")

    label_frame = tk.Frame(root)
    label_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=50, pady=10)

    # Tiêu đề Label
    header_font = font.Font(size=12, weight="bold")
    header_label = tk.Label(label_frame, text="Thông tin người thuê", font=header_font)
    header_label.pack(pady=5, anchor="w")


    # Tạo các label và button
    label0 = tk.Label(label_frame, text="Phòng: " + str(sophong))
    label0.pack(pady=10, anchor="w")

    label01 = tk.Label(label_frame, text="Giá: " + str(giaphong))
    label01.pack(pady=10, anchor="w")


    label1 = tk.Label(label_frame, text="Họ và tên: " + hoten)
    label1.pack(pady=10, anchor="w")

    label2 = tk.Label(label_frame, text="CCCD: " + cancuoc)
    label2.pack(pady=10, anchor="w")

    label3 = tk.Label(label_frame, text="SĐT: " + sdt)
    label3.pack(pady=10, anchor="w")


    tree_frame = tk.Frame(root)
    tree_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)


    # Tiêu đề Treeview
    tree_header_font = font.Font(size=12, weight="bold")
    tree_header_label = tk.Label(tree_frame, text="Lịch sử thanh toán", font=tree_header_font)
    tree_header_label.pack()

    # Tạo Treeview và thêm các cột
    tree = ttk.Treeview(tree_frame, columns=("Tháng", "Số điện", "Số nước", "Tổng tiền", "Đóng tiền"), show="headings")
    tree.heading("#1", text="Tháng")
    tree.heading("#2", text="Số điện")
    tree.heading("#3", text="Số nước")
    tree.heading("#4", text="Tổng tiền")
    tree.heading("#5", text="Đóng tiền")

    for child in tree.get_children():
        tree.set(child, "#4", format_currency_cell(tree.set(child, "#4")))

    # Đưa treeview vào thanh cuộn
    tree_scroll = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
    tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    tree.configure(yscrollcommand=tree_scroll.set)

    # Đưa treeview vào giao diện
    tree.pack(fill=tk.BOTH, expand=True)



    # Thêm dữ liệu mẫu

    

    
    #[
    #    ("101", 500, 100, 50, 650),
    #    ("102", 600, 120, 60, 780),
    #    ("103", 550, 110, 55, 715),
    #]
    for record in data:
        tree.insert("", tk.END, values=record)

    button_frame = tk.Frame(tree_frame)
    button_frame.pack(pady=10)

    button_label_frame = tk.Frame(label_frame)
    button_label_frame.pack(pady=10)

    add_button = tk.Button(button_frame, text="Thêm", command=add_item)
    add_button.pack(side=tk.LEFT, padx=5)

    delete_button = tk.Button(button_frame, text="Xóa", command=delete_selected_row)
    delete_button.pack(side=tk.LEFT, padx=5)

    update_button = tk.Button(button_frame, text="Cập nhật", command=edit_item)
    update_button.pack(side=tk.LEFT, padx=5)

    clear_button = tk.Button(button_frame, text="Xoá lịch sử thanh toán", command=clear_treeview)
    clear_button.pack(side=tk.LEFT, padx=5)

    destroy_button = tk.Button(button_frame, text="Xoá phòng", command=destroy_button)
    destroy_button.pack(side=tk.LEFT, padx=5)

    dongtien_button = tk.Button(button_frame, text="Đóng tiền", command=dongtien)
    dongtien_button.pack(side=tk.LEFT, padx=5)

    update_customer_button = tk.Button(button_label_frame, text="Sửa thông tin người thuê", command=edit_customer_info)
    update_customer_button.pack(side=tk.LEFT, padx=5)


    #red_button(original_button, room_id)
    # Tạo nút "Chỉnh sửa" và "Lưu thay đổi"
    #edit_button = tk.Button(root, text="Chỉnh sửa", command=edit_item)
    #add_button = tk.Button(root, text="Thêm", command=add_item)
    #delete_button = tk.Button(root, text="Xóa", command=delete_selected_row)


    # Đặt vị trí các widget trong giao diện
    #tree.grid(row=0, column=0, columnspan=6, padx=10, pady=10)
    #edit_button.grid(row=2, column=1, pady=5, sticky="E")
    #add_button.grid(row=2, column=2, pady=5, sticky="E")
    #delete_button.grid(row=2, column=3, pady=5, sticky="E")

    #tree.tag_configure("highlighted", background="yellow")

    root.mainloop()
#Tree View -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View  -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View  -- Tree View -- Tree View -- Tree View -- Tree View -- Tree View















        

root = tk.Tk()
root.title("Quản lý nhà trọ")
root.geometry("500x500")
root.minsize(500, 500)    # Đặt kích thước tối thiểu
root.maxsize(500, 500)    # Đặt kích thước tối đa
#label
title_label = tk.Label(root, text="Quản lý nhà trọ", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

button_frame2 = tk.Frame(root)
button_frame2.pack(side=tk.TOP, anchor=tk.NE, pady=10)

add_button_button = tk.Button(button_frame2, text="Thêm Phòng", command=add_button, width=12, height=3)
thaydoigia_button = tk.Button(button_frame2, text="Thay đổi giá\nđiện/nước", command=thaydoigia, width=12, height=3)
sort_button = tk.Button(button_frame2, text="Hiện phòng\nchưa đóng tiền", command=reorganize_buttons, width=12, height=3)
#delete_button = tk.Button(root, text="Xoá phòng", command=change_command_all_button)
#test_button = tk.Button(root, text="Test", command=test)

#Pack
add_button_button.grid(row=0, column=2, padx=10)
thaydoigia_button.grid(row=0, column=1, padx=10)
sort_button.grid(row=0, column=0, padx=10)
#delete_button.pack(side=tk.TOP, anchor=tk.NE, pady=10)
#test_button.pack(side=tk.TOP, anchor=tk.NE, pady=10)


# Create a Scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a Canvas to contain the buttons and link it to the Scrollbar
canvas = tk.Canvas(root, yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=canvas.yview)

# Tạo frame để chứa các nút
button_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=button_frame, anchor="nw")


# Mảng để lưu các thông tin đã nhập
button_id_dict = {}
button_labels = []
buttons = [] #Các button hiển thị
hidden_buttons = [] #Các button ẩn được liên kết với button hiển thị
original_positions = []  # Store the original positions of buttons
sorted_positions = []  # Store the positions after sorting
thongtinphongtro = []
num_buttons_added = 0

current_number_room = get_all_so_phong()

for i, so_phong in enumerate(current_number_room):

    button = tk.Button(button_frame)
    btn_id = len(buttons) + 1
    button_id_dict[button] = btn_id
    button.grid(row=i // 5, column=i % 5, padx=5, pady=5)
    buttons.append(button)
    hidden_buttons.append(False)
    
    #print(khach_hang_info[1])
    
    phong_tro = select_phong_by_id(so_phong)
    if check_phong_has_khachhang(so_phong):
        #print(phong_tro[1])
        #Á đù má vãi cả lò
        khach_hang_info = get_customer_info_by_phong(so_phong)
        ten = get_first_name(khach_hang_info[1])
        buttons[btn_id-1].config(text=str(so_phong) + "\n\n" + ten, width=10, height=5, command=lambda btn_id=btn_id, phong_tro=phong_tro: payment_info(buttons[btn_id-1], phong_tro[0]))
        #red_button(buttons[btn_id-1], so_phong)
        button_info = buttons[btn_id-1].grid_info()  # Lấy thông tin vị trí
        row = button_info["row"]  # Lấy giá trị của thuộc tính "row"
        column = button_info["column"]  # Lấy giá trị của thuộc tính "column"
        original_positions.append((row, column))  # Thêm vào danh sách
    else:
        buttons[btn_id-1].config(text=str(so_phong) + "\n\nTrống", width=10, height=5, command=lambda btn_id=btn_id, phong_tro=phong_tro: edit_button(buttons[btn_id-1], btn_id, so_phong, phong_tro[0]))

        button_info = buttons[btn_id-1].grid_info()  # Lấy thông tin vị trí
        row = button_info["row"]  # Lấy giá trị của thuộc tính "row"
        column = button_info["column"]  # Lấy giá trị của thuộc tính "column"
        original_positions.append((row, column))  # Thêm vào danh sách



# Bind the canvas configuration function to the canvas scroll event
canvas.bind("<Configure>", on_configure)

>>>>>>> 2980f569ef0d68128605192c6fa4df3f5808ad73
root.mainloop()