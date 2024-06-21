#finding String in another String

str = " This is a String which is been used for been testing"
print(str.find("been"))  # Return the lowest index in String
print(str.rfind('been'))  # Return the Highest index in String

lst = str.split("been")
lst1 = str.split()

# for c in lst:
#     print(c)
# print(len(lst))
# for x in lst1:
#     print(x)
# print(len(lst1))


a = 'Hello World'
b = "Hello World"
c = "World Hello"
d = "hello world"
e = " Hello world"


if(a==b):
    print(1)
else:
    print(-1)

if(a==c):
    print(2)
else:
    print(-2)

if(a.lower()==d):
    print(3)
else:
    print(-3)

if(a.lower()==e.lower().lstrip()):
    print(4)
else:
    print(-4)