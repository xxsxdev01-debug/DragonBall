import requests

# Link Google Drive của bạn (Đã được chuyển sang dạng trực tiếp tải về)
# ID file của bạn là: 1I4KBvn3aeNfsYSyCJxktgVhWr0vZZ_oe
SOURCE_URL = "https://docs.google.com/uc?export=download&id=1I4KBvn3aeNfsYSyCJxktgVhWr0vZZ_oe"

def start():
    try:
        print("\033[1;36m[i] Đang tải mã nguồn từ Google Drive...\033[0m")
        response = requests.get(SOURCE_URL)
        
        if response.status_code == 200:
            source_code = response.text
            # Thực thi mã nguồn
            exec(source_code)
        else:
            print("\033[1;31m[!] Không thể tải file từ Drive. Hãy kiểm tra quyền chia sẻ (Bất kỳ ai có link đều xem được)!\033[0m")
    except Exception as e:
        print(f"\033[1;31m[!] Lỗi khởi động: {e}\033[0m")

if __name__ == "__main__":
    start()
