import requests

url = 'https://httpbin.org/get'
headerdata={'k1':'Head1','k2':'Head2'}
para={'name':'AT','email':'ashish@gmail.com'}
response = requests.get(url,headers=headerdata,params=para)
print(response.text)
print(response.status_code)