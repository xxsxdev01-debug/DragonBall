import os
import time

def setup_database():
    os.system('clear')
    print("\033[1;32m===============================================")
    print("      HỆ THỐNG TỰ ĐỘNG SQL & PHPMYADMIN        ")
    print("===============================================\033[0m")

    # Cấu hình thông số hiển thị
    DB_NAME = "dragonball"
    DB_USER = "root"
    DB_PASS = "(Trống)"
    DB_HOST = "127.0.0.1"
    DB_PORT = "3306"

    # 1. Cài đặt các gói
    print(f"\033[1;36m[1/5] Cài đặt gói hệ thống...\033[0m")
    os.system("pkg install mariadb apache2 php php-apache wget unzip curl -y")

    # 2. Khởi động MySQL
    print(f"\033[1;36m[2/5] Khởi động MariaDB Server (Port {DB_PORT})...\033[0m")
    os.system("pkill -9 mariadbd")
    os.system("pkill -9 mysqld")
    
    mysql_data_dir = os.path.expandvars("$PREFIX/var/lib/mysql")
    if not os.path.exists(mysql_data_dir):
        print("[*] Đang khởi tạo dữ liệu MariaDB lần đầu...")
        os.system("mysql_install_db")
    
    os.system(f"mysqld_safe --datadir={mysql_data_dir} --port={DB_PORT} > /dev/null 2>&1 &")
    time.sleep(8) # Đợi MySQL khởi động hoàn toàn

    # 3. Nạp dữ liệu và Cấp quyền
    print(f"\033[1;36m[3/5] Đang tạo Database và nạp SQL...\033[0m")
    url_sql = "https://raw.githubusercontent.com/xxsxdev01-debug/DragonBall/main/dragonball.sql"
    os.system(f"curl -L {url_sql} -o dragonball.sql")
    
    # Thực hiện lệnh tạo DB và User minh bạch
    os.system(f"mariadb -u root -e 'CREATE DATABASE IF NOT EXISTS {DB_NAME};'")
    os.system(f"mariadb -u root {DB_NAME} < dragonball.sql")
    
    # Lệnh cấp quyền quan trọng để sửa được SQL trên Web
    os.system(f"mariadb -u root -e \"GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION; FLUSH PRIVILEGES;\"")
    
    print(f"\033[1;32m[V] Đã tạo thành công Database: {DB_NAME}\033[0m")

    # 4. Cấu hình Apache chạy PHP
    print(f"\033[1;36m[4/5] Cấu hình giao diện Web (phpMyAdmin)...\033[0m")
    httpd_conf = os.path.expandvars("$PREFIX/etc/apache2/httpd.conf")
    
    # Kiểm tra và nạp Module PHP vào Apache
    with open(httpd_conf, "r") as f:
        content = f.read()
    if "libphp.so" not in content:
        with open(httpd_conf, "a") as f:
            f.write("\nLoadModule php_module libexec/apache2/libphp.so\n")
            f.write("AddType application/x-httpd-php .php\n")
            f.write("<IfModule dir_module>\n    DirectoryIndex index.php index.html\n</IfModule>\n")

    # Tải và cài đặt phpMyAdmin
    web_dir = os.path.expandvars("$PREFIX/share/apache2/default-site/htdocs")
    if not os.path.exists(f"{web_dir}/phpmyadmin"):
        print("[-] Đang tải bộ mã nguồn phpMyAdmin...")
        os.system(f"cd {web_dir} && wget https://files.phpmyadmin.net/phpMyAdmin/5.2.1/phpMyAdmin-5.2.1-all-languages.zip")
        os.system(f"cd {web_dir} && unzip phpMyAdmin-5.2.1-all-languages.zip > /dev/null")
        os.system(f"cd {web_dir} && mv phpMyAdmin-5.2.1-all-languages phpmyadmin")
        os.system(f"cd {web_dir} && rm *.zip")

    # Tạo file cấu hình đăng nhập tự động
    config_file = f"{web_dir}/phpmyadmin/config.inc.php"
    with open(config_file, "w") as f:
        f.write(f"<?php $cfg['Servers'][1]['auth_type'] = 'config'; $cfg['Servers'][1]['user'] = '{DB_USER}'; $cfg['Servers'][1]['password'] = ''; $cfg['Servers'][1]['host'] = '{DB_HOST}'; $cfg['Servers'][1]['AllowNoPassword'] = true; ?>")

    # 5. Khởi động lại Apache
    print(f"\033[1;36m[5/5] Kích hoạt Web Server Port 8080...\033[0m")
    os.system("pkill httpd")
    os.system("httpd")

    print("\033[1;32m===============================================")
    print("      THIẾT LẬP THÀNH CÔNG (SQL SẴN SÀNG)      ")
    print("===============================================")
    print(f" ➤ Database Name: {DB_NAME}")
    print(f" ➤ MariaDB User: {DB_USER}")
    print(f" ➤ MariaDB Pass: {DB_PASS}")
    print(f" ➤ MySQL Port:   {DB_PORT}")
    print(" ----------------------------------------------")
    print(" ➤ Link Web: http://127.0.0.1:8080/phpmyadmin/")
    print("===============================================\033[0m")
    input("Nhấn Enter để quay lại Menu...")

if __name__ == "__main__":
    setup_database()
        
