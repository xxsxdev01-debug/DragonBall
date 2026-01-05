import os
import time

def setup_database():
    os.system('clear')
    print("\033[1;32m===============================================")
    print("      HỆ THỐNG TỰ ĐỘNG SQL & PHPMYADMIN        ")
    print("===============================================\033[0m")

    # 1. Cài đặt các gói
    print("\033[1;36m[1/5] Cài đặt MariaDB, Apache, PHP...\033[0m")
    os.system("pkg install mariadb apache2 php php-apache wget unzip curl -y")

    # 2. Khởi động MySQL
    print("\033[1;36m[2/5] Khởi động MariaDB Server...\033[0m")
    os.system("pkill -9 mariadbd")
    os.system("pkill -9 mysqld")
    
    mysql_data_dir = os.path.expandvars("$PREFIX/var/lib/mysql")
    if not os.path.exists(mysql_data_dir):
        os.system("mysql_install_db")
    
    os.system("mysqld_safe --datadir=$PREFIX/var/lib/mysql --port=3306 > /dev/null 2>&1 &")
    time.sleep(7) # Đợi lâu hơn một chút để MySQL kịp lên

    # 3. Nạp dữ liệu và Cấp quyền (SỬA LẠI LỆNH)
    print("\033[1;36m[3/5] Đang tạo Database 'dragonball'...\033[0m")
    url_sql = "https://raw.githubusercontent.com/xxsxdev01-debug/DragonBall/main/dragonball.sql"
    os.system(f"curl -L {url_sql} -o dragonball.sql")
    
    # Ép tạo database và import
    os.system("mariadb -u root -e 'CREATE DATABASE IF NOT EXISTS dragonball;'")
    os.system("mariadb -u root dragonball < dragonball.sql")
    # Cấp quyền sửa cho web
    os.system("mariadb -u root -e \"GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost'; FLUSH PRIVILEGES;\"")

    # 4. Cấu hình Apache chạy PHP (KHẮC PHỤC LỖI HIỆN DANH SÁCH FILE)
    print("\033[1;36m[4/5] Cấu hình Apache nhận diện PHP...\033[0m")
    httpd_conf = os.path.expandvars("$PREFIX/etc/apache2/httpd.conf")
    
    # Thêm cấu hình PHP vào cuối file httpd.conf nếu chưa có
    with open(httpd_conf, "r") as f:
        content = f.read()
    
    if "libphp.so" not in content:
        with open(httpd_conf, "a") as f:
            f.write("\nLoadModule php_module libexec/apache2/libphp.so\n")
            f.write("AddType application/x-httpd-php .php\n")
            f.write("<IfModule dir_module>\n    DirectoryIndex index.php index.html\n</IfModule>\n")

    # Cài đặt phpMyAdmin
    web_dir = os.path.expandvars("$PREFIX/share/apache2/default-site/htdocs")
    if not os.path.exists(f"{web_dir}/phpmyadmin"):
        os.system(f"cd {web_dir} && wget https://files.phpmyadmin.net/phpMyAdmin/5.2.1/phpMyAdmin-5.2.1-all-languages.zip")
        os.system(f"cd {web_dir} && unzip phpMyAdmin-5.2.1-all-languages.zip > /dev/null")
        os.system(f"cd {web_dir} && mv phpMyAdmin-5.2.1-all-languages phpmyadmin")
        os.system(f"cd {web_dir} && rm *.zip")

    # Tạo config tự đăng nhập
    with open(f"{web_dir}/phpmyadmin/config.inc.php", "w") as f:
        f.write("<?php $cfg['Servers'][1]['auth_type'] = 'config'; $cfg['Servers'][1]['user'] = 'root'; $cfg['Servers'][1]['password'] = ''; $cfg['Servers'][1]['host'] = '127.0.0.1'; $cfg['Servers'][1]['AllowNoPassword'] = true; ?>")

    # 5. Khởi động lại Apache
    print("\033[1;36m[5/5] Restart Web Server...\033[0m")
    os.system("pkill httpd")
    os.system("httpd")

    print("\033[1;32m===============================================")
    print("[+] XONG! TRUY CẬP: http://127.0.0.1:8080/phpmyadmin/")
    print("➤ Bây giờ bạn sẽ thấy Database 'dragonball' bên trái.")
    print("===============================================\033[0m")
    input("Nhấn Enter để tiếp tục...")
