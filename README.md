# unifi_devices_to_csv.py
Export UniFi devices to CSV

[NEW] We built a free web tool for this: https://export.hostifi.com

# Requirements
This has been tested on Linux based UniFi controllers only

# Instructions
cd /root

wget https://raw.githubusercontent.com/HostiFi/Export-UniFi-Devices-to-CSV/main/unifi_devices_to_csv.py

pip3 install pymongo

python3 unifi_devices_to_csv.py


Then SFTP to your server and download /root/devices.csv
