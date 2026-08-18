"""
* 
* * 
* * * 
* * * * 
* * * * * 
"""

def printPattern02(rows , cols):
    for i in range(rows):
        for j in range(cols):
            if(j <= i):
                print("*", end=" ")
        print()

if __name__ == "__main__":
    rows = 5
    cols = 5

    printPattern02(rows , cols)

