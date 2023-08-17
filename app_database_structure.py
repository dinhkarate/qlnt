<<<<<<< HEAD
import sqlite3

db_path = "khach_tro.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

def create_database():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Drop existing tables (if they exist)
    cursor.executescript('''
        DROP TABLE IF EXISTS HoaDon;
        DROP TABLE IF EXISTS Phong;
        DROP TABLE IF EXISTS GiaDienNuoc;
        DROP TABLE IF EXISTS KhachHang;
    ''')

    # Creating the tables
    cursor.executescript('''
        CREATE TABLE KhachHang (
            khachhang_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ho_ten TEXT NOT NULL,
            cccd TEXT NOT NULL,
            sdt TEXT NOT NULL
        );

        CREATE TABLE GiaDienNuoc (
            gia_id INTEGER PRIMARY KEY AUTOINCREMENT,
            giadien INTEGER NOT NULL,
            gianuoc INTEGER NOT NULL
        );

        CREATE TABLE Phong (
            so_phong INTEGER PRIMARY KEY,
            gia_tien INTEGER NOT NULL,
            khachhang_id INTEGER,
            FOREIGN KEY (khachhang_id) REFERENCES KhachHang (khachhang_id)         
        );

        CREATE TABLE HoaDon (
            hoadon_id INTEGER PRIMARY KEY AUTOINCREMENT,
            khachhang_id INTEGER NOT NULL,
            so_phong INTEGER NOT NULL,
            tienphong INTEGER NOT NULL,
            tiendien INTEGER NOT NULL,
            tiennuoc INTEGER NOT NULL,
            ngay_thanh_toan TEXT NOT NULL,
            thang_thanh_toan BOOLEAN NOT NULL,
            thang_hoa_don INTEGER NOT NULL,
            FOREIGN KEY (khachhang_id) REFERENCES KhachHang (khachhang_id),
            FOREIGN KEY (so_phong) REFERENCES Phong (so_phong)
        );
    ''')

    conn.commit()
    conn.close()




# CURD
def insert_khachhang(ho_ten, cccd, sdt):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO KhachHang (ho_ten, cccd, sdt) VALUES (?, ?, ?)", (ho_ten, cccd, sdt))
    conn.commit()
    conn.close()

def insert_giadiennuoc(giadien, gianuoc):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO GiaDienNuoc (giadien, gianuoc) VALUES (?, ?)", (giadien, gianuoc))
    conn.commit()
    conn.close()

def insert_khachhang2(ho_ten, cccd, sdt):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO KhachHang (ho_ten, cccd, sdt) VALUES (?, ?, ?)", (ho_ten, cccd, sdt))
    conn.commit()

    # Lấy ID của khách hàng vừa thêm
    cursor.execute("SELECT last_insert_rowid()")
    khachhang_id = cursor.fetchone()[0]

    conn.close()
    return khachhang_id

def insert_phong(so_phong, gia_tien, khachhang_id=None):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Phong (so_phong, gia_tien, khachhang_id) VALUES (?, ?, ?)", (so_phong, gia_tien, khachhang_id))
    conn.commit()
    conn.close()

def insert_hoadon(khachhang_id, so_phong, tienphong, tiendien, tiennuoc, ngay_thanh_toan, thang_thanh_toan, thang_hoa_don):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO HoaDon (khachhang_id, so_phong, tienphong, tiendien, tiennuoc, ngay_thanh_toan, thang_thanh_toan, thang_hoa_don) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (khachhang_id, so_phong, tienphong, tiendien, tiennuoc, ngay_thanh_toan, thang_thanh_toan, thang_hoa_don))
        conn.commit()
        print("Hóa đơn đã được thêm thành công.")
    except sqlite3.Error as e:
        print("Lỗi khi thêm hóa đơn:", e)
        conn.rollback()
    finally:
        conn.close()

def select_all_khachhang():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM KhachHang")
    rows = cursor.fetchall()
    conn.close()
    return rows

def select_khachhang_by_id(khachhang_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM KhachHang WHERE khachhang_id=?", (khachhang_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def select_all_giadiennuoc():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GiaDienNuoc")
    rows = cursor.fetchall()
    conn.close()
    return rows

