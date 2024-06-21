# a=input("Enter a string")
# b=input("Enter another string")
#
# print(a+" "+b)

srt = "Hello World"

# for i in srt:
#     print(i)


# print(srt.upper())
# print(srt.lower())
# print(srt.swapcase())
# print(srt.capitalize())

print(srt.title())
print(srt[6])
print(srt[:5])
print(srt[-5:])
print(srt[2:])
print(srt[-2:])
print(srt[1:7])
print(srt[::2])
print(srt[1::2])
print(srt[2::2])

data = ' this is my strINg '
print(len(data))
print(data.lstrip())
print(data.rstrip())
print(data.strip())

print(data.replace(" ", ''))
print(data.replace('s', '*'))
print(data.replace("is", 'IS').replace('IN', 'in'))
