"""
Closest to n and Divisible by m
Given two integers n and m (m != 0). Find the number closest to n and divisible by m. If there is more than one such number, then output the one having maximum absolute value.

Examples: 

    Input: n = 13, m = 4
    Output: 12
    Explanation: 12 is the closest to 13, divisible by 4.

    Input: n = -15, m = 6
    Output: -18
    Explanation: Both -12 and -18 are closest to -15, but -18 has the maximum absolute value.

"""

def closestNumber(n, m) :
    quotient = int(n / m)
    print(f"the quotient is : {quotient}")
    
    # 1st possible closest number
    leftClosestNumber = m * quotient
    
    # 2nd possible closest number
    if((leftClosestNumber * m) > 0) :
        rightClosestNumber = (m * (quotient + 1)) 
    else :
        rightClosestNumber = (m * (quotient - 1))
    
    # if true, then n1 is the required closest number
    if (abs(n - leftClosestNumber) < abs(n - rightClosestNumber)) :
        return leftClosestNumber
    
    # else n2 is the required closest number 
    return rightClosestNumber
    
    
if __name__ == "__main__":
  n = -15
  m = 6
  print(closestNumber(n, m))