"""

4444444
4333334
4322234
4321234
4322234
4333334
4444444

"""
def printPattern(rows , cols):
    ele = 4
    for i in range(rows):
        for j in range(cols):
            val = min(min(i,j) , min(rows-1-i,cols-1-j))
            print(ele - val,end="")
        print()

if __name__ == "__main__":
    rows = 7
    cols = 7
    printPattern(rows , cols)