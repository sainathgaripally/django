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
    new_list =  []

print(tfdata)

print("########################################")

for key, value in new_name.items():
    for text in tfdata:
        values = text.split('=')
        variable_name = values[0].strip()
        variable_value = values[1].strip()
        if(key == variable_name):
            print(variable_name)

with open(newfile, w) as w:
    for text in tfdata:
        w.write(text)

