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
    """Luồng in log liên tục, đảm bảo không đè lên dòng cuối của Menu"""
    if not os.path.exists(log_file):
        with open(log_file, 'w') as f: f.write("--- Khởi tạo Log ---\n")
    
    with open(log_file, 'r') as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if line:
                rows, _ = os.get_terminal_size()
                # Lưu vị trí con trỏ
                sys.stdout.write("\033[s")
                # Nhảy lên dòng phía trên Menu để in log
                sys.stdout.write(f"\033[{rows-5};1H")
                sys.stdout.write(f"\033[1;37m{line}\033[0m")
                # Trả con trỏ về dòng nhập lệnh
                sys.stdout.write("\033[u")
                sys.stdout.flush()
            else:
                time.sleep(0.2)

def print_menu_at_bottom():
    """In Menu cố định ở 5 dòng cuối cùng"""
    rows, _ = os.get_terminal_size()
    menu_start = rows - 4
    sys.stdout.write(f"\033[{menu_start};1H")
    sys.stdout.write("\033[1;32m===============================================\n")
    sys.stdout.write("      HỆ THỐNG QUẢN LÝ SERVER DRAGONBALL       \n")
    sys.stdout.write(" [1].RAM  [2].Port  [3].Admin  [4].TẮT GAME(SAVE)\n")
    sys.stdout.write("===============================================\033[0m\n")
    sys.stdout.write("\033[1;36m➤ Nhập số: \033[0m")
    sys.stdout.flush()

def main():
    os.system('clear')
    
    # 1. Khởi chạy JAR (Hiện log trực tiếp trong 6 giây đầu)
    if not os.path.exists(driver_file):
        os.system(f"curl -L https://repo1.maven.org/maven2/mysql/mysql-connector-java/5.1.49/mysql-connector-java-5.1.49.jar -o {driver_file}")

    print("\033[1;32m🚀 ĐANG KHỞI CHẠY SERVER... VUI LÒNG ĐỢI 6 GIÂY...\033[0m\n")
    
    # Xóa log cũ
    if os.path.exists(log_file): os.remove(log_file)
    
    # --- ĐOẠN FIX LỖI "NO LINE FOUND" ---
    # Thêm "< /dev/null" để giả lập đầu vào rỗng, tránh Scanner bị lỗi
    cmd_run = f"nohup java -Xmx512M -Duser.timezone=UTC -cp \"{driver_file}:{jar_file}\" {main_class} < /dev/null > {log_file} 2>&1 &"
    os.system(cmd_run)

    # Hiển thị Log trực tiếp trong 6 giây đầu tiên
    start_time = time.time()
    with open(log_file, 'r') as f:
        while time.time() - start_time < 15:
            line = f.readline()
            if line:
                print(f"\033[1;37m{line.strip()}\033[0m")
            else:
                time.sleep(0.1)

    # 2. Sau 6 giây, thiết lập vùng cuộn để giữ Menu ở dưới
    rows, _ = os.get_terminal_size()
    sys.stdout.write(f"\033[1;{rows-15}r") # Vùng cuộn ở trên
    sys.stdout.flush()

    # Chạy luồng cập nhật log tiếp theo vào vùng cuộn
    thread_log = threading.Thread(target=display_logs, daemon=True)
    thread_log.start()

    # 3. Vòng lặp Menu
    while True:
        rows, _ = os.get_terminal_size()
        print_menu_at_bottom()
        
        # Đưa con trỏ đến vị trí nhập số
        sys.stdout.write(f"\033[{rows};12H")
        sys.stdout.flush()
        
        choice = sys.stdin.readline().strip()
        sys.stdout.write(f"\033[{rows};12H\033[K") # Xóa lệnh vừa nhập
        
        if choice == '1':
            os.system("free -h")
            time.sleep(2)
        elif choice == '2':
            os.system("netstat -tunlp | grep java")
            time.sleep(2)
        elif choice == '3':
            os.system("bash admin.sh") if os.path.exists("admin.sh") else None
        elif choice == '4':
            os.system(f"pkill -15 -f {jar_file}")
            sys.stdout.write("\033[r\033[2J\033[H")
            print("Đã lưu dữ liệu và tắt Game.")
            time.sleep(5)
            break

if __name__ == "__main__":
    main()
    
