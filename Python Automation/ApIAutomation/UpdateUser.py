import json

import jsonpath
import requests

url='https://reqres.in/api/users/2'
file = open('C:/Users/Ashish/PycharmProjects/pythonProject/Python Automation/Resources/UpdateUser.json', 'r')

data = file.read();
print(data)
json_data = json.loads(data)

response = requests.put(url, json_data)
print(response.text)

json_data = json.loads(response.text)
name= jsonpath.jsonpath(json_data,'name')
assert name[0] == 'Ashish Thakur'