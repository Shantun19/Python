"""
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15

"""
def printPattern(rows , cols):
    temp = 1
    for i in range(rows):
        for j in range(cols):
            if(j <= i):
                print(temp, end=" ")
                temp += 1
        print()

if __name__ == "__main__":
    rows = 5
    cols = 5
    printPattern(rows , cols)