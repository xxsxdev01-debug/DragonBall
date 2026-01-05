import os
import time

def setup_database():
    os.system('clear')
    print("\033[1;32m===============================================")
    print("      HỆ THỐNG TỰ ĐỘNG SQL & PHPMYADMIN        ")
    print("===============================================\033[0m")

    # 1. Cài đặt các gói cần thiết (Thêm wget và unzip)
    print("\033[1;36m[1/5] Đang cài đặt MariaDB, Apache, PHP, Unzip...\033[0m")
    os.system("pkg install mariadb apache2 php php-apache wget unzip -y")

    # 2. Khởi động MySQL (Port 3306)
    print("\033[1;36m[2/5] Khởi động MySQL Server...\033[0m")
    mysql_data_dir = os.path.expandvars("$PREFIX/var/lib/mysql")
    os.system(f"mysql_install_db --datadir={mysql_data_dir} > /dev/null 2>&1")
    os.system(f"mysqld_safe --datadir={mysql_data_dir} --port=3306 > /dev/null 2>&1 &")
    time.sleep(5)

    # 3. Nạp dữ liệu DragonBall
    print("\033[1;36m[3/5] Đang nạp dữ liệu từ GitHub...\033[0m")
    url_sql = "https://raw.githubusercontent.com/xxsxdev01-debug/DragonBall/main/dragonball.sql"
    os.system(f"curl -L {url_sql} -o dragonball.sql")
    os.system("mariadb -u root -e 'CREATE DATABASE IF NOT EXISTS dragonball;'")
    os.system("mariadb -u root dragonball < dragonball.sql")
    os.system("mariadb -u root -e 'USE mysql; UPDATE user SET plugin=\"\" WHERE User=\"root\"; FLUSH PRIVILEGES;'")

    # 4. TỰ ĐỘNG CÀI PHPMYADMIN (Sửa lỗi Not Found)
    print("\033[1;36m[4/5] Đang cài đặt giao diện Web PHPMyAdmin...\033[0m")
    web_dir = os.path.expandvars("$PREFIX/share/apache2/default-site/htdocs")
    if not os.path.exists(f"{web_dir}/phpmyadmin"):
        print("[-] Đang tải bộ cài phpMyAdmin (v5.2.1)...")
        os.system(f"cd {web_dir} && wget https://files.phpmyadmin.net/phpMyAdmin/5.2.1/phpMyAdmin-5.2.1-all-languages.zip")
        os.system(f"cd {web_dir} && unzip phpMyAdmin-5.2.1-all-languages.zip > /dev/null")
        os.system(f"cd {web_dir} && mv phpMyAdmin-5.2.1-all-languages phpmyadmin")
        os.system(f"cd {web_dir} && rm phpMyAdmin-5.2.1-all-languages.zip")
    else:
        print("[+] phpMyAdmin đã tồn tại.")

    # 5. Khởi động Web Server
    print("\033[1;36m[5/5] Đang bật Web Server...\033[0m")
    os.system("pkill httpd")
    os.system("httpd")

    print("\033[1;32m===============================================")
    print("[+] HOÀN TẤT! SQL CHẠY TẠI PORT 3306")
    print("➤ Web quản trị: http://127.0.0.1:8080/phpmyadmin")
    print("➤ Tài khoản: root | Mật khẩu: (để trống)")
    print("===============================================\033[0m")
    input("Nhấn Enter để quay lại Menu...")

if __name__ == "__main__":
    setup_database()
