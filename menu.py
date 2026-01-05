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
    clear_screen()
    # Kiểm tra xem file start_server.py có tồn tại không
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
        # Nếu chưa có file update.py, tự dùng curl tải về rồi chạy
        print("\033[1;33m[!] Đang tải trình cập nhật lần đầu...\033[0m")
        url = "https://raw.githubusercontent.com/xxsxdev01-debug/DragonBall/main/update.py"
        os.system(f"curl -L {url} -o update.py")
        os.system("python update.py")
    input("\nNhấn Enter để quay lại Menu...")

def main():
    while True:
        menu_display()
        choice = input("\033[1;36m➤ Nhập lựa chọn của bạn: \033[0m")
        
        if choice == '1':
            start_server()
        elif choice == '2':
            setup_database()
        elif choice == '5':
            # Phím số 5 đã có thể sử dụng
            update_tool()
        elif choice == '0':
            print("Đang thoát...")
            break
        else:
            print("\033[1;31m[!] Lựa chọn không hợp lệ!\033[0m")
            time.sleep(1)

if __name__ == "__main__":
    main()
    
