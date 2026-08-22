# varaible are used to store the data or constant

# store integer value
a = 1
print(a)

# store the string value
name = "Peter Parker"
print(name)

# store boolean value 
isValid = True
print(isValid)

print("Hello" + " World")

# in python we can also check a variable belong to which data type
print("the type of a is : ", type(isValid)) # <class 'bool'>
print("the type of a is : ", type(a)) # <class 'int'>
print("the type of a is : ", type(1.2)) # <class 'float'>
print("the type of a is : ", type(name)) # <class 'str'>

# list - collection of different data element of different types
# list are mutable - we can update the list
list = [1,2.3,[-4,5],["apple" , "banana"]]
print("the list : " , list)

# tuple - same as list but they are immutable we cannot update the tuple
tuple1 = (("parrot" , "sparrow"),("lion" , "tiger"))
print(tuple1)

# dictonary is kind of mapped data also it is a king of object
dict1 = {
    "name" : "peter" , 
    "age" : 20, 
    "canVote" : True
}

print("the dict : ", dict1)
