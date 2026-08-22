# method to find the number is prime or not using the iterative approach
def checkIsPrime(num):
    if(num <= 2):
        return False
    for i in range(2 , num):
        if(num % i == 0):
            return False
    
    return True

def checkPrimeUsingSquareRootTrialDivision(num):
    # base condtion 
    if(num < 2):
        return False
    i = 2
    while(i*i <= num):
        if(num%i == 0):
            return False
    
    return True


if __name__ == "__main__":
    num = 3
    # iterative way to check the no. is prime or not 
    if(checkIsPrime(num)):
        print(f"{num} is prime !")
    else:
        print(f"{num} is not a prime number !")

    # Square Root Trial Division - O(√n) time and O(1) space
    if(checkPrimeUsingSquareRootTrialDivision(num)):
        print(f"{num} is prime using trial division method !")
    else:
        print(f"{num} is not a prime using trial division method !")
