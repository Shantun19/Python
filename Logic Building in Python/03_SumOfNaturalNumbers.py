def findSumOfNaturalsNumbers(n):
    # iterative way to get the sum of n naturals numbers 
    sum = 0
    for i in range(1 , n+1):
        sum += i
    print(f"the sum is {sum}")

def findSumOfNaturalsNumbers_usingMathFunction(n):
    sum = (n*(n+1)) // 2
    print(f"the sum of {n} naturals no. is {sum}")

def findSumOfNaturalsNumbers_recusrion(n):
    # base condition
    if(n == 0):
        return 0
    return n + (findSumOfNaturalsNumbers_recusrion(n-1))


if __name__ == "__main__":
    n = 10
    findSumOfNaturalsNumbers(n)

    # find the sum of n naturals no. using the mathematical function
    findSumOfNaturalsNumbers_usingMathFunction(n)

    # find the sum of n natural no. using the recursion
    sum = findSumOfNaturalsNumbers_recusrion(n)
    print(f"the sum using recursion is {sum}")