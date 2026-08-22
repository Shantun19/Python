# ============================================================
# Escape Sequence Characters in Python
# ============================================================
#
# An escape sequence is a combination of characters that is
# used to represent a special character inside a string.
#
# Escape sequences always start with a BACKSLASH (\).
#
# Example:
#
print("Hello\nWorld")
#
# Output:
#
# Hello
# World
#
# Here, \n is an escape sequence.
#
#
# ------------------------------------------------------------
# Why do we need Escape Sequences?
# ------------------------------------------------------------
#
# Sometimes we need to add special characters inside a string.
#
# For example:
#
# - New line
# - Tab space
# - Quotation marks
# - Backslash
# - Carriage return
# - Backspace
#
# Escape sequences allow us to represent these characters
# inside a string.
#
#
# ============================================================
# Common Escape Sequences in Python
# ============================================================
#
# Escape Sequence       Meaning
# ------------------------------------------------------------
# \n                     New line
# \t                     Tab
# \\                     Backslash
# \'                     Single quotation mark
# \"                     Double quotation mark
# \b                     Backspace
# \r                     Carriage return
# \f                     Form feed
# \v                     Vertical tab
# \a                     Alert / Bell
# ============================================================
#
#
# ------------------------------------------------------------
# 1. \n - New Line
# ------------------------------------------------------------
#
# \n is used to move the text to a new line.
#
# Example:
#
# print("Hello\nWorld")
#
# Output:
#
# Hello
# World
#
#
# Another Example:
#
print()
print("Python\nis\nawesome")
#
# Output:
#
# Python
# is
# awesome
#
#
# ------------------------------------------------------------
# 2. \t - Tab
# ------------------------------------------------------------
#
# \t is used to insert a TAB space.
#
# Example:

print()
print("Hello\tWorld")
#
# Output:
#
# Hello    World
#
#
# Another Example:
#
# print("Name\tAge")
# print("Vikas\t25")
#
#
# ------------------------------------------------------------
# 3. \\ - Backslash
# ------------------------------------------------------------
#
# \\ is used when we want to print an actual backslash.
#
# Example:

print()
print("C:\\Users\\Vikas")
#
# Output:
#
# C:\Users\Vikas
#
#
# Why do we use \\?
#
# Because a single backslash is used to start an escape
# sequence.
#
#
# ------------------------------------------------------------
# 4. \' - Single Quotation Mark
# ------------------------------------------------------------
#
# \' is used to print a single quotation mark inside a
# string that is enclosed using single quotes.
#
# Example:
#
print()
print('It\'s Python')
#
# Output:
#
# It's Python
#
#
# ------------------------------------------------------------
# 5. \" - Double Quotation Mark
# ------------------------------------------------------------
#
# \" is used to print a double quotation mark inside a
# string that is enclosed using double quotes.
#
# Example:
#
print()
print("He said \"Hello\"")
#
# Output:
#
# He said "Hello"
#
#
# ------------------------------------------------------------
# 6. \b - Backspace
# ------------------------------------------------------------
#
# \b moves the cursor one position backward.
#
# Example:
#
print()
print("Helloo\b")
#
# Output:
#
# Hello
#
# Note:
# The exact visual result of \b can depend on the environment
# where the output is displayed.
#
#
# ------------------------------------------------------------
# 7. \r - Carriage Return
# ------------------------------------------------------------
#
# \r moves the cursor back to the beginning of the current
# line.
#
# Example:
#
print()
print("Hello\rWorld")
#
# In many terminals, the output will appear similar to:
#
# World
#
# because "World" overwrites the beginning of "Hello".
#
#
# ------------------------------------------------------------
# 8. \f - Form Feed
# ------------------------------------------------------------
#
# \f represents a form feed character.
#
# It is mainly a historical/formatting character and is not
# commonly used in normal Python programs.
#
# Example:
#
print()
print("Hello\fWorld")
#
#
# ------------------------------------------------------------
# 9. \v - Vertical Tab
# ------------------------------------------------------------
#
# \v represents a vertical tab.
#
# It is rarely used in modern Python programs.
#
# Example:
#
print()
print("Hello\vWorld")
#
#
# ------------------------------------------------------------
# 10. \a - Alert / Bell
# ------------------------------------------------------------
#
# \a represents an alert or bell character.
#
# Depending on the terminal or environment, it may produce
# a sound or visual alert.
#
# Example:
#
print()
print("\a")
#
#
# ============================================================
# Important Example
# ============================================================
#
# Suppose we want to print:
#
# He said "Python is easy."
#
# We can write:
#
print()
print("He said \"Python is easy.\"")
#
# Output:
#
# He said "Python is easy."
#
#
# ============================================================
# Escape Sequences with Different Quotes
# ============================================================
#
# Python allows us to use both single and double quotes
# for strings.
#
# Example:
#
# print("Hello")
# print('Hello')
#
# Both are valid.
#
# Because of this, sometimes we don't even need an escape
# sequence.
#
# Example:
#
# print("It's Python")
#
# Output:
#
# It's Python
#
# Here, we don't need to write:
#
# print('It\'s Python')
#
# because the string is enclosed in double quotes.
#
#
# Similarly:
#
# print('He said "Hello"')
#
# We don't need to escape the double quotes because the
# string is enclosed in single quotes.
#
#
# ============================================================
# Raw Strings
# ============================================================
#
# Sometimes we don't want Python to treat backslashes as
# escape sequences.
#
# In that case, we can use a RAW STRING by placing r before
# the string.
#
# Example:
#
# print(r"C:\Users\Vikas\Documents")
#
# Output:
#
# C:\Users\Vikas\Documents
#
# Here, Python treats the backslashes as normal characters.
#
#
# ============================================================
# Important Point to Remember
# ============================================================
#
# Escape Sequence:
#
#     Backslash (\) + Character
#
# Example:
#
#     \n
#     \t
#     \\
#     \'
#     \"
#
# The backslash tells Python that the following character
# has a special meaning.
#
#
# ============================================================
# In Simple Words
# ============================================================
#
# Escape sequences are special character combinations used
# inside strings to perform special formatting or represent
# characters that are difficult to type directly.
#
# The most commonly used escape sequences are:
#
# \n  -> New line
# \t  -> Tab
# \\  -> Backslash
# \'  -> Single quote
# \"  -> Double quote
#
# Example:
#
# print("Hello\nPython\tProgramming")
#
# Output:
#
# Hello
# Python    Programming
# ============================================================