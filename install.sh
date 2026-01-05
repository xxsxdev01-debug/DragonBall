#!/bin/bash

# 1. Cấp quyền truy cập bộ nhớ
termux-setup-storage

# 2. Cập nhật và cài đặt các gói hỗ trợ
pkg update -y
pkg install -y git python python-pip openjdk-17 wget unzip

# 3. Cài đặt các thư viện Python (Dùng python3 để tránh lỗi)
python3 -m pip install --upgrade pip
python3 -m pip install gdown licensing mysql-connector-python requests

# 4. Tải mã nguồn từ Repository
cd ~
rm -rf DragonBall
git clone https://github.com/xxsxdev01-debug/DragonBall

# 5. Di chuyển vào thư mục và xử lý Data
cd DragonBall 

# URL file data.zip
DATA_URL="https://github.com/xxsxdev01-debug/DragonBall/releases/download/V1.0/data.zip"

echo -e "\033[1;36m[i] Đang tải dữ liệu Data từ Release...\033[0m"
wget -q --show-progress "$DATA_URL" -O data.zip

if [ -f "data.zip" ]; then
    echo -e "\033[1;32m[+] Đang giải nén dữ liệu game (700MB)...\033[0m"
    unzip -o data.zip
    rm data.zip
fi

# 6. Đưa các file khởi động vào hệ thống Termux
# Lưu ý: Chỉ di chuyển file .sh KHÁC debug.sh để tránh lỗi đang chạy bị mất file
chmod +x *.sh
cp *.sh $PREFIX/bin/

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

echo -e "\n\033[1;32m[+] Đang khởi chạy Tool DragonBall bằng Python3...\033[0m"

# SỬA Ở ĐÂY: Dùng python3 thay vì python
python3 menu.py
