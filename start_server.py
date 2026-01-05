import os
import time
import threading
import sys

# Cấu hình file
jar_file = "NgocRongOnline.jar"
driver_file = "mysql-driver.jar"
main_class = "nro.models.server.ServerManager"
log_file = "server.log"

def setup_terminal():
    """Thiết lập vùng cuộn: Log ở trên, Menu ở dưới"""
    rows, cols = os.get_terminal_size()
    # Để lại 5 dòng cuối cho Menu
    scroll_region = rows - 5
    # Mã ANSI: Đặt vùng cuộn từ dòng 1 đến dòng scroll_region
    sys.stdout.write(f"\033[1;{scroll_region}r")
    # Đưa con trỏ về dòng đầu tiên của vùng cuộn
    sys.stdout.write("\033[1;1H")
    sys.stdout.flush()

def display_logs():
    """Luồng in log liên tục vào vùng cuộn"""
    if not os.path.exists(log_file):
        with open(log_file, 'w') as f: f.write("--- Khởi tạo Log ---\n")
    
    rows, cols = os.get_terminal_size()
    menu_start_row = rows - 4

    with open(log_file, 'r') as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if line:
                # Lưu vị trí con trỏ hiện tại
                sys.stdout.write("\033[s")
                # Nhảy về dòng cuối của vùng cuộn để in log
                sys.stdout.write(f"\033[{menu_start_row-1};1H")
                sys.stdout.write(f"\033[1;37m{line}\033[0m")
                # Khôi phục vị trí con trỏ (về dòng nhập lệnh)
                sys.stdout.write("\033[u")
                sys.stdout.flush()
            else:
                time.sleep(0.5)

def print_fixed_menu():
    """In Menu cố định ở 5 dòng cuối màn hình"""
    rows, cols = os.get_terminal_size()
    menu_start_row = rows - 4
    
    # Nhảy đến vùng Menu
    sys.stdout.write(f"\033[{menu_start_row};1H")
    sys.stdout.write("\033[1;32m===============================================\n")
    sys.stdout.write("      HỆ THỐNG QUẢN LÝ SERVER DRAGONBALL       \n")
    sys.stdout.write(" [1].RAM  [2].Port  [3].Admin  [4].TẮT GAME(SAVE)\n")
    sys.stdout.write("===============================================\033[0m\n")
    sys.stdout.write("\033[1;36m➤ Nhập số: \033[0m")
    sys.stdout.flush()

def main():
    os.system('clear')
    setup_terminal()
    
    # 1. Khởi chạy JAR ngầm
    check_run = os.popen(f"pgrep -f {jar_file}").read()
    if not check_run:
        if os.path.exists(log_file): os.remove(log_file)
        os.system(f"nohup java -Xmx512M -Duser.timezone=UTC -cp \"{driver_file}:{jar_file}\" {main_class} > {log_file} 2>&1 &")
    
    # 2. Chạy luồng hiển thị Log
    thread_log = threading.Thread(target=display_logs, daemon=True)
    thread_log.start()

    # 3. Vòng lặp nhận lệnh
    while True:
        print_fixed_menu()
        # Đưa con trỏ đến vị trí sau chữ "Nhập số: "
        rows, cols = os.get_terminal_size()
        sys.stdout.write(f"\033[{rows};12H") 
        sys.stdout.flush()
        
        choice = sys.stdin.readline().strip()
        
        # Xóa dòng lệnh vừa nhập để Menu sạch sẽ
        sys.stdout.write(f"\033[{rows};12H\033[K")
        
        if choice == '1':
            os.system("free -h")
            time.sleep(2)
        elif choice == '2':
            os.system("netstat -tunlp | grep java")
            time.sleep(2)
        elif choice == '3':
            os.system("bash admin.sh") if os.path.exists("admin.sh") else print("No admin.sh")
            time.sleep(2)
        elif choice == '4':
            os.system(f"pkill -15 -f {jar_file}")
            # Khôi phục toàn bộ màn hình trước khi thoát
            sys.stdout.write("\033[r\033[2J\033[H") 
            print("Đang lưu và tắt...")
            time.sleep(5)
            break

if __name__ == "__main__":
    main()
    
