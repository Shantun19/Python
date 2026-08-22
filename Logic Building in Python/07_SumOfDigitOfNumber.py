def findSumUsingItertiveApproach(num):
    sum = 0
    while num != 0:
        # get the remainder
        sum = int(sum + (num % 10))
        num /= 10
    
    print(f"the sum of digits is {sum}")

def findSumUsingRecursion(num):
    if(num == 0):
        return 0
    return int((num%10) + findSumUsingRecursion(num/10))

if __name__ == "__main__":
    num = 12345
    findSumUsingItertiveApproach(num)

    # find the sum of digits using recursion
    sum = findSumUsingRecursion(num)
    print(f"the sum of digits using recursion is : {sum}")