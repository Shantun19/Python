"""

*********
 ******* 
  *****  
   ***   
    *

"""

def printPattern(rows , cols):
    for i in range(rows):
        for j in range(cols):
            if j >= i and j <= (cols-1-i):
                print("*",end="")
            else:
                print(" ",end="")
        print()

if __name__ == "__main__":
    rows = 5
    cols = 9

    printPattern(rows,cols)