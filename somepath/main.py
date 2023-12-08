import json 
import os
import re
 
manifest_path = './values.json'
with open(manifest_path,'r') as manifest_file:
    data = json.load(manifest_file)
# print(data)
    
new_name = data["regions"]["region"]["resource_group"]

for key, value in new_name.items():
    print(f"Key: {key}, Value: {value}")

tfdatapath = '/home/azureuser/python_json_tfvars/django/modules/terr.tfvars'
with open(tfdatapath,'r') as tfvarfile:
    tfdata = tfvarfile.readlines()

print(tfdata)

print("########################################")

# for key in new_name.items():
#     for text in key:
#         temp = re.search(r)
#         if(key == temp):
#             print(text)

x = tfdata[0]
match = re.search(r'(\S+)\s*=\s*(\S+)', x)
print(match.group(1))
print(match.group(2))