# unifi_devices_to_csv.py
Export UniFi devices to CSV

# Requirements
This has been tested on Linux based UniFi controllers only

# Instructions
cd /root
wget https://raw.githubusercontent.com/HostiFi/Export-UniFi-Devices-to-CSV/main/unifi_devices_to_csv.py
python3 unifi_devices_to_csv.py

Then SFTP to your server and download /root/devices.csv
