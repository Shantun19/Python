if __name__ == "__main__":
    num1 = "1"
    num2 = "2"

    print(num1 + num2) #12

    str1 = "Peter"
    str2 = "Pareker"

    print(str1+str2) # PeterParker

    # explicit type casting - conversion done by programmer manually
    # if you want to typecast into number the number shoudl be in correct format if you do something like this - int("Pater") : then python throws an error !
    print(int(num1) + int(num2)) # 3

    # implicit conversion - python automatically perform the conversion internally.

    a = 7 # python automatically converts the a into integer data type
    print(type(a))

    b = 2.4 # python automatically converts the b into float data type
    print(type(b))

    sum = a + b # here is the addition of float and interger, so the sum is converted into the float data type menas - 7.0 + 2.4
    print(sum)
