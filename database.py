import os
import time

def setup_database():
    os.system('clear')
    print("\033[1;32m===============================================")
    print("      KHỞI TẠO SQL & CẤU HÌNH WEB PHP          ")
    print("      PORT SQL: 3306 | WEB PORT: 8080          ")
    print("===============================================\033[0m")

    # Xác định môi trường Termux
    is_termux = os.path.exists('/data/data/com.termux')
    
    # 1. Cài đặt các gói cần thiết cho cả Database và Web
    print("\033[1;36m[1/5] Kiểm tra và cài đặt MariaDB, Apache2, PHP...\033[0m")
    if is_termux:
        # Cài đặt trọn gói trên Termux
        os.system("pkg install mariadb apache2 php php-apache -y")
    else:
        # Cài đặt trên Linux Server
        os.system("sudo apt-get update && sudo apt-get install mariadb-server apache2 php libapache2-mod-php php-mysql -y")

    # 2. Khởi động MySQL Server (Port 3306)
    print("\033[1;36m[2/5] Khởi động MySQL Server (Port 3306)...\033[0m")
    if is_termux:
        mysql_data_dir = os.getenv('PREFIX', '') + '/var/lib/mysql'
        os.system(f"mysql_install_db --datadir={mysql_data_dir} > /dev/null 2>&1")
        # Chạy ngầm port 3306
        os.system(f"mysqld_safe --datadir={mysql_data_dir} --port=3306 > /dev/null 2>&1 &")
    else:
        os.system("sudo service mysql start")
    
    time.sleep(5) 

    # 3. Đồng bộ SQL từ GitHub
    print("\033[1;36m[3/5] Tải dữ liệu dragonball.sql từ GitHub...\033[0m")
    sql_file = "dragonball.sql"
    url_sql = "https://raw.githubusercontent.com/xxsxdev01-debug/DragonBall/main/dragonball.sql"
    os.system(f"curl -L {url_sql} -o {sql_file}")

    # 4. Tạo Database và Cấp quyền đăng nhập Web
    print("\033[1;36m[4/5] Nạp dữ liệu & Cấu hình quyền truy cập root...\033[0m")
    db_name = "dragonball"
    
    # Tạo DB và nạp file
    os.system(f"mariadb -u root -e 'CREATE DATABASE IF NOT EXISTS {db_name};'")
    os.system(f"mariadb -u root {db_name} < {sql_file}")
    
    # LỆNH QUAN TRỌNG: Cho phép đăng nhập root trên giao diện Web (phpMyAdmin)
    os.system("mariadb -u root -e 'USE mysql; UPDATE user SET plugin=\"\" WHERE User=\"root\"; FLUSH PRIVILEGES;'")

    # 5. Khởi động Web Server để vào localhost
    print("\033[1;36m[5/5] Khởi động Apache Web Server...\033[0m")
    if is_termux:
        # Tắt apache cũ nếu đang chạy rồi bật lại
        os.system("pkill httpd")
        os.system("httpd") 
        web_url = "http://127.0.0.1:8080/phpmyadmin"
    else:
        os.system("sudo service apache2 restart")
        web_url = "http://127.0.0.1/phpmyadmin"

    print("\033[1;32m===============================================")
    print(f"[+] THÀNH CÔNG! SQL đang chạy tại Port 3306.")
    print(f"[+] Bạn có thể vào Web quản lý tại:")
    print(f"➤ {web_url}")
    print("\033[1;32m===============================================\033[0m")
    input("Nhấn Enter để quay lại Menu...")

if __name__ == "__main__":
    setup_database()
    
