import json
import requests
import jsonpath

# odics = "{'k1':'Ashish','k2':'util'}"
# json_results = json.load(odics)
# print(json_results)

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)
print(str(response) + '\n')
data = response.json()
print(str(data) + '\n')

content = response.content
print(str(content) + '\n')
print(str(response.status_code) + '\n')
assert response.status_code == 200;

print('********** headers *************')
print(str(response.headers) + '\n')
print(response.headers['Content-Type'])
print(response.headers['Date'])

print('********** Cookies *************')
print(response.encoding)
print(str(response.cookies) + '\n')

print('********** elapsed time *************')
print(str(response.elapsed) + '\n')


#Parse responce to json Format
# print('***  #Parse response to json Format  *****')
url = "https://reqres.in/api/users?page=2"
response1 = requests.get(url)

json_response = json.loads(response1.text)
print(json_response)

for i in range(0,6):
    var1=jsonpath.jsonpath(json_response,'data['+str(i)+'].id')
    print(var1[0])
    #assert var1[0] ==7

for i in response1.headers:
    print('Keys = '+str(i))
    print('Values = '+str(response1.headers[i]))
