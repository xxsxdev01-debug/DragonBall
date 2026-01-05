
termux-setup-storage

pkg install -y git python python-pip openjdk-17

pip install gdown licensing mysql-connector-python requests

git clone https://github.com/xxsxdev01-debug/NgocRongTerrmux.git
clear
cd NgocRongTermux 
mv *.sh ~/../usr/bin/
chmod +x ~/../usr/bin/*.sh
cd
clear
debug.sh
