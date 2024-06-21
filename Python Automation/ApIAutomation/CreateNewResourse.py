import json

import jsonpath
import requests

url ='https://reqres.in/api/users'


file = open('C:/Users/Ashish/PycharmProjects/pythonProject/Python Automation/Resources/CreateUser.json', 'r')
data = file.read()
request_json = json.loads(data)
print(request_json)


response = requests.post(url,request_json)
assert response.status_code==201


json_data = json.loads(response.text)
id= jsonpath.jsonpath(json_data,'id')
print(id)
print(id[0])