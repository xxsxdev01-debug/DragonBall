import os
import time

def setup_database():
    os.system('clear')
    print("\033[1;32m===============================================")
    print("      KHỞI TẠO CƠ SỞ DỮ LIỆU DRAGONBALL        ")
    print("===============================================\033[0m")

    # 1. Cài đặt MariaDB nếu chưa có
    print("\033[1;36m[1/4] Kiểm tra MariaDB...\033[0m")
    if os.system("command -v mariadb > /dev/null") != 0:
        print("[!] Đang cài đặt MariaDB hệ thống...")
        os.system("pkg install mariadb -y")
    else:
        print("[+] MariaDB đã được cài đặt.")

    # 2. Khởi động MySQL Server
    print("\033[1;36m[2/4] Khởi động MySQL Server...\033[0m")
    # Đảm bảo thư mục dữ liệu tồn tại
    os.system("mysql_install_db --datadir=$PREFIX/var/lib/mysql > /dev/null 2>&1")
    # Chạy mysqld_safe ngầm
    os.system("mysqld_safe --datadir=$PREFIX/var/lib/mysql > /dev/null 2>&1 &")
    time.sleep(5) # Chờ 5 giây để Server khởi động

    # 3. Tải file SQL từ GitHub (nếu chưa có ở máy)
    print("\033[1;36m[3/4] Kiểm tra tệp tin SQL...\033[0m")
    sql_file = "database.sql"
    if not os.path.exists(sql_file):
        print("[!] Không thấy file SQL tại máy, đang tải từ GitHub...")
        # Thay LINK_RAW_SQL_CUA_BAN bằng link raw thực tế của bạn
        url_sql = "https://raw.githubusercontent.com/xxsxdev01-debug/DragonBall/main/dragonball.sql"
        os.system(f"curl -L {url_sql} -o {sql_file}")
    
    # 4. Tạo Database và nạp dữ liệu
    print("\033[1;36m[4/4] Nạp dữ liệu vào Database 'dragonball'...\033[0m")
    db_name = "dragonball"
    
    # Tạo database (mặc định user root, localhost không pass trên Termux)
    os.system(f"mariadb -u root -e 'CREATE DATABASE IF NOT EXISTS {db_name};'")
    
    # Nạp file SQL
    if os.path.exists(sql_file):
        error = os.system(f"mariadb -u root {db_name} < {sql_file}")
        if error == 0:
            print(f"\033[1;32m[+] THÀNH CÔNG: Đã nạp Database '{db_name}' thành công!\033[0m")
        else:
            print("\033[1;31m[!] LỖI: Không thể nạp dữ liệu. Kiểm tra lại file SQL.\033[0m")
    else:
        print("\033[1;31m[!] LỖI: Thiếu file database.sql để nạp.\033[0m")

    print("\033[1;32m===============================================\033[0m")
    input("Nhấn Enter để quay lại Menu quản trị...")

if __name__ == "__main__":
    setup_database()
  
