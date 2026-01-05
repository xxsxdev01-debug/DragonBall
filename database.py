
import os
import time

def setup_database():
    os.system('clear')
    print("\033[1;32m===============================================")
    print("      HỆ THỐNG TỰ ĐỘNG SQL & PHPMYADMIN        ")
    print("      (PHIÊN BẢN FIX LỖI MARIADB 12)           ")
    print("===============================================\033[0m")

    # Cấu hình thông số
    DB_NAME = "dragonball"
    DB_USER = "root"
    DB_PASS = "" 
    DB_HOST = "127.0.0.1"
    DB_PORT = "3306"

    # 1. LỆNH XÓA SẠCH FILE CŨ & TIẾN TRÌNH TREO
    print("\033[1;31m[*] Đang dọn dẹp hệ thống...\033[0m")
    os.system("pkill -9 httpd mariadbd mysqld mariadb")
    # Xóa file socket cũ để tránh lỗi port 3306 already in use
    os.system("rm -rf $PREFIX/var/run/mysqld.sock")
    
    # 2. Cài đặt các gói
    print(f"\033[1;36m[1/5] Cài đặt gói hệ thống...\033[0m")
    os.system("pkg install mariadb apache2 php php-apache wget unzip curl -y")

    # 3. CẤU HÌNH FIX LỖI BẢNG MÃ (QUAN TRỌNG NHẤT)
    print(f"\033[1;33m[*] Đang cấu hình Fix lỗi NullPointerException cho Java...\033[0m")
    cnf_path = os.path.expandvars("$PREFIX/etc/my.cnf.d/mariadb-server.cnf")
    os.system(f"mkdir -p $(dirname {cnf_path})")
    with open(cnf_path, "w") as f:
        f.write("[mysqld]\n")
        f.write("character-set-server=latin1\n")
        f.write("collation-server=latin1_swedish_ci\n")
        f.write("skip-character-set-client-handshake\n")
        f.write("innodb_strict_mode=0\n")
        f.write("lower_case_table_names=1\n")

    # 4. Khởi động MySQL
    print(f"\033[1;36m[2/5] Khởi động MariaDB Server...\033[0m")
    mysql_data_dir = os.path.expandvars("$PREFIX/var/lib/mysql")
    if not os.path.exists(mysql_data_dir):
        os.system("mysql_install_db")
    
    # Khởi động mariadbd trực tiếp thay vì mysqld_safe để ổn định trên Termux mới
    os.system(f"nohup mariadbd --skip-log-bin --lower-case-table-names=1 > /dev/null 2>&1 &")
    time.sleep(10) # Chờ database thức dậy

    # 5. Nạp dữ liệu (Sửa link Raw)
    print(f"\033[1;36m[3/5] Đang nạp SQL từ GitHub...\033[0m")
    url_sql = "https://raw.githubusercontent.com/xxsxdev01-debug/DragonBall/main/dragonball.sql"
    os.system(f"rm -f dragonball.sql")
    os.system(f"curl -L {url_sql} -o dragonball.sql")
    
    os.system(f"mariadb -u root -e 'DROP DATABASE IF EXISTS {DB_NAME};'")
    os.system(f"mariadb -u root -e 'CREATE DATABASE {DB_NAME} CHARACTER SET utf8 COLLATE utf8_general_ci;'")
    os.system(f"mariadb -u root {DB_NAME} < dragonball.sql")
    
    # Cấp quyền
    os.system(f"mariadb -u root -e \"GRANT ALL PRIVILEGES ON *.* TO '{DB_USER}'@'localhost'; FLUSH PRIVILEGES;\"")
    
    print(f"\033[1;32m[V] Đã tạo và nạp thành công Database: {DB_NAME}\033[0m")

    # 6. Cấu hình phpMyAdmin
    print(f"\033[1;36m[4/5] Cấu hình phpMyAdmin...\033[0m")
    web_dir = os.path.expandvars("$PREFIX/share/apache2/default-site/htdocs")
    os.system(f"rm -rf {web_dir}/phpmyadmin")
    os.system(f"mkdir -p {web_dir}")
    
    # Tải phpmyadmin nếu chưa có
    if not os.path.exists(f"{web_dir}/phpmyadmin"):
        os.system(f"cd {web_dir} && wget https://files.phpmyadmin.net/phpMyAdmin/5.2.1/phpMyAdmin-5.2.1-all-languages.zip")
        os.system(f"cd {web_dir} && unzip phpMyAdmin-5.2.1-all-languages.zip > /dev/null")
        os.system(f"cd {web_dir} && mv phpMyAdmin-5.2.1-all-languages phpmyadmin && rm *.zip")

    # Ghi file config phpMyAdmin
    config_file = f"{web_dir}/phpmyadmin/config.inc.php"
    with open(config_file, "w") as f:
        f.write(f"<?php $cfg['Servers'][1]['auth_type'] = 'config'; $cfg['Servers'][1]['user'] = '{DB_USER}'; $cfg['Servers'][1]['password'] = '{DB_PASS}'; $cfg['Servers'][1]['host'] = '{DB_HOST}'; $cfg['Servers'][1]['AllowNoPassword'] = true; ?>")

    # 7. Khởi động Web Server Apache
    print(f"\033[1;36m[5/5] Khởi động Apache Server...\033[0m")
    os.system("pkill -9 httpd")
    httpd_conf = os.path.expandvars("$PREFIX/etc/apache2/httpd.conf")
    os.system(f"sed -i 's/#LoadModule php_module/LoadModule php_module/' {httpd_conf}")
    os.system(f"grep -q \"AddType application/x-httpd-php\" {httpd_conf} || echo \"AddType application/x-httpd-php .php\" >> {httpd_conf}")
    os.system("httpd")

    print("\033[1;32m===============================================")
    print("      THIẾT LẬP HOÀN TẤT - SERVER SẴN SÀNG     ")
    print("===============================================")
    print(f" ➤ Database: {DB_NAME} (Đã Fix NullPointer)")
    print(f" ➤ Link Web: http://127.0.0.1:8080/phpmyadmin/")
    print(" ----------------------------------------------")
    print(" ➤ Lệnh chạy Game đề xuất:")
    print(" java -Xmx512M -Duser.timezone=UTC -cp \"mysql-driver.jar:NgocRongOnline.jar\" nro.models.server.ServerManager")
    print("===============================================\033[0m")
    input("Nhấn Enter để quay lại Menu...")

if __name__ == "__main__":
    setup_database()
    
