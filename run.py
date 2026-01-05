import requests

# Link Google Drive mới của bạn
SOURCE_URL = "https://docs.google.com/uc?export=download&id=1t5IX3VTl66sB9Ed-073LLvHavFgrGxr2"

def start():
    try:
        print("\033[1;36m[i] Đang tải mã nguồn từ Google Drive...\033[0m")
        response = requests.get(SOURCE_URL)
        
        if response.status_code == 200:
            # Lọc bỏ ký tự NULL (\x00) để tránh lỗi "null bytes"
            source_code = response.text.replace('\x00', '')
            
            if len(source_code.strip()) == 0:
                print("\033[1;31m[!] File trống hoặc không phải code Python!\033[0m")
                return

            print("\033[1;32m[+] Tải thành công! Đang khởi động...\033[0m")
            exec(source_code)
        else:
            print(f"\033[1;31m[!] Lỗi tải: {response.status_code}\033[0m")
    except Exception as e:
        # Nếu vẫn lỗi null bytes, khả năng cao file là file ZIP nén
        print(f"\033[1;31m[!] Lỗi thực thi: {e}\033[0m")
        print("\033[1;33m[?] Gợi ý: Hãy đảm bảo file trên Drive là file .py thuần túy.\033[0m")

if __name__ == "__main__":
    start()
