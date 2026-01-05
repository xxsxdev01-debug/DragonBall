import requests

# Dùng link Raw GitHub để đảm bảo code sạch, không bị null bytes
SOURCE_URL = "https://raw.githubusercontent.com/xxsxdev01-debug/DragonBall/main/menu.py"

def start():
    try:
        response = requests.get(SOURCE_URL)
        if response.status_code == 200:
            # Thực thi nội dung chữ tải về
            exec(response.text)
        else:
            print("Lỗi: Không thể kết nối GitHub!")
    except Exception as e:
        print(f"Lỗi hệ thống: {e}")

if __name__ == "__main__":
    start()
