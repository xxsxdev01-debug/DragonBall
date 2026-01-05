import os
import time
import requests

def run_update():
    os.system('clear')
    print("\033[1;32m===============================================")
    print("      HỆ THỐNG CẬP NHẬT TỰ ĐỘNG (BẢN FIX)      ")
    print("===============================================\033[0m")
    
    user = "xxsxdev01-debug"
    repo = "DragonBall"
    # Thêm tham số thời gian để tránh GitHub trả về kết quả cũ (Cache)
    api_url = f"https://api.github.com/repos/{user}/{repo}/contents/?t={int(time.time())}"
    raw_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

    print("\033[1;36m[i] Đang quét toàn bộ danh sách file từ GitHub...\033[0m")
    
    try:
        # Gửi request với Header để tránh bị Cache
        headers = {'Cache-Control': 'no-cache'}
        response = requests.get(api_url, headers=headers)
        
        if response.status_code == 200:
            contents = response.json()
            
            # Đếm số file tìm thấy
            file_count = sum(1 for item in contents if item['type'] == 'file')
            print(f"\033[1;33m[+] Tìm thấy tổng cộng {file_count} tệp tin.\033[0m")
            print("-----------------------------------------------")

            for item in contents:
                if item['type'] == 'file':
                    filename = item['name']
                    print(f"[-] Đang tải bản mới nhất: {filename}...")
                    # Sử dụng thêm -H 'Cache-Control: no-cache' trong curl
                    os.system(f"curl -H 'Cache-Control: no-cache' -L {raw_url}/{filename} -o {filename}")
                    time.sleep(0.1)
            
            print("\033[1;32m-----------------------------------------------\033[0m")
            print(f"[+] Đã đồng bộ hoàn tất toàn bộ {file_count} tệp tin!")
        else:
            print(f"\033[1;31m[!] Lỗi: GitHub trả về mã {response.status_code}\033[0m")
            
    except Exception as e:
        print(f"\033[1;31m[!] Lỗi kết nối: {e}\033[0m")

    print("\033[1;32m===============================================\033[0m")
    input("Nhấn Enter để quay lại Menu...")

if __name__ == "__main__":
    run_update()
    
