#!/bin/bash

# 1. Cập nhật hệ thống và cài đặt môi trường
echo -e "\e[1;32m[i] Đang cài đặt môi trường hệ thống...\e[0m"
pkg update -y
pkg install -y git python openjdk-17 wget unzip python-is-python3

# 2. Cài đặt các thư viện Python cần thiết
echo -e "\e[1;36m[i] Đang cài đặt thư viện Python...\e[0m"
pip install requests mysql-connector-python

# 3. Tải DATA nặng từ Release (498 MB)
# Link lấy trực tiếp từ ảnh Asset của bạn
DATA_URL="https://github.com/xxsxdev01-debug/DragonBall/releases/download/V1.0/data.zip"

if [ ! -d "data" ]; then
    echo -e "\e[1;33m[i] Đang tải dữ liệu Data (498MB)... Vui lòng đợi.\e[0m"
    wget -q --show-progress "$DATA_URL" -O data.zip
    
    echo -e "\e[1;32m[+] Đang giải nén dữ liệu...\e[0m"
    unzip -o data.zip
    rm data.zip
fi

# 4. Cấp quyền cho các file script
chmod +x *.sh

clear
echo -e "\e[1;32m==============================================="
echo -e "      CÀI ĐẶT HOÀN TẤT - HỆ THỐNG SẴN SÀNG     "
echo -e "===============================================\e[0m"

# 5. Đếm ngược 5 giây và khởi chạy
for i in {5..1}
do
    echo -ne "\e[1;33m[!] Hệ thống sẽ tự động chạy sau $i giây...\r\e[0m"
    sleep 1
done

echo -e "\n\e[1;32m[+] Đang khởi chạy Tool...\e[0m"
# Chạy file run.py hoặc menu.py tùy theo code của bạn
python run.py
