
termux-setup-storage

# Cài đặt các gói hỗ trợ hệ thống
pkg install -y git python python-pip openjdk-17

# Cài đặt các thư viện Python cần thiết
pip install gdown licensing mysql-connector-python requests

# Tải mã nguồn từ Repository của bạn (Sửa từ JINN1368 sang xxsxdev01-debug)
git clone https://github.com/xxsxdev01-debug/DragonBall

clear

# Di chuyển vào thư mục DragonBall
cd DragonBall 

# Đưa các file khởi động vào hệ thống Termux
mv *.sh ~/../usr/bin/
chmod +x ~/../usr/bin/*.sh

# Quay lại thư mục gốc và khởi chạy lệnh của bạn
cd
clear
debug.sh
