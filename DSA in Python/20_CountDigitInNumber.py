import math

def countDigitsInNumber(num):
    count_digit = 0
    while num != 0:
        count_digit += 1
        num //= 10
    return count_digit

def countDigitsInNumberUsingRecursion(num):
    if num == 0:
        return 0
    return 1 + countDigitsInNumberUsingRecursion(num//10)

def countDigitsInNumberUsingMathematicsFormula(num):
    # using the log function
    num = abs(num)
    if num == 0:
        return 1
    return math.floor(math.log10(num) + 1)

if __name__ == "__main__":
    num = int(input("Enter any Number !! "))

    # count the number of digits from a number using the iterative approach.
    print("The Number of digits in {num} is" , countDigitsInNumber(num))

    # count the number of digits from a number using the recursive approach.
    print("The Number of digits in {num} is" , countDigitsInNumberUsingRecursion(num))

    # count the number of digits from a number using the mathematics formula.
    print("The Number of digits in {num} is" , countDigitsInNumberUsingMathematicsFormula(num))

