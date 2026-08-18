# Print square pattern

"""
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
"""

def printSquarePattern(rows, cols):
    for i in range(rows):
        for j in range(cols):
            print("*", end=" ")
        print()  # Move to the next line after each row


if __name__ == "__main__":
    rows = 5
    cols = 5

    printSquarePattern(rows, cols)
