import os
import time

def main():
    os.system('clear')
    print("\033[1;32m===============================================")
    print("      HỆ THỐNG KHỞI CHẠY SERVER DRAGONBALL     ")
    print("===============================================\033[0m")

    if not os.path.exists("NgocRongOnline.jar"):
        print("\033[1;31m[!] Lỗi: Không tìm thấy Server.jar!\033[0m")
        return

    print("\033[1;36m[i] Đang gửi lệnh khởi chạy sang Session mới...\033[0m")
    
    # Lệnh mở Session mới và chạy Java
    # Lưu ý: Chúng ta thêm 'cd' vào thư mục hiện tại để đảm bảo Java tìm thấy file
    current_dir = os.getcwd()
    cmd = f"cd {current_dir} && java -Xmx512M -jar NgocRongOnline.jar"
    
    # Gửi lệnh chạy sang Session mới
    os.system(f"am startservice --user 0 -a com.termux.service_execute -n com.termux/com.termux.app.TermuxService -e com.termux.execute.command '{cmd}'")

    print("\033[1;33m[i] Vui lòng vuốt từ trái sang để xem Log ở Session 2.\033[0m")
    print("\033[1;32m[+] Khởi chạy hoàn tất!\033[0m")
    print("-----------------------------------------------")
    
    # Menu điều khiển sau khi chạy
    while True:
        print("\n\033[1;37mCHỌN THAO TÁC TIẾP THEO:\033[0m")
        print(" [1]. Mở Admin Panel (admin.sh)")
        print(" [0]. Quay lại Menu chính")
        
        choice = input("\n\033[1;36m➤ Nhập lựa chọn: \033[0m")
        
        if choice == '1':
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
  
