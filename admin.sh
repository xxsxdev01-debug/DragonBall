import os
import subprocess
import mysql.connector as mysql
from datetime import datetime

# Hệ thống màu sắc Bold
R, G, Y, B, P, C, W, X = '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;37m', '\033[0m'

def Clrscr():
    subprocess.run('clear', shell=True)

def Show_Success(action, old_v, new_v):
    """Hiển thị thông báo kết quả chi tiết"""
    print(f"\n{C}┌──────────────────────────────────────────────────┐")
    print(f"{C}│ {G}✔ Thành Công: {W}{action:30} {C}│")
    print(f"{C}│ {W}Thay Đổi: {R}{old_v:,} {G}➜ {Y}{new_v:,}{X} {C}│")
    print(f"{C}└──────────────────────────────────────────────────┘{X}")
    os.system('sleep 2')

def main():
    try:
        # Kết nối Database từ mã nguồn gốc
        conn = mysql.connect(host='localhost', user='root', password='', database='dragonball')
        cursor = conn.cursor()
    except:
        print(f"{R}[!] Lỗi Kết Nối Cơ Sở Dữ Liệu{X}")
        return

    while True:
        Clrscr()
        print(f"{C}┌──────────────────────────────────────────────────┐")
        print(f"{C}│{Y}        Quản Trị Viên Ngọc Rồng Online            {C}│")
        print(f"{C}└──────────────────────────────────────────────────┘{X}")
        
        # Lấy danh sách tài khoản
        cursor.execute('SELECT account_id, name FROM player')
        print(f"{B} ID Tài Khoản      Tên Nhân Vật{X}")
        print(f"{W} ─────────────      ─────────────{X}")
        for id, name in cursor:
            print(f" {B}[{W}{id:^5}{B}] {G}➜ {W}{name}")
        
        try:
            row_id = int(input(f"\n{Y}➜ Nhập ID Tài Khoản: {W}"))
        except: continue

        # Truy vấn dữ liệu từ player
        cursor.execute('SELECT data_point, data_task, data_inventory FROM player WHERE account_id = %s', (row_id,))
        res = cursor.fetchone()
        if not res: continue

        # Giải mã các mảng dữ liệu
        points = eval(res[0])
        tasks = eval(res[1])
        items = eval(res[2])

        Clrscr()
        print(f"{C}┌── {Y}Menu Chỉnh Sửa Chỉ Số Player: {G}{row_id} {C}──────────────────┐{X}")
        print(f" {C}[01] {W}Tiềm Năng: {G}{points[1]:,}")
        print(f" {C}[02] {W}Hp: {G}{points[2]:,}") 
        print(f" {C}[03] {W}Hp: {G}{points[5]:,}")
        print(f" {C}[04] {W}Ki: {G}{points[6]:,}")
        print(f" {C}[05] {W}Sức Đánh             : {G}{points[7]:,}")
        print(f" {C}[06] {W}Giáp                 : {G}{points[8]:,}")
        print(f" {C}[07] {W}Chí Mạng             : {G}{points[9]}%")
        
        # Danh sách nhiệm vụ
        task_list = [
            'Nhiệm Vụ Đầu Tiên', 'Nhiệm Vụ Tập Luyện', 'Nhiệm Vụ Tìm Thức Ăn', 'Tìm Kiếm Sao Băng',
            'Nhiệm Vụ Khó Khăn', 'Nhiệm Vụ Gia Tăng Sức Mạnh', 'Nhiệm Vụ Trò Chuyện', 'Nhiệm Vụ Giải Cứu',
            'Nhiệm Vụ Ân Nhân Xuất Sắc', 'Nhiệm Vụ Tiên Học Lễ', 'Nhiệm Vụ Học Phí', 'Nhiệm Vụ Kết Giao',
            'Nhiệm Vụ Xin Phép', 'Nhiệm Vụ Gia Nhập Bang Hội', 'Nhiệm Vụ Bang Hội Lần 1', 'Nhiệm Vụ Bang Hội Lần 2',
            'Tiêu Diệt Quái Vật', 'Nhiệm Vụ Giúp Đỡ Cui', 'Nhiệm Vụ Bất Khả Thi', 'Nhiệm Vụ Chạm Trán Đệ Tử',
            'Nhiệm Vụ Tiểu Đội Sát Thủ', 'Nhiệm Vụ Chạm Trán Fide Đại Ca', 'Nhiệm Vụ Chạm Trán Rôbốt Sát Thủ Lần 1',
            'Nhiệm Vụ Chạm Trán Rôbốt Sát Thủ Lần 2', 'Nhiệm Vụ Giải Cứu Thị Trấn Ginder', 'Tiêu Diệt Xên Đi Mấy Em',
            'Tiêu Diệt Xên Đi Mấy Em', 'Kết Bạn Nhiều Niềm Vui', 'Săn Xên Bên Võ Đài Nhé', 'Qua Cold Nhé',
            'Pem Chết Cụ Tụi Doraemon Đi', 'Nhiệm Vụ Hơi Khó', 'Đã Hoàn Thành Hết Nhiệm Vụ'
        ]
        print(f" {C}[06] {W}Nhiệm Vụ Hiện Tại    : {P}{task_list[tasks[0]]}")
        print(f" {C}[07] {W}Vàng                 : {Y}{items[0]:,}")
        print(f" {C}[08] {W}Ngọc Xanh            : {G}{items[1]:,}")
        print(f" {C}[09] {W}Hồng Ngọc            : {R}{items[2]:,}")
        
        # Kiểm tra Admin
        cursor.execute('SELECT is_admin FROM account WHERE id = %s', (row_id,))
        is_admin = cursor.fetchone()[0]
        status = "Có" if is_admin == 1 else "Không"
        print(f" {C}[10] {W}Quyền Admin          : {G if is_admin==1 else R}{status}")
        print(f"{C}└──────────────────────────────────────────────────┘{X}")
        
        choose = input(f"{Y}➜ Nhập Lựa Chọn: {W}")

        if choose == '1':
            old = points[1]
            new_val = int(input(f"{G}➜ Nhập Sức Mạnh Mới: {W}"))
            points[1] = points[2] = new_val
            cursor.execute('UPDATE player SET data_point = %s WHERE account_id = %s', (str(points), row_id))
            conn.commit()
            Show_Success("Chỉnh Sức Mạnh", old, new_val)

        elif choose == '2':
            old = points[5]
            new_val = int(input(f"{G}➜ Nhập Hp, Ki Mới: {W}"))
            points[5] = points[6] = new_val
            cursor.execute('UPDATE player SET data_point = %s WHERE account_id = %s', (str(points), row_id))
            conn.commit()
            Show_Success("Chỉnh Hp Và Ki", old, new_val)

        elif choose == '7':
            old = items[0]
            new_val = int(input(f"{Y}➜ Nhập Số Vàng Mới: {W}"))
            items[0] = new_val
            cursor.execute('UPDATE player SET data_inventory = %s WHERE account_id = %s', (str(items), row_id))
            conn.commit()
            Show_Success("Chỉnh Số Vàng", old, new_val)

        elif choose == '8':
            old = items[1]
            new_val = int(input(f"{G}➜ Nhập Số Ngọc Mới: {W}"))
            items[1] = new_val
            cursor.execute('UPDATE player SET data_inventory = %s WHERE account_id = %s', (str(items), row_id))
            conn.commit()
            Show_Success("Chỉnh Ngọc Xanh", old, new_val)

        elif choose == '10':
            old_s = "Admin" if is_admin == 1 else "User"
            new_val = int(input(f"{W}➜ Quyền Admin (1: Có, 0: Không): {W}"))
            cursor.execute('UPDATE account SET is_admin = %s WHERE id = %s', (new_val, row_id))
            conn.commit()
            print(f"{G}✔ Đã Thay Đổi Quyền Admin Thành Công!{X}")
            os.system('sleep 2')

        elif choose == '':
            break

if __name__ == "__main__":
    main()
