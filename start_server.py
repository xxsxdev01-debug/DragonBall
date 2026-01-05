import os
import time
import subprocess

def main():
    os.system('clear')
    print("\033[1;32m===============================================")
    print("      HỆ THỐNG KHỞI CHẠY SERVER DRAGONBALL     ")
    print("===============================================\033[0m")

    jar_file = "NgocRongOnline.jar"

    if not os.path.exists(jar_file):
        print(f"\033[1;31m[!] Lỗi: Không tìm thấy {jar_file}!\033[0m")
        return

    print("\033[1;36m[i] Đang chuẩn bị môi trường khởi chạy chi tiết...\033[0m")
    
    current_dir = os.getcwd()
    
    # NÂNG CẤP LỆNH CHẠY: 
    # 1. Hiển thị thông tin hệ thống trước khi chạy JAR
    # 2. Dùng 'trap' để giữ cửa sổ khi bị tắt đột ngột
    # 3. Thêm lệnh 'read' để Session không tự đóng khi có lỗi Java xảy ra
    
    inner_cmd = (
        f"printf '\\033[1;34m[SYSTEM] Đang khởi chạy Server tại: {current_dir}\\n';"
        f"printf '\\033[1;32m[INFO] Tài nguyên dự kiến: 512MB RAM\\n';"
        f"printf '\\033[1;37m-----------------------------------------------\\n\\n';"
        f"java -Xmx512M -jar {jar_file};"
        f"printf \"\\n\\033[1;31m[!] SERVER ĐÃ DỪNG HOẶC GẶP LỖI XUNG ĐỘT!\\n\";"
        f"printf \"\\033[1;33m[?] Nhấn Enter để đóng Session này... \";"
        f"read"
    )

    # Gửi lệnh chạy sang Session mới với cấu trúc chi tiết
    launch_cmd = f"am startservice --user 0 -a com.termux.service_execute -n com.termux/com.termux.app.TermuxService -e com.termux.execute.command \"{inner_cmd}\""
    
    os.system(launch_cmd)

    # Kiểm tra trạng thái thực tế
    print("\033[1;33m[i] Đang kiểm tra tín hiệu từ Session mới...\033[0m")
    time.sleep(2)
    
    # Kiểm tra xem tiến trình Java đã xuất hiện trong hệ thống chưa
    check_process = os.popen(f"pgrep -f {jar_file}").read()
    
    if check_process:
        print("\033[1;32m[+] THÀNH CÔNG: Server đã hoạt động tại Session 2.\033[0m")
    else:
        print("\033[1;31m[!] CẢNH BÁO: Session đã mở nhưng chưa thấy tiến trình Java.\033[0m")
        print("\033[1;31m    Hãy vuốt sang Session 2 để xem lỗi chi tiết.\033[0m")

    print("-----------------------------------------------")
    
    while True:
        print("\n\033[1;37mBẢNG ĐIỀU KHIỂN:\033[0m")
        print(" [1]. Xem trạng thái RAM (Hệ thống)")
        print(" [2]. Mở Admin Panel (admin.sh)")
        print(" [0]. Quay lại Menu chính")
        
        choice = input("\n\033[1;36m➤ Nhập lựa chọn: \033[0m")
        
        if choice == '1':
            os.system("free -h")
        elif choice == '2':
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
