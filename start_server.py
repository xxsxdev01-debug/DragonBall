
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
    """Thiết lập vùng cuộn: Log cuộn từ dòng 1 đến (rows-6), Menu cố định 5 dòng cuối"""
    rows, cols = os.get_terminal_size()
    # Vùng cuộn chỉ từ dòng 1 đến dòng cách đáy 6 dòng
    scroll_limit = rows - 6
    # ANSI: Đặt vùng cuộn (Top;Bottom r)
    sys.stdout.write(f"\033[1;{scroll_limit}r")
    # Đưa con trỏ về dòng 1
    sys.stdout.write("\033[1;1H")
    sys.stdout.flush()

def display_logs():
    """Luồng in log tự động vào vùng cuộn phía trên"""
    if not os.path.exists(log_file):
        with open(log_file, 'w') as f: f.write("--- Đang khởi tạo Log ---\n")
    
    rows, _ = os.get_terminal_size()
    log_row = rows - 6 # Dòng cuối cùng của vùng log

    with open(log_file, 'r') as f:
        f.seek(0, 2) # Nhảy đến cuối file
        while True:
            line = f.readline()
            if line:
                # Lưu vị trí con trỏ (đang ở dòng nhập lệnh)
                sys.stdout.write("\033[s")
                # Nhảy lên dòng cuối của vùng cuộn để in log
                sys.stdout.write(f"\033[{log_row};1H")
                # In log và xóa định dạng màu nếu cần
                sys.stdout.write(f"\033[1;37m{line.strip()}\033[0m\n")
                # Khôi phục con trỏ về vị trí nhập lệnh
                sys.stdout.write("\033[u")
                sys.stdout.flush()
            else:
                time.sleep(0.2)

def print_fixed_menu():
    """In Menu cố định ở 5 dòng cuối cùng"""
    rows, _ = os.get_terminal_size()
    menu_start = rows - 4 # Bắt đầu in menu từ dòng này
    
    # Nhảy đến dòng bắt đầu Menu
    sys.stdout.write(f"\033[{menu_start};1H")
    sys.stdout.write("\033[1;32m===============================================\n")
    sys.stdout.write("      HỆ THỐNG QUẢN LÝ SERVER DRAGONBALL       \n")
    sys.stdout.write(" [1].RAM  [2].Port  [3].Admin  [4].TẮT GAME(SAVE)\n")
    sys.stdout.write("===============================================\033[0m\n")
    sys.stdout.write("\033[1;36m➤ Nhập số: \033[0m")
    sys.stdout.flush()

def main():
    # Xóa màn hình và thiết lập vùng cuộn
    os.system('clear')
    setup_terminal()
    
    # 1. Khởi chạy JAR ngầm nếu chưa chạy
    check_run = os.popen(f"pgrep -f {jar_file}").read()
    if not check_run:
        if os.path.exists(log_file): os.remove(log_file)
        os.system(f"nohup java -Xmx512M -Duser.timezone=UTC -cp \"{driver_file}:{jar_file}\" {main_class} > {log_file} 2>&1 &")
    
    # 2. Chạy luồng Log (Daemon để tự tắt khi thoát main)
    thread_log = threading.Thread(target=display_logs, daemon=True)
    thread_log.start()

    # 3. Vòng lặp nhận lệnh
    while True:
        rows, _ = os.get_terminal_size()
        print_fixed_menu()
        
        # Đưa con trỏ đến đúng vị trí sau chữ "Nhập số: " (Dòng cuối cùng)
        sys.stdout.write(f"\033[{rows};12H")
        sys.stdout.flush()
        
        # Nhận input
        choice = sys.stdin.readline().strip()
        
        # Xóa dòng vừa nhập để Menu luôn sạch sẽ
        sys.stdout.write(f"\033[{rows};12H\033[K")
        
        if choice == '1':
            # Nhảy lên vùng log để in tạm kết quả RAM
            sys.stdout.write("\033[s\033[1;1H\n\033[1;33m--- RAM Status ---\033[0m\n")
            os.system("free -h")
            sys.stdout.write("\033[u")
            time.sleep(2)
        elif choice == '2':
            sys.stdout.write("\033[s\033[1;1H\n\033[1;33m--- Port Status ---\033[0m\n")
            os.system("netstat -tunlp | grep java")
            sys.stdout.write("\033[u")
            time.sleep(2)
        elif choice == '3':
            if os.path.exists("admin.sh"):
                os.system("bash admin.sh")
            else:
                sys.stdout.write("\033[s\033[1;1H\033[1;31m[!] Không thấy admin.sh\033[0m\n\033[u")
            time.sleep(1)
        elif choice == '4':
            os.system(f"pkill -15 -f {jar_file}")
            # Khôi phục terminal (Hủy vùng cuộn)
            sys.stdout.write("\033[r\033[2J\033[H")
            print("\033[1;31m[*] Đang lưu dữ liệu và tắt Game...\033[0m")
            time.sleep(5)
            break

if __name__ == "__main__":
    main()
            
