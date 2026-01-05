import requests

# 1. Link kiểm tra ID (Nếu muốn)
ID_URL = "https://raw.githubusercontent.com/xxsxdev01-debug/DragonBall/main/dataID.txt"
# 2. Link chứa code Menu (Phải là link Raw)
SOURCE_URL = "https://raw.githubusercontent.com/xxsxdev01-debug/DragonBall/main/admin.py"

def start():
    try:
        # Tải mã nguồn từ GitHub của bạn
        response = requests.get(SOURCE_URL)
        if response.status_code == 200:
            # Thực thi code
            exec(response.text)
        else:
            print("Không thể tải mã nguồn!")
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    start()
