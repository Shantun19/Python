"""
*    
**   
***  
**** 
*****
**** 
***  
**   
*

"""

def printPattern(rows , cols):
    for i in range(rows):
        if (i <= (rows // 2)):
            for j in range(cols):
                if (j <= i):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
        else:
            for j in range(cols):
                if(j <= 8 - i):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()


if __name__ == "__main__":
    rows = 9
    cols = 5

    printPattern(rows,cols)