"""

1
01
101
0101
10101

"""

def printPattern(rows, cols):
    for i in range(rows):
        for j in range(cols):
            if j <= i:
                # if row is even
                if i % 2 == 0:
                    if j % 2 == 0:
                        print("1", end="")
                    else:
                        print("0", end="")
                else:
                    if j % 2 == 0:
                        print("0", end="")
                    else:
                        print("1", end="")
        print()


if __name__ == "__main__":
    rows = 5
    cols = 5

    printPattern(rows, cols)
