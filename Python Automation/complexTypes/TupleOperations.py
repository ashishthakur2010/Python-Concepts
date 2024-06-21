# Tuple in Python
# Data in placed in ( ) separated by comma(,)
# Can save multiple data of different data type
# Can fetch data by giving index (Can fetch 1 or multiple data)
# Support Only Read Operation, does not support Write operations.
# Loop though complete tuple to fetch data
# Find length of Tuple
# Concatenate multiple tuples


# Concatenation of Tuple
programmingLanguage = (2021,'Java' 'C#','Python',True, False, 'Java')
programmingLanguage_latest = ('PHP','Ruby')

final_Tuple = programmingLanguage + programmingLanguage_latest
print (final_Tuple)
print (len(final_Tuple))


#We CAN't modify are write the exsiting Tuple

#Read Operations on List
print(type(final_Tuple))
print(programmingLanguage)
print(programmingLanguage[3])
print(programmingLanguage[3:5])
print(programmingLanguage[2:])
print(programmingLanguage_latest[:3])


tupleLength = len(final_Tuple)

for i in range(0,tupleLength):
    print(final_Tuple[i])

for i in programmingLanguage:
    print(i)

# programmingLanguage[0]="hello" # TypeError: 'tuple' object does not support item assignment
# print(programmingLanguage)