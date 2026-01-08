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
    if not os.path.exists(log_file):
        with open(log_file, 'w') as f: f.write("--- Khởi tạo Log ---\n")
    
    rows, _ = os.get_terminal_size()
    log_row = rows - 7

    with open(log_file, 'r') as f:
        f.seek(0, 2) 
        while True:
            line = f.readline()
            if line:               
                if "java.util.Scanner" not in line and "NoSuchElementException" not in line:
                    sys.stdout.write("\033[s") 
                    sys.stdout.write(f"\033[{log_row};1H") 
                    sys.stdout.write(f"\033[1;37m{line}\033[0m")
                    sys.stdout.write("\033[u")
                    sys.stdout.flush()
            else:
                time.sleep(0.1)

def print_fixed_menu():

    rows, _ = os.get_terminal_size()
    menu_start = rows - 5
    sys.stdout.write(f"\033[{menu_start};1H")
    sys.stdout.write("\033[1;32m╔═════════════════════════════════════════════╗\n")
    sys.stdout.write("║      HỆ THỐNG QUẢN LÝ SERVER DRAGONBALL     ║\n")
    sys.stdout.write("║ [1].RAM  [2].Port  [3].Admin  [4].TẮT (SAVE)║\n")
    sys.stdout.write("╚═════════════════════════════════════════════╝\033[0m\n")
    sys.stdout.write("\033[1;36m➤ Nhập lệnh: \033[0m")
    sys.stdout.flush()

def print_big_debug_null():
    os.system('clear')
    # Định nghĩa mã màu
    RED = "\x1b[1;31m"
    YELLOW = "\x1b[1;33m"
    RESET = "\x1b[0m"
    
    # Chèn mã RED vào trước các thanh ║ ở cuối dòng để giữ khung màu đỏ
    logo = f"""{RED}+══════════════════════════════════════════════════════════+
║  ____  _____ ____  _   _  ____   _   _ _   _ _           ║
║ |  _ \\| ____| __ )| | | |/ ___| | \\ | | | | | |          ║
║ | | | |  _| |  _ \\| | | | |  _  |  \\| | | | | |          ║
║ | |_| | |___| |_) | |_| | |_| | | |\\  | |_| | |___       ║
║ |____/|_____|____/ \___/ \____| |_| \_|\___/|_____|      ║
║                                                          ║
║{YELLOW}  Dev: Debug Null                                         {RED}║
║{YELLOW}  Zalo: 0899.736.320                                      {RED}║
║{YELLOW}  Github: https://github.com/xxsxdev01-debug              {RED}║
║                                                          ║
║{RED}            --- DragonBall Version 1.0 ---                ║
+══════════════════════════════════════════════════════════+{RESET}"""
    print(logo)
    

def main():
    print_big_debug_null()


    
    if not os.path.exists(driver_file):
        os.system(f"curl -L https://repo1.maven.org/maven2/mysql/mysql-connector-java/5.1.49/mysql-connector-java-5.1.49.jar -o {driver_file}")

    if os.path.exists(log_file): os.remove(log_file)   
    cmd_fix = (
        f"tail -f /dev/null | java -Xmx512M -Duser.timezone=UTC "
        f"-cp \"{driver_file}:{jar_file}\" {main_class} > {log_file} 2>&1 &"
    )
    os.system(cmd_fix)

    
    start_time = time.time()
    with open(log_file, 'r') as f:
        while time.time() - start_time < 20:
            line = f.readline()
            if line:
                if "java.util.Scanner" not in line and "NoSuchElementException" not in line:
                    print(f"\033[1;37m{line.strip()}\033[0m")
            else:
                time.sleep(0.1)


    rows, _ = os.get_terminal_size()
    sys.stdout.write(f"\033[1;{rows-20}r") 
    sys.stdout.flush()

    thread_log = threading.Thread(target=display_logs, daemon=True)
    thread_log.start()

    
    while True:
        rows, _ = os.get_terminal_size()
        print_fixed_menu()
         
        sys.stdout.write(f"\033[{rows};14H") 
        sys.stdout.flush()
        
        choice = sys.stdin.readline().strip()
        sys.stdout.write(f"\033[{rows};14H\033[K")
        
        if choice == '1':
            os.system("free -h")
            time.sleep(2)
        elif choice == '2':
            os.system("netstat -tunlp | grep java")
            time.sleep(2)
        elif choice == '3':
            os.system("bash admin.sh") if os.path.exists("admin.sh") else None
            time.sleep(2)
        elif choice == '4':
            os.system(f"pkill -15 -f {jar_file}")
            os.system("pkill -f 'tail -f /dev/null'") 
            sys.stdout.write("\033[r\033[2J\033[H")
            print("\033[1;31m[DEBUG NULL] ĐÃ LƯU DỮ LIỆU VÀ TẮT GAME AN TOÀN.\033[0m")
            time.sleep(2)
            break

if __name__ == "__main__":
    main()
