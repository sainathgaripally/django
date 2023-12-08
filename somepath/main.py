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
    for line in tfdata:
        new_list.append(line)
        

print(tfdata)

print("########################################")

# with open('newfile', 'w') as w:
#     for text in new_list:
#         w.write(text)

print(new_list)

for key, value in new_name.items():
    for line in new_list:
        values = line.split('=')
        variable_name = values[0].strip()
        variable_value = values[1].strip()
        if(key == variable_name):
            # myindex = new_list.index(line)
            line.replace(variable_value, value) 


print(new_list)

wow = ["ab", "abc"]
t1 = "a"
t2 = "gg"
ttt = wow[0].replace(t1, t2)
wow[0] = ttt
# for i in wow:
#     wow[i] = wow[i].replace(t1, t2)

print(wow)

