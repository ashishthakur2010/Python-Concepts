# read data from file
obj = open("Py.txt",'a+')

print(obj.read())
print(obj.tell())
# print(obj.readline())
# print(obj.readline())

for i in obj.readline():
    print(i)


readLine = obj.readline()
print(obj.tell())

#while readLine != '': OR
while readLine:
    print(readLine)
    readLine = obj.readline()

#write data into the file
obj1 = open("Py.txt",'a')
obj1.write("This is 4th line\n")


while readLine !='':
    print(readLine)