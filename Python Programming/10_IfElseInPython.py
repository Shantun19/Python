# decision making in python

age = int(input("Enter the age !"))

if age >= 18:
    print("You can drive")
else:
    print("You cannot drive")

# elif statement 

applePrice = 200

if applePrice <= 200:
    print("We can buy an apple")
elif applePrice >= 200 and applePrice <= 400:
    print("we cannot buy an apple")
elif applePrice > 400:
    print("we need to take loan to buy an apple")

# nested if

num = 10

if num < 0:
    print("Number is Negative")
elif num > 0:
    if num >= 1 and num <= 10:
        print("the number is between 1-10")
    elif num > 10 and num <= 20:
        print("the number is between 10-20")
else:
    print("the number is bigger than 20")
