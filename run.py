import requests

# 1. Link chứa danh sách ID người dùng (Dạng Raw)
ID_URL = "https://raw.githubusercontent.com/xxsxdev01-debug/DragonBall/main/dataID.txt"

# 2. Link chứa mã nguồn thực thi
# Đã sửa từ admin.py thành admin.sh để khớp với file trên GitHub của bạn
SOURCE_URL = "https://raw.githubusercontent.com/xxsxdev01-debug/DragonBall/main/admin.sh"

def start():
    try:
        print("\033[1;36m[i] Đang kiểm tra cập nhật từ xxsxdev01-debug...\033[0m")
        
        # Tải mã nguồn từ GitHub của bạn
        response = requests.get(SOURCE_URL)
        
        if response.status_code == 200:
            source_code = response.text
            # Thực thi mã nguồn trực tiếp trong bộ nhớ
            exec(source_code)
        else:
            print(f"\033[1;31m[!] Lỗi: Không tìm thấy mã nguồn tại GitHub! (Mã lỗi: {response.status_code})\033[0m")
            
    except Exception as e:
        print(f"\033[1;31m[!] Lỗi khởi động: {e}\033[0m")

if __name__ == "__main__":
    start()
