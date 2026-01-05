import requests

# ID file mới của bạn: 1t5IX3VTl66sB9Ed-073LLvHavFgrGxr2
# Link này đã được chuyển sang dạng trực tiếp tải (Direct Download)
SOURCE_URL = "https://docs.google.com/uc?export=download&id=1t5IX3VTl66sB9Ed-073LLvHavFgrGxr2"

def start():
    try:
        print("\033[1;36m[i] Đang tải mã nguồn từ Google Drive mới...\033[0m")
        
        # Gửi yêu cầu tải file
        response = requests.get(SOURCE_URL, stream=True)
        
        if response.status_code == 200:
            # Nếu file là code Python (.py)
            source_code = response.text
            print("\033[1;32m[+] Tải thành công! Đang thực thi...\033[0m")
            exec(source_code)
        else:
            print("\033[1;31m[!] Lỗi: Không thể tải file. Mã lỗi: {}\033[0m".format(response.status_code))
            print("\033[1;33m[?] Hãy đảm bảo bạn đã bật 'Bất kỳ ai có liên kết đều có thể xem' trên Drive.\033[0m")
            
    except Exception as e:
        print(f"\033[1;31m[!] Lỗi khởi động: {e}\033[0m")

if __name__ == "__main__":
    start()
