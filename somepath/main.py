import json 
import os
 
manifest_path = './values.json'
with open(manifest_path,'r') as manifest_file:
    data = json.load(manifest_file)
print(data)
    
new_name = data["regions"]["region"]["resource_group"]

for key, value in new_name.items():
    print(f"Key: {key}, Value: {value}")

tfdatapath = './django/modules/terr.tfvars'
with open(tfdatapath,'r') as tfvarfile:
    tfdata = json.load(tfvarfile)

print(tfdata)
