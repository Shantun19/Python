# strings in python - strings are the sequence of character that is stored inside the variable.
# to store the string we use double/single quotes - "" , ''.

firstName = "Harry"
lastName = "Potter"

print(firstName + " " + lastName)

# print - He said "I want to eat an apple"

string = "He said \"i want to eat an apple\""
string1 = 'He said "I want to eat an apple"'
print(string)
print(string1)

# if we have a multi-line string in python like
"""
hi my name is shantun
i am good 
and i am working as a sde
"""

# to print the above string in multi-line we use triple double/single quotes.
tempString = """
hi my name is shantun
i am good 
and i am working as a sde
"""
print(tempString)

# string indexing - in python string is an like an array of characters
studentName = "Peter"
print(studentName[0])
print(studentName[1])
print(studentName[2])
print(studentName[3])
print(studentName[4])
# print(studentName[5]) # IndexError: string index out of range

# for loop with string 
tempString = """
hi my name is shantun
i am good 
and i am working as a sde
"""
for character in tempString:
    print(character)

# string slicing in python - to get subset of string from the existing parent string
# in python if we do slicing we use square brackets  - [start_index : last_index - 1]
student_names = "Marry,shubham,peter"
# fetch the startung five character
print(student_names[0:5]) # the last index was not included

# to get the length of the string
print(len(student_names[0:5]))
print(len(student_names[:5])) # if you not include the 0 python by default include 9 at the starting !

# negative slicing
temp = "Volcano"
print(temp[0:-3]) # output : Volc - what python does is this [0:len(temp)-3] = 7 - 3 = 4

"""
string methods in python
    - in python string is immutable means 
    - str = "Peter" - you can't change this string if you perform any method over this string then python return the new methods
------------------------
"""

str1 = "Pater"
print(len(str1)) # 5
print(str1.lower()) # pater
print(str1.upper()) # PATER

str2 = "Gara!!!!!"
print(str2.rstrip("!")) # remove the trailing ! means from the string

str3 = "12345Parker6789"
print(str3.replace("Parker" , "Mary")) # remove the all occurence from the string

str4 = "My name is harry osborn"
print(str4.split(" ")) # return the list of the string separated by the space - ['My', 'name', 'is', 'harry', 'osborn']
print(str4.capitalize()) # make the first character uppercase
print(str4.count("harry")) # how many times harry occurrs in the string - 1 time
print(str4.endswith("osborn")) # true

str5 = "Mary jane is a good girl and she is also a nice cook"
print(str5.find("is")) # return the first occurence of the provided string - if not occured then it return -1
print(str5.index("is")) # return the first occurence of the provided string - if not occured then it return throw the exception and this is similar to the find()
