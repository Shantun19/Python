import math 

def countDigits(num):
    if num == 0:
        return 1
    return math.floor(math.log10(num) + 1)

def reverseTheNumber(num):
    if countDigits(num) == 1:
        return num

    reverseNumber = 0

    while num != 0:
        reverseNumber = (reverseNumber * 10) + (num % 10)
        num //= 10
    
    return reverseNumber

def reverseTheNumberUsingRecursion(reverseNumber , num):
    if num == 0:
        # when the actual number becomes 0 then simply return the reversed number.
        return reverseNumber
    reverseNumber = (reverseNumber * 10) + (num%10)
    return reverseTheNumberUsingRecursion(reverseNumber , num//10)

if __name__ == "__main__":
    num = int(input("Enter any Number "))
    # reverse the number using the recursive approach
    print('the reverse Number is ' , reverseTheNumber(num))

    # reverse the number using the recursion
    print('the reverse Number is ' , reverseTheNumberUsingRecursion(0 , num))