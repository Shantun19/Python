# ============================================================
# What are Modules in Python?
# ============================================================
#
# A module in Python is simply a Python file (.py) that contains Python code.
# 
#
# A module can contain:
# - Variables
# - Functions
# - Classes
# - Statements
# - Constants
#
# Modules are used to organize code into separate files and make the code reusable.
#
#
# ------------------------------------------------------------
# Why do we use Modules?
# ------------------------------------------------------------
#
# Suppose we have a large Python program containing:
#
# - 100 functions
# - 50 classes
# - Many variables
# - Thousands of lines of code
#
# Keeping everything in one file can make the program difficult to understand and maintain.
#
# Instead, we can divide the code into different modules.
#
# For example:
#
# calculator.py
# student.py
# employee.py
# database.py
#
# Each file can contain code related to a particular functionality.
#
#
# ------------------------------------------------------------
# Example of a Module
# ------------------------------------------------------------
#
# Suppose we create a file called:
#
# calculator.py
#
# Inside calculator.py:
#
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
#
# Here, calculator.py is a MODULE.
#
# It contains two functions:
#
# - add()
# - subtract()
#
#
# ------------------------------------------------------------
# How do we use a Module?
# ------------------------------------------------------------
#
# We can use the 'import' keyword to import a module.
#
# Example:
#
# import calculator
#
# result = calculator.add(10, 20)
# print(result)
#
# Output:
# 30
#
# Here:
#
# import calculator
#
# tells Python that we want to use the calculator module.
#
# Then:
#
# calculator.add(10, 20)
#
# means we are calling the add() function from the
# calculator module.
#
#
# ------------------------------------------------------------
# Another way to import from a Module
# ------------------------------------------------------------
#
# Instead of importing the complete module, we can import specific functions from the module.
#
# Example:
#
# from calculator import add
#
# result = add(10, 20)
# print(result)
#
# Output:
# 30
#
# Here, we imported only the add() function from the calculator module.
#
#
# ------------------------------------------------------------
# Import Multiple Functions
# ------------------------------------------------------------
#
# We can also import multiple functions from a module.
#
# Example:
#
# from calculator import add, subtract
#
# print(add(10, 20))
# print(subtract(20, 10))
#
#
# ------------------------------------------------------------
# Built-in Modules
# ------------------------------------------------------------
#
# Python also provides many modules that are already available with Python.
#
# These are called BUILT-IN or STANDARD LIBRARY MODULES.
#
# Some commonly used modules are:
#
# - math
# - random
# - os
# - datetime
# - json
# - sys
#
#
# Example:
#
# import math
#
# print(math.sqrt(25))
#
# Output:
# 5.0
#
# Here, math is a module provided by Python.
#
#
# ------------------------------------------------------------
# Example with the random Module
# ------------------------------------------------------------
#
# import random
#
# number = random.randint(1, 10)
# print(number)
#
# The randint() function generates a random integer
# between the given range.
#
#
# ------------------------------------------------------------
# User-Defined Modules/External Module
# ------------------------------------------------------------
#
# A module created by us is called a USER-DEFINED MODULE.
#
# For example, suppose we create:
#
# mymodule.py
#
# Inside mymodule.py:
#
# name = "Vikas"
#
# def greet():
#     print("Hello Vikas")
#
#
# Now we can use this module in another Python file:
#
# import mymodule
#
# print(mymodule.name)
# mymodule.greet()
#
#
# ------------------------------------------------------------
# Module vs File
# ------------------------------------------------------------
#
# A Python file with a .py extension can be used as a module.
#
# Example:
#
# calculator.py
#
# calculator.py is:
#
# - A Python file
# - A module when it is imported into another Python program
#
#
# ------------------------------------------------------------
# Advantages of Modules
# ------------------------------------------------------------
#
# Modules provide several advantages:
#
# 1. CODE REUSABILITY
#    We can write code once and use it in multiple programs.
#
# 2. CODE ORGANIZATION
#    We can divide a large program into smaller files.
#
# 3. EASY MAINTENANCE
#    It becomes easier to find and modify specific code.
#
# 4. READABILITY
#    Dividing code into modules makes the program easier
#    to understand.
#
# 5. AVOID DUPLICATION
#    We don't have to write the same functionality again
#    and again.
#
#
# ============================================================
# In Simple Words:
# ============================================================
#
# A MODULE is a Python file that contains reusable Python code.
#
# We use the 'import' keyword to use a module in another
# Python program.
#
# Example:
#
# calculator.py
#       ↓
#     import
#       ↓
# main.py
#
# So, we can think of a module as a BOX containing related
# Python code that we can reuse whenever we need it.
# ============================================================

# pip : is the standard package manager for Python, used to install, update, and manage external libraries that are not part of the standard Python installation
# pip install pandas means giving order to pip to install the pandas module.