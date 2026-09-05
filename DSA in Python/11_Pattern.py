"""
A 
B C 
D E F 
G H I J 
K L M N O 

"""

def printPattern(rows, cols):
    # ord('A') gives u the numeric value of character.
    char = ord('A')
    for i in range(rows):
        for j in range(cols):
            if j <= i:
                # chr(char) converts the character numeric value to actual character.
                print(chr(char), end=" ")
                char += 1
        print()
if __name__ == "__main__":
    rows = 5
    cols = 5
    printPattern(rows, cols)