def select_giadiennuoc_by_id(gia_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GiaDienNuoc WHERE gia_id=?", (gia_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def select_all_phong():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Phong")
    rows = cursor.fetchall()
    conn.close()
    return rows

def select_phong_by_id(so_phong):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Phong WHERE so_phong=?", (so_phong,))
    row = cursor.fetchone()
    conn.close()
    return row

def select_all_hoadon():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM HoaDon")
    rows = cursor.fetchall()
    conn.close()
    return rows

def select_hoadon_by_id(hoadon_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM HoaDon WHERE hoadon_id=?", (hoadon_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def update_khachhang(khachhang_id, ho_ten, cccd, sdt):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("UPDATE KhachHang SET ho_ten=?, cccd=?, sdt=? WHERE khachhang_id=?", (ho_ten, cccd, sdt, khachhang_id))
    conn.commit()
    conn.close()

def update_giadiennuoc(gia_id, giadien, gianuoc):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("UPDATE GiaDienNuoc SET giadien=?, gianuoc=? WHERE gia_id=?", (giadien, gianuoc, gia_id))
    conn.commit()
    conn.close()

def update_ngay_thang_thanh_toan_by_sophong(so_phong, new_ngay_thanh_toan, new_thang_thanh_toan, new_thang_hoa_don):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute("UPDATE HoaDon SET ngay_thanh_toan=?, thang_thanh_toan=?, thang_hoa_don=? WHERE so_phong=?", 
                       (new_ngay_thanh_toan, new_thang_thanh_toan, new_thang_hoa_don, so_phong))
        conn.commit()
        print("Cập nhật thành công.")
    except sqlite3.Error as e:
        print("Lỗi khi cập nhật:", e)
        conn.rollback()
    finally:
        conn.close()

def update_phong(so_phong, gia_tien, khachhang_id=None):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        if khachhang_id is not None:
            # Update both gia_tien and khachhang_id for the Phong
            cursor.execute("UPDATE Phong SET gia_tien=?, khachhang_id=? WHERE so_phong=?", (gia_tien, khachhang_id, so_phong))
        else:
            # Update only gia_tien for the Phong
            cursor.execute("UPDATE Phong SET gia_tien=? WHERE so_phong=?", (gia_tien, so_phong))

        # Commit the changes
        conn.commit()
        print("Updated Phong successfully.")
    except sqlite3.Error as e:
        print("Error while updating Phong:", e)
    finally:
        # Close the connection
        conn.close()

def update_data(khachhang_id, so_phong, new_gia_tien, new_ho_ten, new_cccd, new_sdt):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        conn.execute("BEGIN TRANSACTION")  # Bắt đầu transaktion

        # Cập nhật thông tin trong bảng KhachHang
        cursor.execute("UPDATE KhachHang SET ho_ten=?, cccd=?, sdt=? WHERE khachhang_id=?", (new_ho_ten, new_cccd, new_sdt, khachhang_id))

        # Cập nhật thông tin trong bảng Phong
        cursor.execute("UPDATE Phong SET gia_tien=?, so_phong=? WHERE khachhang_id=?", (new_gia_tien, so_phong, khachhang_id))

        # Cập nhật thông tin trong bảng HoaDon
        cursor.execute("UPDATE HoaDon SET khachhang_id=?, tienphong=? WHERE khachhang_id=?", (khachhang_id, new_gia_tien, khachhang_id))

        conn.execute("COMMIT")  # Kết thúc transaktion và thực hiện thay đổi

        print("Updated data successfully.")
    except sqlite3.Error as e:
        print("Error while updating data:", e)
        conn.execute("ROLLBACK")  # Hoàn tác transaktion nếu có lỗi
    finally:
        conn.close()

def update_hoadon_by_sophong(so_phong, new_tienphong, new_tiendien, new_tiennuoc, new_ngay_thanh_toan, new_thang_thanh_toan):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("UPDATE HoaDon SET tienphong=?, tiendien=?, tiennuoc=?, ngay_thanh_toan=?, thang_thanh_toan=? WHERE so_phong=?", 
                       (new_tienphong, new_tiendien, new_tiennuoc, new_ngay_thanh_toan, new_thang_thanh_toan, so_phong))

        conn.commit()
        print("Updated HoaDon successfully.")
    except sqlite3.Error as e:
        print("Error while updating HoaDon:", e)
    finally:
        conn.close()

def update_hoadon(hoadon_id, khachhang_id, so_phong, tienphong, tiendien, tiennuoc, ngay_thanh_toan, thang_thanh_toan, thang_hoa_don):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("UPDATE HoaDon SET khachhang_id=?, so_phong=?, tienphong=?, tiendien=?, tiennuoc=?, ngay_thanh_toan=?, thang_thanh_toan=?, thang_hoa_don=? WHERE hoadon_id=?",
                   (khachhang_id, so_phong, tienphong, tiendien, tiennuoc, ngay_thanh_toan, thang_thanh_toan, thang_hoa_don, hoadon_id))
    conn.commit()
    conn.close()

def delete_khachhang(khachhang_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM KhachHang WHERE khachhang_id=?", (khachhang_id,))
    conn.commit()
    conn.close()

def delete_giadiennuoc(gia_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM GiaDienNuoc WHERE gia_id=?", (gia_id,))
    conn.commit()
    conn.close()

def delete_phong(so_phong):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Phong WHERE so_phong=?", (so_phong,))
    conn.commit()
    conn.close()

def delete_hoadon_by_id(hoadon_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM HoaDon WHERE hoadon_id=?", (hoadon_id,))
    conn.commit()
    conn.close()

def delete_hoadon(khachhang_id, so_phong, tienphong, tiendien, tiennuoc, ngay_thanh_toan, thang_thanh_toan, thang_hoa_don):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM HoaDon WHERE khachhang_id=? AND so_phong=? AND tienphong=? AND tiendien=? AND tiennuoc=? AND ngay_thanh_toan=? AND thang_thanh_toan=? AND thang_hoa_don=?",
                   (khachhang_id, so_phong, tienphong, tiendien, tiennuoc, ngay_thanh_toan, thang_thanh_toan, thang_hoa_don))
    connection.commit()
    connection.close()

def delete_hoadon_by_so_phong(so_phong):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM HoaDon WHERE so_phong=?", (so_phong,))

    conn.commit()
    conn.close()

def delete_customer_with_related_info(khachhang_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        # Lấy thông tin về phòng của khách hàng
        cursor.execute("SELECT so_phong FROM Phong WHERE khachhang_id=?", (khachhang_id,))
        phong_info = cursor.fetchone()

        if phong_info:
            so_phong = phong_info[0]

            # Xoá các hoá đơn liên quan
            cursor.execute("DELETE FROM HoaDon WHERE khachhang_id=?", (khachhang_id,))

            # Xoá thông tin về phòng
            cursor.execute("DELETE FROM Phong WHERE khachhang_id=?", (khachhang_id,))

            # Xoá KhachHang
            cursor.execute("DELETE FROM KhachHang WHERE khachhang_id=?", (khachhang_id,))

            # Lưu các thay đổi vào cơ sở dữ liệu
            conn.commit()
            print(f"Đã xoá thông tin liên quan đến KhachHang và Phong {so_phong} thành công.")
        else:
            print("Không tìm thấy thông tin về phòng của KhachHang.")
    except sqlite3.Error as e:
        print("Lỗi trong quá trình xoá dữ liệu:", e)
    finally:
        # Đóng kết nối
        conn.close()

def get_hoadon_by_so_phong(so_phong):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM HoaDon WHERE so_phong=? ORDER BY ngay_thanh_toan", (so_phong,))
    hoadon_list = cursor.fetchall()

    conn.close()
    return hoadon_list

def get_latest_giadiennuoc_id():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch the latest gia_id from GiaDienNuoc table
    cursor.execute("SELECT gia_id FROM GiaDienNuoc ORDER BY gia_id DESC LIMIT 1")
    latest_giadiennuoc_id = cursor.fetchone()

    conn.close()

    # Return the latest gia_id (or None if the table is empty)
    return latest_giadiennuoc_id[0] if latest_giadiennuoc_id else None

def get_thangthanhtoan_by_sophong(sophong):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT thang_thanh_toan FROM ThangThanhToan WHERE so_phong=?", (sophong,))
        thangthanhtoan_list = [row[0] for row in cursor.fetchall()]
        return thangthanhtoan_list
    except sqlite3.Error as e:
        print("Error while getting ThangThanhToan:", e)
        return []

def get_customer_info_by_phong(so_phong):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch the khachhang_id associated with the given so_phong in Phong table
    cursor.execute("SELECT khachhang_id FROM Phong WHERE so_phong=?", (so_phong,))
    khachhang_id = cursor.fetchone()

    customer_info = None
    if khachhang_id:
        # Fetch all columns of the corresponding khachhang_id from KhachHang table
        cursor.execute("SELECT * FROM KhachHang WHERE khachhang_id=?", (khachhang_id[0],))
        customer_info = cursor.fetchone()

    conn.close()
    return customer_info

def check_phong_has_khachhang(so_phong):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch khachhang_id associated with the given so_phong in Phong table
    cursor.execute("SELECT khachhang_id FROM Phong WHERE so_phong=?", (so_phong,))
    khachhang_id = cursor.fetchone()

    # If khachhang_id exists and is not None, check if it is associated with a valid KhachHang
    if khachhang_id is not None:
        cursor.execute("SELECT khachhang_id FROM KhachHang WHERE khachhang_id=?", (khachhang_id[0],))
        exists = cursor.fetchone() is not None
    else:
        exists = False

    conn.close()

    # Return True if the khachhang_id exists and is associated with a valid KhachHang
    return exists


def get_all_so_phong():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execute the SQL query to fetch all so_phong from Phong table
    cursor.execute("SELECT so_phong FROM Phong")
    so_phong_list = [row[0] for row in cursor.fetchall()]

    conn.close()

    return so_phong_list

def get_hoadon_by_so_phong(so_phong):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch hoa don information associated with the given so_phong in HoaDon table
    cursor.execute("SELECT * FROM HoaDon WHERE so_phong=?", (so_phong,))
    hoadon_info = cursor.fetchall()

    conn.close()
    return hoadon_info

def get_latest_customer_info():

    try:
        # Thực hiện truy vấn SQL để lấy thông tin mới nhất của khách hàng
        cursor.execute("SELECT * FROM KhachHang ORDER BY khachhang_id DESC LIMIT 1")
        latest_customer = cursor.fetchone()

        return latest_customer

    except Exception as e:
        print("Lỗi khi lấy thông tin khách hàng:", str(e))

    finally:
        conn.close()

def get_hoadon_id_by_sophong(so_phong):
    conn = sqlite3.connect(db_path)  # Thay db_path bằng đường dẫn đến cơ sở dữ liệu của bạn
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT hoadon_id FROM HoaDon WHERE so_phong=?", (so_phong,))
        hoadon_ids = [row[0] for row in cursor.fetchall()]
        return hoadon_ids
    except sqlite3.Error as e:
        print("Error while fetching HoaDon IDs:", e)
        return []

    finally:
        conn.close()



#create_database()
#insert_giadiennuoc(5000, 10000)
#insert_khachhang("Lý Quốc An", "3425213342134", "32454562134")
#insert_khachhang("Phạm Quang Dinh", "111111", "222222")

#insert_phong(1, 1000)
#insert_phong(2, 999999, 1)
#insert_phong(3, 1000)
#insert_phong(4, 1000, 2)
#update_phong(101, 9913213, 1)
#insert_hoadon(3, 4, 2221111132135, 888123213213888, 71232137, "21/12/2023", 12)



#print(get_hoadon_by_so_phong(4))
#print(get_latest_customer_info())




#all_phong = select_all_phong()
#print(all_phong)

#all_khachhang = select_all_khachhang()
#print(all_khachhang)


#all_hoadon = select_all_hoadon()
#print(all_hoadon)


#print(get_hoadon_id_by_sophong(5))
#update_hoadon(2, 2, 4, 1000, 440000, 615000, '14/12/2008', 0)

#khachhang = select_all_khachhang()
#print(khachhang)
#phong = select_phong_by_id(101)
#print(get_customer_info_by_phong(3))
#update_phong(3, 999, 3)
#print(phong)
#print(get_customer_info_by_phong(101))
#delete_phong(103)

#phong_102_has_khachhang = check_phong_has_khachhang(101)
#print("Phong 102 has khachhang:", phong_102_has_khachhang)

#current_price = get_latest_giadiennuoc_id()
#giadien = select_giadiennuoc_by_id(current_price)

#laygia = select_all_giadiennuoc()
#print(laygia)
#print(get_latest_giadiennuoc_id())


=======
import sqlite3

db_path = "khach_tro.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

def create_database():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Drop existing tables (if they exist)
    cursor.executescript('''
        DROP TABLE IF EXISTS HoaDon;
        DROP TABLE IF EXISTS Phong;
        DROP TABLE IF EXISTS GiaDienNuoc;
        DROP TABLE IF EXISTS KhachHang;
    ''')

    # Creating the tables
    cursor.executescript('''
        CREATE TABLE KhachHang (
            khachhang_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ho_ten TEXT NOT NULL,
            cccd TEXT NOT NULL,
            sdt TEXT NOT NULL
        );

        CREATE TABLE GiaDienNuoc (
            gia_id INTEGER PRIMARY KEY AUTOINCREMENT,
            giadien INTEGER NOT NULL,
            gianuoc INTEGER NOT NULL
        );

        CREATE TABLE Phong (
            so_phong INTEGER PRIMARY KEY,
            gia_tien INTEGER NOT NULL,
            khachhang_id INTEGER,
            FOREIGN KEY (khachhang_id) REFERENCES KhachHang (khachhang_id)         
        );

        CREATE TABLE HoaDon (
            hoadon_id INTEGER PRIMARY KEY AUTOINCREMENT,
            khachhang_id INTEGER NOT NULL,
            so_phong INTEGER NOT NULL,
            tienphong INTEGER NOT NULL,
            tiendien INTEGER NOT NULL,
            tiennuoc INTEGER NOT NULL,
            ngay_thanh_toan TEXT NOT NULL,
            thang_thanh_toan BOOLEAN NOT NULL,
            thang_hoa_don INTEGER NOT NULL,
            FOREIGN KEY (khachhang_id) REFERENCES KhachHang (khachhang_id),
            FOREIGN KEY (so_phong) REFERENCES Phong (so_phong)
        );
    ''')

    conn.commit()
    conn.close()




# CURD
def insert_khachhang(ho_ten, cccd, sdt):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO KhachHang (ho_ten, cccd, sdt) VALUES (?, ?, ?)", (ho_ten, cccd, sdt))
    conn.commit()
    conn.close()

def insert_giadiennuoc(giadien, gianuoc):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO GiaDienNuoc (giadien, gianuoc) VALUES (?, ?)", (giadien, gianuoc))
    conn.commit()
    conn.close()

def insert_khachhang2(ho_ten, cccd, sdt):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO KhachHang (ho_ten, cccd, sdt) VALUES (?, ?, ?)", (ho_ten, cccd, sdt))
    conn.commit()

    # Lấy ID của khách hàng vừa thêm
    cursor.execute("SELECT last_insert_rowid()")
    khachhang_id = cursor.fetchone()[0]

    conn.close()
    return khachhang_id

def insert_phong(so_phong, gia_tien, khachhang_id=None):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Phong (so_phong, gia_tien, khachhang_id) VALUES (?, ?, ?)", (so_phong, gia_tien, khachhang_id))
    conn.commit()
    conn.close()

def insert_hoadon(khachhang_id, so_phong, tienphong, tiendien, tiennuoc, ngay_thanh_toan, thang_thanh_toan, thang_hoa_don):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO HoaDon (khachhang_id, so_phong, tienphong, tiendien, tiennuoc, ngay_thanh_toan, thang_thanh_toan, thang_hoa_don) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (khachhang_id, so_phong, tienphong, tiendien, tiennuoc, ngay_thanh_toan, thang_thanh_toan, thang_hoa_don))
        conn.commit()
        print("Hóa đơn đã được thêm thành công.")
    except sqlite3.Error as e:
        print("Lỗi khi thêm hóa đơn:", e)
        conn.rollback()
    finally:
        conn.close()

def select_all_khachhang():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM KhachHang")
    rows = cursor.fetchall()
    conn.close()
    return rows

def select_khachhang_by_id(khachhang_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM KhachHang WHERE khachhang_id=?", (khachhang_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def select_all_giadiennuoc():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GiaDienNuoc")
    rows = cursor.fetchall()
    conn.close()
    return rows

def select_giadiennuoc_by_id(gia_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GiaDienNuoc WHERE gia_id=?", (gia_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def select_all_phong():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Phong")
    rows = cursor.fetchall()
    conn.close()
    return rows

def select_phong_by_id(so_phong):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Phong WHERE so_phong=?", (so_phong,))
    row = cursor.fetchone()
    conn.close()
    return row

def select_all_hoadon():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM HoaDon")
    rows = cursor.fetchall()
    conn.close()
    return rows

def select_hoadon_by_id(hoadon_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM HoaDon WHERE hoadon_id=?", (hoadon_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def update_khachhang(khachhang_id, ho_ten, cccd, sdt):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("UPDATE KhachHang SET ho_ten=?, cccd=?, sdt=? WHERE khachhang_id=?", (ho_ten, cccd, sdt, khachhang_id))
    conn.commit()
    conn.close()

def update_giadiennuoc(gia_id, giadien, gianuoc):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("UPDATE GiaDienNuoc SET giadien=?, gianuoc=? WHERE gia_id=?", (giadien, gianuoc, gia_id))
    conn.commit()
    conn.close()

def update_ngay_thang_thanh_toan_by_sophong(so_phong, new_ngay_thanh_toan, new_thang_thanh_toan, new_thang_hoa_don):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute("UPDATE HoaDon SET ngay_thanh_toan=?, thang_thanh_toan=?, thang_hoa_don=? WHERE so_phong=?", 
                       (new_ngay_thanh_toan, new_thang_thanh_toan, new_thang_hoa_don, so_phong))
        conn.commit()
        print("Cập nhật thành công.")
    except sqlite3.Error as e:
        print("Lỗi khi cập nhật:", e)
        conn.rollback()
    finally:
        conn.close()

def update_phong(so_phong, gia_tien, khachhang_id=None):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        if khachhang_id is not None:
            # Update both gia_tien and khachhang_id for the Phong
            cursor.execute("UPDATE Phong SET gia_tien=?, khachhang_id=? WHERE so_phong=?", (gia_tien, khachhang_id, so_phong))
        else:
            # Update only gia_tien for the Phong
            cursor.execute("UPDATE Phong SET gia_tien=? WHERE so_phong=?", (gia_tien, so_phong))

        # Commit the changes
        conn.commit()
        print("Updated Phong successfully.")
    except sqlite3.Error as e:
        print("Error while updating Phong:", e)
    finally:
        # Close the connection
        conn.close()

def update_data(khachhang_id, so_phong, new_gia_tien, new_ho_ten, new_cccd, new_sdt):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        conn.execute("BEGIN TRANSACTION")  # Bắt đầu transaktion

        # Cập nhật thông tin trong bảng KhachHang
        cursor.execute("UPDATE KhachHang SET ho_ten=?, cccd=?, sdt=? WHERE khachhang_id=?", (new_ho_ten, new_cccd, new_sdt, khachhang_id))

        # Cập nhật thông tin trong bảng Phong
        cursor.execute("UPDATE Phong SET gia_tien=?, so_phong=? WHERE khachhang_id=?", (new_gia_tien, so_phong, khachhang_id))

        # Cập nhật thông tin trong bảng HoaDon
        cursor.execute("UPDATE HoaDon SET khachhang_id=?, tienphong=? WHERE khachhang_id=?", (khachhang_id, new_gia_tien, khachhang_id))

        conn.execute("COMMIT")  # Kết thúc transaktion và thực hiện thay đổi

        print("Updated data successfully.")
    except sqlite3.Error as e:
        print("Error while updating data:", e)
        conn.execute("ROLLBACK")  # Hoàn tác transaktion nếu có lỗi
    finally:
        conn.close()

def update_hoadon_by_sophong(so_phong, new_tienphong, new_tiendien, new_tiennuoc, new_ngay_thanh_toan, new_thang_thanh_toan):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("UPDATE HoaDon SET tienphong=?, tiendien=?, tiennuoc=?, ngay_thanh_toan=?, thang_thanh_toan=? WHERE so_phong=?", 
                       (new_tienphong, new_tiendien, new_tiennuoc, new_ngay_thanh_toan, new_thang_thanh_toan, so_phong))

        conn.commit()
        print("Updated HoaDon successfully.")
    except sqlite3.Error as e:
        print("Error while updating HoaDon:", e)
    finally:
        conn.close()

def update_hoadon(hoadon_id, khachhang_id, so_phong, tienphong, tiendien, tiennuoc, ngay_thanh_toan, thang_thanh_toan, thang_hoa_don):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("UPDATE HoaDon SET khachhang_id=?, so_phong=?, tienphong=?, tiendien=?, tiennuoc=?, ngay_thanh_toan=?, thang_thanh_toan=?, thang_hoa_don=? WHERE hoadon_id=?",
                   (khachhang_id, so_phong, tienphong, tiendien, tiennuoc, ngay_thanh_toan, thang_thanh_toan, thang_hoa_don, hoadon_id))
    conn.commit()
    conn.close()

def delete_khachhang(khachhang_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM KhachHang WHERE khachhang_id=?", (khachhang_id,))
    conn.commit()
    conn.close()

def delete_giadiennuoc(gia_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM GiaDienNuoc WHERE gia_id=?", (gia_id,))
    conn.commit()
    conn.close()

def delete_phong(so_phong):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Phong WHERE so_phong=?", (so_phong,))
    conn.commit()
    conn.close()

def delete_hoadon_by_id(hoadon_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM HoaDon WHERE hoadon_id=?", (hoadon_id,))
    conn.commit()
    conn.close()

def delete_hoadon(khachhang_id, so_phong, tienphong, tiendien, tiennuoc, ngay_thanh_toan, thang_thanh_toan, thang_hoa_don):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM HoaDon WHERE khachhang_id=? AND so_phong=? AND tienphong=? AND tiendien=? AND tiennuoc=? AND ngay_thanh_toan=? AND thang_thanh_toan=? AND thang_hoa_don=?",
                   (khachhang_id, so_phong, tienphong, tiendien, tiennuoc, ngay_thanh_toan, thang_thanh_toan, thang_hoa_don))
    connection.commit()
    connection.close()

def delete_hoadon_by_so_phong(so_phong):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM HoaDon WHERE so_phong=?", (so_phong,))

    conn.commit()
    conn.close()

def delete_customer_with_related_info(khachhang_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        # Lấy thông tin về phòng của khách hàng
        cursor.execute("SELECT so_phong FROM Phong WHERE khachhang_id=?", (khachhang_id,))
        phong_info = cursor.fetchone()

        if phong_info:
            so_phong = phong_info[0]

            # Xoá các hoá đơn liên quan
            cursor.execute("DELETE FROM HoaDon WHERE khachhang_id=?", (khachhang_id,))

            # Xoá thông tin về phòng
            cursor.execute("DELETE FROM Phong WHERE khachhang_id=?", (khachhang_id,))

            # Xoá KhachHang
            cursor.execute("DELETE FROM KhachHang WHERE khachhang_id=?", (khachhang_id,))

            # Lưu các thay đổi vào cơ sở dữ liệu
            conn.commit()
            print(f"Đã xoá thông tin liên quan đến KhachHang và Phong {so_phong} thành công.")
        else:
            print("Không tìm thấy thông tin về phòng của KhachHang.")
    except sqlite3.Error as e:
        print("Lỗi trong quá trình xoá dữ liệu:", e)
    finally:
        # Đóng kết nối
        conn.close()

def get_hoadon_by_so_phong(so_phong):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM HoaDon WHERE so_phong=? ORDER BY ngay_thanh_toan", (so_phong,))
    hoadon_list = cursor.fetchall()

    conn.close()
    return hoadon_list

def get_latest_giadiennuoc_id():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch the latest gia_id from GiaDienNuoc table
    cursor.execute("SELECT gia_id FROM GiaDienNuoc ORDER BY gia_id DESC LIMIT 1")
    latest_giadiennuoc_id = cursor.fetchone()

    conn.close()

    # Return the latest gia_id (or None if the table is empty)
    return latest_giadiennuoc_id[0] if latest_giadiennuoc_id else None

def get_thangthanhtoan_by_sophong(sophong):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT thang_thanh_toan FROM ThangThanhToan WHERE so_phong=?", (sophong,))
        thangthanhtoan_list = [row[0] for row in cursor.fetchall()]
        return thangthanhtoan_list
    except sqlite3.Error as e:
        print("Error while getting ThangThanhToan:", e)
        return []

def get_customer_info_by_phong(so_phong):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch the khachhang_id associated with the given so_phong in Phong table
    cursor.execute("SELECT khachhang_id FROM Phong WHERE so_phong=?", (so_phong,))
    khachhang_id = cursor.fetchone()

    customer_info = None
    if khachhang_id:
        # Fetch all columns of the corresponding khachhang_id from KhachHang table
        cursor.execute("SELECT * FROM KhachHang WHERE khachhang_id=?", (khachhang_id[0],))
        customer_info = cursor.fetchone()

    conn.close()
    return customer_info

def check_phong_has_khachhang(so_phong):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch khachhang_id associated with the given so_phong in Phong table
    cursor.execute("SELECT khachhang_id FROM Phong WHERE so_phong=?", (so_phong,))
    khachhang_id = cursor.fetchone()

    # If khachhang_id exists and is not None, check if it is associated with a valid KhachHang
    if khachhang_id is not None:
        cursor.execute("SELECT khachhang_id FROM KhachHang WHERE khachhang_id=?", (khachhang_id[0],))
        exists = cursor.fetchone() is not None
    else:
        exists = False

    conn.close()

    # Return True if the khachhang_id exists and is associated with a valid KhachHang
    return exists


def get_all_so_phong():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execute the SQL query to fetch all so_phong from Phong table
    cursor.execute("SELECT so_phong FROM Phong")
    so_phong_list = [row[0] for row in cursor.fetchall()]

    conn.close()

    return so_phong_list

def get_hoadon_by_so_phong(so_phong):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch hoa don information associated with the given so_phong in HoaDon table
    cursor.execute("SELECT * FROM HoaDon WHERE so_phong=?", (so_phong,))
    hoadon_info = cursor.fetchall()

    conn.close()
    return hoadon_info

def get_latest_customer_info():

    try:
        # Thực hiện truy vấn SQL để lấy thông tin mới nhất của khách hàng
        cursor.execute("SELECT * FROM KhachHang ORDER BY khachhang_id DESC LIMIT 1")
        latest_customer = cursor.fetchone()

        return latest_customer

    except Exception as e:
        print("Lỗi khi lấy thông tin khách hàng:", str(e))

    finally:
        conn.close()

def get_hoadon_id_by_sophong(so_phong):
    conn = sqlite3.connect(db_path)  # Thay db_path bằng đường dẫn đến cơ sở dữ liệu của bạn
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT hoadon_id FROM HoaDon WHERE so_phong=?", (so_phong,))
        hoadon_ids = [row[0] for row in cursor.fetchall()]
        return hoadon_ids
    except sqlite3.Error as e:
        print("Error while fetching HoaDon IDs:", e)
        return []

    finally:
        conn.close()



#create_database()
#insert_giadiennuoc(5000, 10000)
#insert_khachhang("Lý Quốc An", "3425213342134", "32454562134")
#insert_khachhang("Phạm Quang Dinh", "111111", "222222")

#insert_phong(1, 1000)
#insert_phong(2, 999999, 1)
#insert_phong(3, 1000)
#insert_phong(4, 1000, 2)
#update_phong(101, 9913213, 1)
#insert_hoadon(3, 4, 2221111132135, 888123213213888, 71232137, "21/12/2023", 12)



#print(get_hoadon_by_so_phong(4))
#print(get_latest_customer_info())




#all_phong = select_all_phong()
#print(all_phong)

#all_khachhang = select_all_khachhang()
#print(all_khachhang)


#all_hoadon = select_all_hoadon()
#print(all_hoadon)


#print(get_hoadon_id_by_sophong(5))
#update_hoadon(2, 2, 4, 1000, 440000, 615000, '14/12/2008', 0)

#khachhang = select_all_khachhang()
#print(khachhang)
#phong = select_phong_by_id(101)
#print(get_customer_info_by_phong(3))
#update_phong(3, 999, 3)
#print(phong)
#print(get_customer_info_by_phong(101))
#delete_phong(103)

#phong_102_has_khachhang = check_phong_has_khachhang(101)
#print("Phong 102 has khachhang:", phong_102_has_khachhang)

#current_price = get_latest_giadiennuoc_id()
#giadien = select_giadiennuoc_by_id(current_price)

#laygia = select_all_giadiennuoc()
#print(laygia)
#print(get_latest_giadiennuoc_id())


>>>>>>> 2980f569ef0d68128605192c6fa4df3f5808ad73
