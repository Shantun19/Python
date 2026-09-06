"""

*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * * *   * * * * 
* * * *       * * * 
* * *           * * 
* *               * 

"""

def printPattern(rows , cols):
    for i in range(rows):
        for j in range(cols):
            if i <= (rows // 2):
                if j <= i or j >= 9-i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            else:
                if j <= 4-(i-5) or j >= (6+(i-5)):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        print()

if __name__ == "__main__":
    rows = 9
    cols = 10
    printPattern(rows , cols)