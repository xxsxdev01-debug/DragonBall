#!/bin/bash

# 1. Cấp quyền bộ nhớ
termux-setup-storage

# 2. Cài đặt Python và các công cụ (Sửa lỗi command not found)
echo -e "\e[1;32m[i] Đang cài đặt môi trường... Vui lòng đợi.\e[0m"
pkg update -y
pkg install -y python openjdk-17 wget unzip python-is-python3

# 3. Cài đặt thư viện Python
pip install requests mysql-connector-python

# 4. Tải DATA nặng từ Release (498MB)
# Link lấy từ mục Assets trong ảnh của bạn
DATA_URL="https://github.com/xxsxdev01-debug/DragonBall/releases/download/V1.0/data.zip"

if [ ! -d "data" ]; then
    echo -e "\e[1;33m[i] Đang tải data.zip từ Release...\e[0m"
    wget -q --show-progress "$DATA_URL" -O data.zip
    
    echo -e "\e[1;32m[+] Đang giải nén dữ liệu game...\e[0m"
    unzip -o data.zip
    rm data.zip
fi

# 5. Cấp quyền chạy file
chmod +x *.sh

clear
echo -e "\e[1;32m==============================================="
echo -e "      CÀI ĐẶT HOÀN TẤT - HỆ THỐNG SẴN SÀNG     "
echo -e "===============================================\e[0m"

# 6. Đếm ngược 5 giây và tự động chạy
for i in {5..1}
do
    echo -ne "\e[1;33m[!] Hệ thống sẽ tự động khởi chạy sau $i giây...\r\e[0m"
    sleep 1
done

echo -e "\n\e[1;32m[+] Đang khởi chạy Tool...\e[0m"
python3 run.py
