import requests

# Thay link bằng link RAW của file menu.py của bạn
SOURCE_URL = "https://raw.githubusercontent.com/xxsxdev01-debug/DragonBall/main/menu.py"

def start():
    try:
        print("\033[1;36m[i] Đang kết nối tới GitHub...\033[0m")
        response = requests.get(SOURCE_URL)
        if response.status_code == 200:
            # Lệnh exec() sẽ chạy toàn bộ file menu.py bạn vừa sửa ở trên
            # Nó sẽ tự động gọi hàm main() nhờ đoạn if __name__ ở cuối
            exec(response.text, globals())
        else:
            print("\033[1;31m[!] Không thể tải file menu.py (Mã lỗi: {})\033[0m".format(response.status_code))
    except Exception as e:
        print(f"\033[1;31m[!] Lỗi hệ thống: {e}\033[0m")

if __name__ == "__main__":
    start()
