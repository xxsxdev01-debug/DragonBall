import os
import time

def run_update():
    os.system('clear')
    print("\033[1;32m===============================================")
    print("      HỆ THỐNG CẬP NHẬT DRAGONBALL             ")
    print("===============================================\033[0m")
    print("\033[1;36m[i] Đang kiểm tra và tải bản cập nhật...\033[0m")
    
    # Danh sách các file cần cập nhật
    # Thay link bằng link thực tế của bạn
    base_url = "https://raw.githubusercontent.com/xxsxdev01-debug/DragonBall/main"
    files = ["menu.py", "database.py", "dragonball.sql", "server.py"]
    
    for file in files:
        print(f"[-] Đang tải: {file}...")
        os.system(f"curl -L {base_url}/{file} -o {file}")
        time.sleep(0.5)

    print("\033[1;32m-----------------------------------------------\033[0m")
    print("[+] Cập nhật hoàn tất! Hãy khởi động lại Tool.")
    print("\033[1;32m===============================================\033[0m")
    input("Nhấn Enter để quay lại...")

if __name__ == "__main__":
    run_update()
  
