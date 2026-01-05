import os
import time

def clear_screen():
    os.system('clear')

def menu_display():
    clear_screen()
    # Giao diện DEBUG NULL với khung viền kép đúng mẫu của bạn
    print("\033[1;31m+═══════════════════════════════════════════════════════+")
    print("║  ____  _____ ____  _   _  ____     _   _ _   _ _      ║")
    print("║ |  _ \| ____| __ )| | | |/ ___|   | \ | | | | | |     ║")
    print("║ | | | |  _| |  _ \| | | | |  _    |  \| | | | | |     ║")
    print("║ | |_| | |___| |_) | |_| | |_| |   | |\  | |_| | |___  ║")
    print("║ |____/|_____|____/ \___/ \____|   |_| \_|\___/|_____| ║")
    print("║                                                       ║")
    print("║  Dev: Debug Null                                      ║")
    print("║  Zalo: 0899.736.320                                   ║")
    print("║  Github: https://github.com/xxsxdev01-debug           ║")
    print("║                                                       ║")
    print("║            --- DragonBall Version 1.0 ---             ║")
    print("+═══════════════════════════════════════════════════════+\033[0m")
    
    # Menu với mỗi dòng một màu riêng biệt
    print("\033[1;32m [1]. Khởi động Server Game (Java)\033[0m")       # Xanh lá
    print("\033[1;34m [2]. Bật Cơ sở dữ liệu (MySQL)\033[0m")    # Xanh dương
    print("\033[1;35m [3]. Chỉnh sửa tài khoản người dùng\033[0m")      # Tím
    print("\033[1;33m [4]. Xem Log hoạt động hệ thống\033[0m")         # Vàng
    print("\033[1;36m [5]. Cập nhật mã nguồn mới nhất\033[0m")         # Xanh lơ (Cyan)
    print("\033[1;31m [0]. Thoát Tool\033[0m")                        # Đỏ
    
    print("\033[1;31m+═══════════════════════════════════════════════════════+\033[0m")

def start_server():
    clear_screen()    
    if os.path.exists("start_server.py"):
        print("\033[1;33m[i] Đang gọi trình khởi động Server Game...\033[0m")
        os.system("python start_server.py")
    else:
        print("\033[1;31m[!] Lỗi: Không tìm thấy file start_server.py!\033[0m")
    input("\nNhấn Enter để quay lại Menu...")

def setup_database():
    clear_screen()
    if os.path.exists("database.py"):
        os.system("python database.py")
    else:
        print("\033[1;31m[!] Lỗi: Không tìm thấy file database.py!\033[0m")
    input("\nNhấn Enter để quay lại Menu...")

def update_tool():
    clear_screen()
    if os.path.exists("update.py"):
        os.system("python update.py")
    else:
        print("\033[1;33m[!] Đang tải trình cập nhật lần đầu...\033[0m")
        url = "https://raw.githubusercontent.com/xxsxdev01-debug/DragonBall/main/update.py"
        os.system(f"curl -L {url} -o update.py")
        os.system("python update.py")
    input("\nNhấn Enter để quay lại Menu...")

def main():
    while True:
        menu_display()
        choice = input("\033[1;37m➤ Nhập lựa chọn của bạn: \033[0m")
        
        if choice == '1':
            start_server()
        elif choice == '2':
            setup_database()
        elif choice == '5':
            update_tool()
        elif choice == '0':
            print("\033[1;31m[!] Đang thoát hệ thống...\033[0m")
            time.sleep(1)
            break
        else:
            print("\033[1;31m[!] Lựa chọn không hợp lệ!\033[0m")
            time.sleep(1)

if __name__ == "__main__":
    main()
