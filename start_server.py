import os
import time
import subprocess

def main():
    os.system('clear')
    print("\033[1;32m===============================================")
    print("      HỆ THỐNG KHỞI CHẠY SERVER DRAGONBALL     ")
    print("      (FIXED: DRIVER & TIMEZONE)               ")
    print("===============================================\033[0m")

    jar_file = "NgocRongOnline.jar"
    driver_file = "mysql-driver.jar"
    # Lớp khởi chạy (Main Class) bạn đã cung cấp từ Log lỗi trước đó
    main_class = "nro.models.server.ServerManager"

    if not os.path.exists(jar_file):
        print(f"\033[1;31m[!] Lỗi: Không tìm thấy {jar_file}!\033[0m")
        return

    # TỰ ĐỘNG KIỂM TRA VÀ TẢI DRIVER NẾU THIẾU
    if not os.path.exists(driver_file):
        print("\033[1;33m[i] Đang tải thư viện Driver MySQL tương thích MariaDB 12...\033[0m")
        url_driver = "https://repo1.maven.org/maven2/mysql/mysql-connector-java/5.1.49/mysql-connector-java-5.1.49.jar"
        os.system(f"curl -L {url_driver} -o {driver_file}")

    print("\033[1;36m[i] Đang chuẩn bị môi trường khởi chạy chi tiết...\033[0m")
    
    current_dir = os.getcwd()
    
    # NÂNG CẤP LỆNH CHẠY:
    # Sử dụng -cp để nạp Driver bên ngoài đè lên Driver cũ trong JAR
    # Thêm -Duser.timezone=UTC để fix lỗi múi giờ của MariaDB
    inner_cmd = (
        f"cd {current_dir};"
        f"printf '\\033[1;34m[SYSTEM] Đang khởi chạy Server tại: {current_dir}\\n';"
        f"printf '\\033[1;32m[INFO] Tài nguyên: 512MB RAM | Múi giờ: UTC\\n';"
        f"printf '\\033[1;32m[INFO] Driver: {driver_file} (External)\\n';"
        f"printf '\\033[1;37m-----------------------------------------------\\n\\n';"
        f"java -Xmx512M -Duser.timezone=UTC -cp \"{driver_file}:{jar_file}\" {main_class};"
        f"printf \"\\n\\033[1;31m[!] SERVER ĐÃ DỪNG HOẶC GẶP LỖI XUNG ĐỘT!\\n\";"
        f"printf \"\\033[1;33m[?] Nhấn Enter để đóng Session này... \";"
        f"read"
    )

    # Gửi lệnh chạy sang Session mới
    launch_cmd = f"am startservice --user 0 -a com.termux.service_execute -n com.termux/com.termux.app.TermuxService -e com.termux.execute.command \"{inner_cmd}\""
    
    os.system(launch_cmd)

    print("\033[1;33m[i] Đang kiểm tra tín hiệu từ Session mới...\033[0m")
    time.sleep(3) # Tăng thời gian chờ để Java kịp nạp
    
    # Kiểm tra tiến trình Java (kiểm tra cả classpath)
    check_process = os.popen(f"pgrep -f {jar_file}").read()
    
    if check_process:
        print("\033[1;32m[+] THÀNH CÔNG: Server đã hoạt động tại Session 2.\033[0m")
    else:
        print("\033[1;31m[!] CẢNH BÁO: Session đã mở nhưng chưa thấy tiến trình Java.\033[0m")
        print("\033[1;33m    Gợi ý: Hãy vuốt sang Session 2 để kiểm tra lỗi log trực tiếp.\033[0m")

    print("-----------------------------------------------")
    
    while True:
        print("\n\033[1;37mBẢNG ĐIỀU KHIỂN:\033[0m")
        print(" [1]. Xem trạng thái RAM (Hệ thống)")
        print(" [2]. Xem danh sách Port đang mở (Netstat)")
        print(" [3]. Mở Admin Panel (admin.sh)")
        print(" [0]. Quay lại Menu chính")
        
        choice = input("\n\033[1;36m➤ Nhập lựa chọn: \033[0m")
        
        if choice == '1':
            os.system("free -h")
        elif choice == '2':
            os.system("netstat -tunlp")
        elif choice == '3':
            if os.path.exists("admin.sh"):
                os.system("bash admin.sh")
            else:
                print("\033[1;31m[!] Lỗi: Không tìm thấy file admin.sh\033[0m")
        elif choice == '0':
            break
        else:
            print("[!] Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
