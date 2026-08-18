def printTableUsingIterativeApproach(num):
    for i in range(1,11):
        print("%d * %d = %d" % (num , i , num*i))

def printTableUsingRecursion(num , index):
    if(index == 11):
        return
    print("%d * %d = %d" % (num , index , num*index))
    index += 1
    printTableUsingRecursion(num , index)



if __name__ == "__main__":
    num = (int(input("Enter any value !")))
    printTableUsingIterativeApproach(num)

    # print table using recursion
    printTableUsingRecursion(num , 1)