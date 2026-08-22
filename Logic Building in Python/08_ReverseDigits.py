def reverseDigits(num):
    reversedNumber = 0

    while num != 0:
        reversedNumber = (reversedNumber * 10) + (num % 10)
        num //= 10

    return reversedNumber

def reverseDigitsUsingRecursion(reversed , num):
    # based condition 
    if(num == 0):
        return reversed
        
    reversed = (reversed * 10 + (num % 10))
    return reverseDigitsUsingRecursion(reversed , num//10)


if __name__ == "__main__":
    num = 12345
    print(f"The reversed number is: {reverseDigits(num)}")

    # reverse the number using recursion
    reversed = reverseDigitsUsingRecursion(0,num)
    print(f"the reversed number using recursion is : {reversed}")