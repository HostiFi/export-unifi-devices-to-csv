import csv
from pymongo import MongoClient

#Creating a pymongo client
client = MongoClient('localhost', 27117)

#Getting the database instance
db = client['ace']
devices = db['device']
sites = db['site']
settings = db['setting']
device_rows = []
sites_dict = {}
hostname = "unknown"
for setting in settings.find():
    try:
        hostname = setting["hostname"]
        break
    except Exception as e:
        print(e)

for site in sites.find():
    try:
        print(site)
        print(site["desc"])
        sites_dict[str(site["_id"])] = {"desc": site["desc"], "name": site["name"]}
    except Exception as e:
        print(e)
print(sites_dict)

for device in devices.find():
    try:
        if "name" in device:
            device_name = device["name"]
        else:
            device_name = ""
        device_row = [device_name, device["model"], device["mac"], device["version"], sites_dict[device["site_id"]]["desc"], device["model_in_lts"], device["model_in_eol"], device["adopted"], "https://" + hostname + ":8443/manage/" + sites_dict[device["site_id"]]["name"] + "/devices"]
        device_rows.append(device_row)
        print(device_row)
    except Exception as e:
        print(e)

with open('devices.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Model", "Mac", "Firmware", "Site", "LTS", "EOL", "Adopted", "Link"])
    for device_row in device_rows:
           writer.writerow(device_row)
