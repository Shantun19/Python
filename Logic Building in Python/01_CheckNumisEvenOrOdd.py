# method to ckeck a num is even or odd
def checkNumIsEvenOrOdd(num):
    if(num % 2 == 0):
        print(num , "Is a even Number")
    else:
        print(num , "Is not even Number")

def checkNumIsEvenOrOdd_usingBitwise(num):
    if(num & 1 == 0):
        print(num , "Is a even Number")
    else:
        print(num , "Is not even Number")

if __name__ == "__main__":
    num = (int(input("Enter any value !")))
    # check a number is even or not using brute force approach
    checkNumIsEvenOrOdd(num)

    # check a number is even or not using the bitwise operator
    checkNumIsEvenOrOdd_usingBitwise(num)