import requests

# ID file Google Drive của bạn: 1t5IX3VTl66sB9Ed-073LLvHavFgrGxr2
# Đường dẫn này giúp tải trực tiếp nội dung file để thực thi
SOURCE_URL = "https://docs.google.com/uc?export=download&id=1t5IX3VTl66sB9Ed-073LLvHavFgrGxr2"

def start():
    try:
        print("\033[1;36m[i] Đang tải mã nguồn từ Google Drive mới...\033[0m")
        
        # Gửi yêu cầu tải file với headers để tránh bị Google chặn bot
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(SOURCE_URL, headers=headers, stream=True)
        
        if response.status_code == 200:
            # Lấy nội dung code Python
            source_code = response.text
            
            # Kiểm tra nếu file tải về là trang báo lỗi của Google (do chưa chia sẻ)
            if "Google Drive - Quota exceeded" in source_code or "sign in" in source_code.lower():
                print("\033[1;31m[!] Lỗi: Google Drive chặn tải hoặc file chưa được mở khóa công khai!\033[0m")
                return

            print("\033[1;32m[+] Tải thành công! Đang thực thi...\033[0m")
            # Thực thi mã nguồn tải về
            exec(source_code)
        else:
            print("\033[1;31m[!] Lỗi: Không thể tải file. Mã lỗi: {}\033[0m".format(response.status_code))
            print("\033[1;33m[?] Hãy đảm bảo bạn đã chỉnh: 'Bất kỳ ai có liên kết đều có thể xem'.\033[0m")
            
    except Exception as e:
        print(f"\033[1;31m[!] Lỗi khởi động: {e}\033[0m")

if __name__ == "__main__":
    start()
