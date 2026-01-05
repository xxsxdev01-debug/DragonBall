import os
import time

def setup_database():
    os.system('clear')
    print("\033[1;32m===============================================")
    print("      HỆ THỐNG TỰ ĐỘNG SQL & PHPMYADMIN        ")
    print("===============================================\033[0m")

    # 1. Cài đặt các gói cần thiết
    print("\033[1;36m[1/5] Đang cài đặt MariaDB, Apache, PHP, Unzip...\033[0m")
    os.system("pkg install mariadb apache2 php php-apache wget unzip -y")

    # 2. Khởi động MySQL (Port 3306)
    print("\033[1;36m[2/5] Khởi động MySQL Server...\033[0m")
    os.system("pkill -9 mariadbd") # Tắt bản cũ nếu đang treo
    mysql_data_dir = os.path.expandvars("$PREFIX/var/lib/mysql")
    if not os.path.exists(mysql_data_dir):
        os.system(f"mysql_install_db --datadir={mysql_data_dir} > /dev/null 2>&1")
    
    os.system(f"mysqld_safe --datadir={mysql_data_dir} --port=3306 > /dev/null 2>&1 &")
    time.sleep(5)

    # 3. Nạp dữ liệu DragonBall và Cấp quyền root
    print("\033[1;36m[3/5] Đang nạp dữ liệu và cấp quyền sửa SQL...\033[0m")
    url_sql = "https://raw.githubusercontent.com/xxsxdev01-debug/DragonBall/main/dragonball.sql"
    os.system(f"curl -L {url_sql} -o dragonball.sql")
    # Tạo DB và Import
    os.system("mariadb -u root -e 'CREATE DATABASE IF NOT EXISTS dragonball;'")
    os.system("mariadb -u root dragonball < dragonball.sql")
    # Lệnh quan trọng: Cho phép root đăng nhập không mật khẩu và sửa được mọi thứ
    os.system("mariadb -u root -e \"ALTER USER 'root'@'localhost' IDENTIFIED VIA unix_socket OR mysql_native_password USING ''; GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION; FLUSH PRIVILEGES;\"")

    # 4. TỰ ĐỘNG CÀI PHPMYADMIN & CẤU HÌNH ĐỂ SỬA ĐƯỢC SQL
    print("\033[1;36m[4/5] Đang cài đặt giao diện Web PHPMyAdmin...\033[0m")
    web_dir = os.path.expandvars("$PREFIX/share/apache2/default-site/htdocs")
    pma_dir = f"{web_dir}/phpmyadmin"
    
    if not os.path.exists(pma_dir):
        os.system(f"cd {web_dir} && wget https://files.phpmyadmin.net/phpMyAdmin/5.2.1/phpMyAdmin-5.2.1-all-languages.zip")
        os.system(f"cd {web_dir} && unzip phpMyAdmin-5.2.1-all-languages.zip > /dev/null")
        os.system(f"cd {web_dir} && mv phpMyAdmin-5.2.1-all-languages phpmyadmin")
        os.system(f"cd {web_dir} && rm phpMyAdmin-5.2.1-all-languages.zip")
    
    # TẠO FILE CONFIG ĐỂ ĐĂNG NHẬP KHÔNG CẦN MẬT KHẨU
    print("[*] Đang cấu hình quyền truy cập cho phpMyAdmin...")
    config_path = f"{pma_dir}/config.inc.php"
    pma_config = """<?php
$cfg['Servers'][1]['auth_type'] = 'config';
$cfg['Servers'][1]['user'] = 'root';
$cfg['Servers'][1]['password'] = '';
$cfg['Servers'][1]['host'] = '127.0.0.1';
$cfg['Servers'][1]['AllowNoPassword'] = true;
$cfg['DefaultLang'] = 'vi';
?>"""
    with open(config_path, "w") as f:
        f.write(pma_config)

    # 5. Khởi động Web Server
    print("\033[1;36m[5/5] Đang bật Web Server tại Port 8080...\033[0m")
    os.system("pkill httpd")
    os.system("httpd")

    print("\033[1;32m===============================================")
    print("[+] HOÀN TẤT! BẠN CÓ THỂ SỬA SQL BÂY GIỜ")
    print("➤ Link Web: http://127.0.0.1:8080/phpmyadmin")
    print("➤ Chọn Database 'dragonball' bên trái để sửa")
    print("===============================================\033[0m")
    input("Nhấn Enter để quay lại Menu...")

if __name__ == "__main__":
    setup_database()
