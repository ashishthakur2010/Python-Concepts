# Dictionary in Python
# Data in placed in { } separated by comma(,)
# Data is stored in Key-Value pair
# Keys and Values are separated by :, Keys must be unique
# Can save multiple data of different data type
# Can fetch data by giving key name
# Support Read and Write operations.
# Fetch all keys or values of dictionary
# Find length of Tuple


myData = {"a":100,"b":200,"c":'Hello',10:"world",'a':'replace Key "a"'}
print(myData)
print(type(myData))
print(len(myData))
print("a : "+myData['a'])
print("b : "+str(myData["b"]))
print("c : "+myData["c"])
print("10: "+myData[10])

print('******************** # add new Element in dic     ***********')
myData['email']="Ashish@gmail.com"
print(str(myData)+"\n")

print('******************** # Update an Element in dic     ***********')
myData['a']="Updating with new value"
print(str(myData)+"\n")

print('******************** # Delete an Element in dic     ***********')
myData.pop('a')
print(str(myData)+"\n")

print('******************** # fetch keys and values in dic     ***********')
print(myData.keys())
print(myData.values())