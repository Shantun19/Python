"""

    *    
   ***   
  *****  
 ******* 
*********
*********
 ******* 
  *****  
   ***   
    *    

"""


def printPattern(rows,cols):
    for i in range(rows):
        if i < (rows // 2):
            for j in range(cols):
                if j >= 4-i and j <= 4+i:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
        else:
            temp = i - 5
            for j in range(cols):
                if(j >= temp and j <= 8-temp):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()





if __name__ == "__main__":
    rows = 10
    cols = 9

    printPattern(rows,cols)