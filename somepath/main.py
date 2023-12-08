import json 
import os
import re
 
manifest_path = './values.json'
with open(manifest_path,'r') as manifest_file:
    data = json.load(manifest_file)
    
new_name = data["regions"]["region"]["resource_group"]

print(new_name)

for key, value in new_name.items():
    print(f"Key: {key}, Value: {value}")

tfdatapath = '/home/azureuser/python_json_tfvars/django/modules/terr.tfvars'
with open(tfdatapath,'r') as tfvarfile:
    tfdata = tfvarfile.readlines()
    new_list =  []
    for line in tfdata:
        new_list.append(line)
        

print(tfdata)

print("########################################")

print(new_list)

for key, value in new_name.items():
    for line in new_list:
        values = line.split('=')
        variable_name = values[0].strip()
        variable_value = values[1].strip()
        if(key == variable_name):
            myindex = new_list.index(line)
            new_list[myindex] = new_list[myindex].replace(variable_value, value)

print(new_list)

with open('newfile', 'w') as w:
    for text in new_list:
        w.write(text)



