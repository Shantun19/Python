def add(firstNumber , secondNumber):
    return firstNumber + secondNumber

def subtract(firstNumber , secondNumber):
    return firstNumber - secondNumber

def multiply(firstNumber , secondNumber):
    return firstNumber * secondNumber

def divide(firstNumber , secondNumber):
    return firstNumber / secondNumber

def floorDivision(firstNumber , secondNumber):
    return firstNumber // secondNumber

def modulo(firstNumber , secondNumber):
    return firstNumber % secondNumber

def exponential(firstNumber , secondNumber):
    return firstNumber ** secondNumber

# Global operator table
operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "//": floorDivision,
    "%": modulo,
    "**": exponential
}

def run_calculator(firstNumber , operator , secondNumber):
    if operator in operators:
        operation = operators[operator]
        return operation(firstNumber , secondNumber)
    return 'Invalid Inputs !!'

if __name__ == "__main__":
    # take the first number from the user input
    firstNumber = int(input('Enter the first Number'))
    # take the operator from the user input
    operator = input('choose operator - [+(Addition) , -(subtraction) , *(multiply) , /(Division) , //(floor division) , %(Modulo) , **(Exponential)]')
    # take the second number as input from the user
    secondNumber = int(input('Enter the second Number'))

    result = run_calculator(firstNumber , operator , secondNumber)
    print('Result is :',result) 