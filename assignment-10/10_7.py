'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

import json

# Serialize/Deserialize Employee object
emp = {
    "empcode": "E101",
    "empname": "Piyush",
    "doj": "2023-08-01",
    "salary": 65000
}

with open("emp.json", "w") as f:
    json.dump(emp, f)

with open("emp.json", "r") as f:
    newemp = json.load(f)

print(newemp)
