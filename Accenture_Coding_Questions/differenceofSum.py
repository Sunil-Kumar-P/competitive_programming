# 1. Execute the given function.
# def differenceofSum(n.m)
# The function takes two integrals m and n as arguments. You are required to obtain the total of all
# integers ranging between 1 to n (both inclusive) which are not divisible by m. You must also
# return the distinction between the sum of integers not divisible by m with the sum of integers
# divisible by m.
# Assumption
# ○ m > 0 and n > 0
# ○ Sum lies within the integral range
# Example
# Input:
# m = 6
# n = 30
# Output:
# 285
# ○ Integers divisible by 6 are 6, 12, 18, 24, and 30. Their sum is 90.
# ○ Integers that are not divisible by 6 are 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19,
# 20, 21, 22, 23, 25, 26, 27, 28, and 29. Their sum is 375.
# ○ The difference between them is 285 (375 – 90).
# Sample input:
# m = 3
# n = 10
# Sample output:
# 19

def differenceofSum(n,m):
    diff, SumN, SumM = 0,0,0
    for i in range(n+1):
        if(i%m==0):
            SumM+=i
        else:
            SumN+=i
    diff=SumN-SumM
    return diff
        
print(differenceofSum(30,6))
print(differenceofSum(10,3))