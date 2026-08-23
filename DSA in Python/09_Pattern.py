"""

1      1
12    21
123  321
12344321

"""

def printPattern(rows , cols):
    for i in range(rows):
        for j in range(cols):
            if(j <= i or j >= 7-i):
                if(j < (cols // 2)):
                    print(j+1,end="")
                else:
                    print((cols-j),end="")
            else:
                print(" ",end="")
        print()

if __name__ == "__main__":
    rows = 4
    cols = 8
    printPattern(rows , cols)