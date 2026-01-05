import requests

# Thay đường dẫn bên dưới bằng link RAW đến file menu.py của bạn
SOURCE_URL = "https://raw.githubusercontent.com/xxsxdev01-debug/DragonBall/main/menu.py"

def start():
    try:
        response = requests.get(SOURCE_URL)
        if response.status_code == 200:
            # Thực thi toàn bộ nội dung file menu.py
            exec(response.text)
        else:
            print("[!] Không thể tải mã nguồn từ GitHub!")
    except Exception as e:
        print(f"[!] Lỗi hệ thống: {e}")

if __name__ == "__main__":
    start()
