"""

    *    
   ***   
  *****  
 ******* 
*********

"""

def printPattern(rows,cols):
    for i in range(rows):
        for j in range(cols):
            if(j >= (rows-1-i) and j <= (rows-1+i)):
                print("*" , end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":
    rows = 5
    cols = 9

    printPattern(rows,cols)