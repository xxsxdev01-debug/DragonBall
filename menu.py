import os
import time

def clear_screen():
    os.system('clear')

def menu_display():
    clear_screen()
    print("\033[1;32m===============================================")
    print("      MENU QUẢN TRỊ DRAGONBALL - TERMUX        ")
    print("===============================================\033[0m")
    print(" [1]. Khởi động Server Game (Java)")
    print(" [2]. Bật Cơ sở dữ liệu (MySQL/KSWEB)")
    print(" [3]. Chỉnh sửa tài khoản người dùng")
    print(" [4]. Xem Log hoạt động hệ thống")
    print(" [5]. Cập nhật mã nguồn mới nhất")
    print(" [0]. Thoát Tool")
    print("\033[1;32m-----------------------------------------------\033[0m")

def start_server():
    print("\033[1;33m[i] Đang khởi động Server Java...\033[0m")
    time.sleep(2)
    print("\033[1;32m[+] Server đã sẵn sàng!\033[0m")
    input("\nNhấn Enter để quay lại Menu...")

def main():
    while True:
        menu_display()
        choice = input("\033[1;36m➤ Nhập lựa chọn của bạn: \033[0m")
        if choice == '1':
            start_server()
        elif choice == '0':
            print("Đang thoát...")
            break
        else:
            print("\033[1;31m[!] Lựa chọn không hợp lệ!\033[0m")
            time.sleep(1)

# QUAN TRỌNG: Dòng này giúp tool tự bật Menu ngay khi tải về
if __name__ == "__main__":
    main()
