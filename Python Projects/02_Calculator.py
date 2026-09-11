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

global_operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "//": floorDivision,
    "%": modulo,
    "**": exponential
}

def run_calculator(firstNumber , operator , secondNumber):
    if operator in global_operators:
        operationToPerform = global_operators[operator]
        return operationToPerform(firstNumber , secondNumber)
    return 'INVALID INPUTS'


if __name__ == "__main__":
    # take the first number as an input from the user
    firstNumber = int(input("Enter the first Number !"))
    # take the operator as an input from the user
    operator = input('choose operator - [+(Addition) , -(subtraction) , *(multiply) , /(Division) , //(floor division) , %(Modulo) , **(Exponential)]')
    # take the second number as an input from the user
    secondNumber = int(input('Enter the second Number'))

    result = run_calculator(firstNumber , operator , secondNumber)
    print("The Result is :" , result)