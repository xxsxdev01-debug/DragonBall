import os
import time
import requests # Nếu chưa có hãy chạy: pkg install python-requests

def run_update():
    os.system('clear')
    print("\033[1;32m===============================================")
    print("      HỆ THỐNG CẬP NHẬT TỰ ĐỘNG ")
    print("===============================================\033[0m")
    
    # Thông tin kho lưu trữ
    user = "xxsxdev01-debug"
    repo = "DragonBall"
    api_url = f"https://api.github.com/repos/{user}/{repo}/contents/"
    raw_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

    print("\033[1;36m[i] Đang quét danh sách file cần cập nhật từ GitHub...\033[0m")
    
    try:
        # Lấy danh sách file qua GitHub API
        response = requests.get(api_url)
        if response.status_code == 200:
            contents = response.json()
            
            for item in contents:
                # Chỉ tải tệp tin (file), bỏ qua thư mục (dir)
                if item['type'] == 'file':
                    filename = item['name']
                    # Không tải lại chính file update.py nếu bạn muốn tránh xung đột khi đang chạy
                    # Hoặc cứ tải để cập nhật cả trình update
                    
                    print(f"[-] Đang Cập Nhật: {filename}...")
                    os.system(f"curl -L {raw_url}/{filename} -o {filename}")
                    time.sleep(0.2)
            
            print("\033[1;32m-----------------------------------------------\033[0m")
            print("[+] Đã cập nhật bản update mới nhất thành công!")
        else:
            print(f"\033[1;31m[!] Lỗi API: Không thể lấy danh sách file update (Code: {response.status_code})\033[0m")
            
    except Exception as e:
        print(f"\033[1;31m[!] Lỗi kết nối: {e}\033[0m")

    print("\033[1;32m===============================================\033[0m")
    input("Nhấn Enter để quay lại Menu...")

if __name__ == "__main__":
    # Đảm bảo máy đã cài thư viện requests
    if os.system("python -c 'import requests' > /dev/null 2>&1") != 0:
        os.system("pip install requests")
    run_update()
