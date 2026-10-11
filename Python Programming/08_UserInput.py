# user input in python
# to get the input from the user we use input() function in python.

name = input()
print('My name is ' , name)

age = input("Enter your age !!") # you can also pass the string inside the input function
print("the input age is ", age)

# when you take the input from the user by default it stores the value in the form of string
marks = input("Enter your marks")
print(type(marks)) # <class , str>

# you need to explicitly conver the data type of the input like:
percentange = int(input("Enter your perentage !!"))
print(type(percentange)) # <class , int>
print(percentange)
