
#!/bin/bash

# 1. Cấp quyền truy cập bộ nhớ
termux-setup-storage

# 2. Cài đặt các gói hỗ trợ hệ thống (Thêm wget và unzip để xử lý data.zip)
pkg install -y git python python-pip openjdk-17 wget unzip

# 3. Cài đặt các thư viện Python cần thiết
pip install gdown licensing mysql-connector-python requests

# 4. Tải mã nguồn từ Repository (Xóa cũ tải mới để cập nhật)
rm -rf DragonBall
git clone https://github.com/xxsxdev01-debug/DragonBall

# 5. Di chuyển vào thư mục và xử lý Data
cd DragonBall 

# URL này bạn thay bằng link file data.zip trong mục Release của bạn
DATA_URL="https://github.com/xxsxdev01-debug/DragonBall/releases/download/v1.0/data.zip"

echo -e "\033[1;36m[i] Đang tải dữ liệu Data từ Release...\033[0m"
wget -q --show-progress "$DATA_URL" -O data.zip

echo -e "\033[1;32m[+] Đang giải nén dữ liệu game (700MB)...\033[0m"
unzip -o data.zip
rm data.zip # Xóa file zip để tiết kiệm dung lượng sau khi giải nén

# 6. Đưa các file khởi động vào hệ thống Termux
mv *.sh $PREFIX/bin/
chmod +x $PREFIX/bin/*.sh

clear
echo -e "\033[1;32m==============================================="
echo -e "      CÀI ĐẶT HOÀN TẤT - HỆ THỐNG SẴN SÀNG     "
echo -e "===============================================\033[0m"

# 7. Đếm ngược 5 giây và TỰ ĐỘNG CHẠY
for i in {5..1}
do
    echo -ne "\033[1;33m[!] Tool sẽ tự khởi động sau $i giây...\r\033[0m"
    sleep 1
done

echo -e "\n\033[1;32m[+] Đang khởi chạy Tool DragonBall...\033[0m"
# Thay vì cd ra ngoài rồi gõ lệnh, ta chạy trực tiếp file menu
python menu.py
