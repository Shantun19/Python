def getSquare(n):
    return n*n

def findSumOfFirstNaturalsNumbers(num):
    # base condition
    if(num == 1 or num == 0):
        print(f"the sum of square of first {num} natural numbers are: {num}")
    sum = 0
    for i in range(1 , (num + 1)):
        sum += getSquare(i)
    
    print(f"the sum of square of first {num} natural numbers are: {sum}")

if __name__ == "__main__":
    num = 8
    # bruteforce approach to find the sum of square of first n naturals numbers
    findSumOfFirstNaturalsNumbers(num)