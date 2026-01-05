import os
import time
import threading
import sys

# Cấu hình file
jar_file = "NgocRongOnline.jar"
driver_file = "mysql-driver.jar"
main_class = "nro.models.server.ServerManager"
log_file = "server.log"

def display_logs():
    """Hàm này chạy ngầm để liên tục in log mới ra màn hình"""
    if not os.path.exists(log_file):
        with open(log_file, 'w') as f: f.write("--- Khởi tạo Log ---\n")
    
    # Mở file log và nhảy đến cuối file
    with open(log_file, 'r') as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if line:
                # In log ra và giữ menu phía trên (không dùng clear ở đây)
                sys.stdout.write(f"\033[1;37m{line}\033[0m")
                sys.stdout.flush()
            else:
                time.sleep(0.5)

def print_menu():
    """Hàm in Menu cố định ở phía trên"""
    # Dùng mã ANSI để cố định Menu ở những dòng đầu tiên
    print("\033[H") # Đưa con trỏ về đầu màn hình
    print("\033[1;32m===============================================")
    print("      HỆ THỐNG QUẢN LÝ SERVER DRAGONBALL       ")
    print(" [1].RAM  [2].Port  [3].Admin  [4].TẮT GAME(SAVE)")
    print("===============================================\033[0m")
    print("\033[1;36m➤ Nhập số rồi Enter: \033[0m", end="", flush=True)

def main():
    os.system('clear')
    
    # 1. Khởi chạy JAR ngầm nếu chưa chạy
    check_run = os.popen(f"pgrep -f {jar_file}").read()
    if not check_run:
        if os.path.exists(log_file): os.remove(log_file)
        # Chạy Java đẩy log vào file
        os.system(f"nohup java -Xmx512M -Duser.timezone=UTC -cp \"{driver_file}:{jar_file}\" {main_class} > {log_file} 2>&1 &")
        print("🚀 Đang khởi động JAR...")
        time.sleep(2)

    # 2. Chạy luồng hiển thị Log tự động
    thread_log = threading.Thread(target=display_logs, daemon=True)
    thread_log.start()

    # 3. Vòng lặp nhận lệnh từ người dùng
    while True:
        print_menu()
        choice = input()
        
        # Xử lý lệnh
        if choice == '1':
            print("\n")
            os.system("free -h")
            time.sleep(2)
        elif choice == '2':
            print("\n")
            os.system("netstat -tunlp | grep java")
            time.sleep(2)
        elif choice == '3':
            if os.path.exists("admin.sh"):
                os.system("bash admin.sh")
            else:
                print("\n[!] Không thấy admin.sh")
            time.sleep(2)
        elif choice == '4':
            print("\n\033[1;31m[*] Đang lưu và tắt Game...\033[0m")
            os.system(f"pkill -15 -f {jar_file}")
            time.sleep(5)
            print("Đã tắt.")
            break
        
        # Sau mỗi lệnh, xóa bớt màn hình phía trên để Menu không bị trôi
        os.system('clear')

if __name__ == "__main__":
    main()
