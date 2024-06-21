# Concatenation of List
programmingLanguage = [2021,'Java' 'C#','Python',True, False, 'Java']
programmingLanguage_latest = ['PHP','Ruby']
final_list = programmingLanguage + programmingLanguage_latest
print (final_list)
print (len(final_list))

#Write Operations on List

# Update Value on ListAndTuple
programmingLanguage[2] = "C++"
print("******************** Updated ListAndTuple *********************")
print (programmingLanguage)

# Insert Values to List
programmingLanguage.insert(2, "PHP LANGUAGE")
print("******************** Added Value in the ListAndTuple *********************")
print (programmingLanguage)

# Delete value from the List
programmingLanguage.remove('Java')
print("******************** Deleted Value from the ListAndTuple *********************")
print (programmingLanguage)