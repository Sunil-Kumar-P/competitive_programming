# 5. Perform the function for the given purpose.
# For writing numbers, there is a system called N-base notation. This system uses only N-based
# symbols. It uses symbols that are listed as the first n symbols. Decimal and n-based notations
# are 0:0, 1:1, 2:2, …, 10:A, 11:B, …, 35:Z.
# Perform the function: Chats DectoNBase(int n, int num)
# This function only uses positive integers. Use a positive integer n and num to find out the n-base
# that is equal to num.
# Steps
# ○ Select a decimal number and divide it by n. Consider this as an integer division.
# ○ Denote the remainder as n-based notation.
# ○ Again divide the quotient by n.
# ○ Repeat the above steps until you get a 0 remainder.
# ○ The remainders from last to first are the n-base values.
# Assumption
# 1 < n < = 36
# Example
# Input:
# N: 12
# Num: 718
# Output:
# 4BA
# Explanation
# num Divisor Quotient Remainder
# 718 12 59 10(A)
# 59 2 4 11(B)
# 4 12 0 4(4)
# Sample input:
# N: 21
# Num: 5678
# Sample output:
# CI8

def DecToNBase(n, num):
    if not (1 < n <= 36):
        return "Invalid input: n must be between 2 and 36 inclusive."
    if num == 0:
        return "0"
    symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n_base = ""
    while num > 0:
        remainder = num % n
        n_base = symbols[remainder] + n_base
        num = num // n

    return n_base

print(DecToNBase(21,5678))
