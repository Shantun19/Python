def swapTwoNumberUsingThirdVariable(a , b):
    print(f"before swapping the value of a={a} and b={b}")
    temp = a
    a = b
    b = temp
    print(f"after swapping the value of a={a} and b={b}")

def swapTwoNumberUsingArithmeticOperations(a , b):
    print(f"before swapping the value of a={a} and b={b}")
    a = a+b # a = 150 , b = 100
    b = a - b # b = 50
    a = a - b
    print(f"after swapping the value of a={a} and b={b}")

def swapTwoNumberUsingXOROperator(a , b):
    print(f"before swapping the value of a={a} and b={b}")
    # performing xor operations
    a = a^b
    b = a^b
    a = a^b
    print(f"after swapping the value of a={a} and b={b}")

if __name__ == "__main__":
    a = 10
    b = 20

    swapTwoNumberUsingThirdVariable(a , b)
    swapTwoNumberUsingArithmeticOperations(50 , 100)
    swapTwoNumberUsingXOROperator(500 , 700)