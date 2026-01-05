import os
import time

def setup_database():
    os.system('clear')
    print("\033[1;32m===============================================")
    print("      HỆ THỐNG TỰ ĐỘNG SQL & PHPMYADMIN        ")
    print("===============================================\033[0m")

    # Cấu hình thông số - Pass trống để là ""
    DB_NAME = "dragonball"
    DB_USER = "root"
    DB_PASS = ""  # Sửa lại ở đây thành ""
    DB_HOST = "127.0.0.1"
    DB_PORT = "3306"

    # 1. LỆNH XÓA SẠCH FILE CŨ (Để cài lại từ đầu)
    print("\033[1;31m[*] Đang xóa sạch dữ liệu cũ để làm mới...\033[0m")
    os.system("pkill -9 httpd mariadbd mysqld")
    os.system(f"mariadb -u root -e 'DROP DATABASE IF EXISTS {DB_NAME};'")
    os.system("rm -f dragonball.sql")
    # Xóa cả phpmyadmin cũ để tránh lỗi giải nén
    web_dir = os.path.expandvars("$PREFIX/share/apache2/default-site/htdocs")
    os.system(f"rm -rf {web_dir}/phpmyadmin")

    # 2. Cài đặt các gói
    print(f"\033[1;36m[1/5] Cài đặt gói hệ thống...\033[0m")
    os.system("pkg install mariadb apache2 php php-apache wget unzip curl -y")

    # 3. Khởi động MySQL
    print(f"\033[1;36m[2/5] Khởi động MariaDB Server (Port {DB_PORT})...\033[0m")
    mysql_data_dir = os.path.expandvars("$PREFIX/var/lib/mysql")
    if not os.path.exists(mysql_data_dir):
        os.system("mysql_install_db")
    
    os.system(f"mysqld_safe --datadir={mysql_data_dir} --port={DB_PORT} > /dev/null 2>&1 &")
    time.sleep(8) 

    # 4. Nạp dữ liệu và Cấp quyền
    print(f"\033[1;36m[3/5] Đang nạp SQL và cấp quyền user '{DB_USER}'...\033[0m")
    url_sql = "https://raw.githubusercontent.com/xxsxdev01-debug/DragonBall/main/dragonball.sql"
    os.system(f"curl -L {url_sql} -o dragonball.sql")
    
    os.system(f"mariadb -u root -e 'CREATE DATABASE IF NOT EXISTS {DB_NAME};'")
    os.system(f"mariadb -u root {DB_NAME} < dragonball.sql")
    
    # Lệnh cấp quyền quan trọng: dùng IDENTIFIED BY '' để xác nhận pass rỗng
    os.system(f"mariadb -u root -e \"GRANT ALL PRIVILEGES ON *.* TO '{DB_USER}'@'localhost' IDENTIFIED BY '{DB_PASS}'; FLUSH PRIVILEGES;\"")
    
    print(f"\033[1;32m[V] Đã tạo thành công Database: {DB_NAME}\033[0m")

    # 5. Cấu hình phpMyAdmin và Apache
    print(f"\033[1;36m[4/5] Cấu hình giao diện Web...\033[0m")
    # Cài đặt phpMyAdmin (Đã xóa ở trên nên giờ cài mới 100%)
    os.system(f"cd {web_dir} && wget https://files.phpmyadmin.net/phpMyAdmin/5.2.1/phpMyAdmin-5.2.1-all-languages.zip")
    os.system(f"cd {web_dir} && unzip phpMyAdmin-5.2.1-all-languages.zip > /dev/null")
    os.system(f"cd {web_dir} && mv phpMyAdmin-5.2.1-all-languages phpmyadmin && rm *.zip")

    # Ghi file config phpMyAdmin với pass rỗng
    config_file = f"{web_dir}/phpmyadmin/config.inc.php"
    with open(config_file, "w") as f:
        f.write(f"<?php $cfg['Servers'][1]['auth_type'] = 'config'; $cfg['Servers'][1]['user'] = '{DB_USER}'; $cfg['Servers'][1]['password'] = '{DB_PASS}'; $cfg['Servers'][1]['host'] = '{DB_HOST}'; $cfg['Servers'][1]['AllowNoPassword'] = true; ?>")

    # Sửa lỗi Apache hiện danh sách file (Index Of)
    httpd_conf = os.path.expandvars("$PREFIX/etc/apache2/httpd.conf")
    os.system(f"sed -i 's/#LoadModule php_module/LoadModule php_module/' {httpd_conf}")
    os.system(f"grep -q \"AddType application/x-httpd-php\" {httpd_conf} || echo \"AddType application/x-httpd-php .php\" >> {httpd_conf}")

    os.system("httpd")

    print("\033[1;32m===============================================")
    print("      THIẾT LẬP THÀNH CÔNG (ĐÃ LÀM SẠCH)       ")
    print("===============================================")
    print(f" ➤ Database Name: {DB_NAME}")
    print(f" ➤ MariaDB User: {DB_USER}")
    print(f" ➤ MariaDB Pass: \"{DB_PASS}\"") # Hiển thị dấu "" cho rõ ràng
    print(f" ➤ MySQL Port:   {DB_PORT}")
    print(" ----------------------------------------------")
    print(" ➤ Link Web: http://127.0.0.1:8080/phpmyadmin/")
    print("===============================================\033[0m")
    input("Nhấn Enter để quay lại Menu...")

if __name__ == "__main__":
    setup_database()
    
