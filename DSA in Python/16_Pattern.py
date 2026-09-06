"""

* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 

"""
def printPattern(rows , cols):
    for i in range(rows):
        for j in range(cols):
            if i < (cols // 2):
                if j <= (4-i) or j >= (5+i):
                    print("*" , end=" ")
                else:
                    print(" ", end=" ")
            else:
                if j <= (i-5) or j >= (9 - (i-5)):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        print()

if __name__ == "__main__":
    rows = 10
    cols = 10
    printPattern(rows , cols)