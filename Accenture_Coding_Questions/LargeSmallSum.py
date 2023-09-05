# 2. Execute the given function.
# def LargeSmallSum(arr)
# The function takes an integral arr which is of the size or length of its arguments. Return the sum
# of the second smallest element at odd position ‘arr’ and the second largest element at the even
# position.
# Assumption
# ○ Every array element is unique.
# ○ Array is 0 indexed.
# Note:
# ○ If the array is empty, return 0.
# ○ If array length is 3 or <3, return 0.
# Example
# Input:
# Arr: 3 2 1 7 5 4
# Output:
# 7
# Explanation
# ○ The second largest element at the even position is 3.
# ○ The second smallest element at the odd position is 4.
# ○ The output is 7 (3 + 4).

# Note: 
# index: 0 1 2 3 4 5
# value: 3 2 1 7 5 4
#        |         |
#       small     large
    
def LargeSmallSum(arr):
    n = len(arr)
    if(n<=3):
        return 0
    second_smallest_odd = float('inf')
    second_largest_even = float('-inf')
    minval = min(arr)
    maxval = max(arr)
    for i in range(n):
        if i % 2 == 1:  # Odd position
            if arr[i] < second_smallest_odd and arr[i] != minval:
                second_smallest_odd = arr[i]
        else:  # Even position
            if arr[i] > second_largest_even and arr[i] != maxval:
                second_largest_even = arr[i]

    return second_smallest_odd + second_largest_even

print(LargeSmallSum([3, 2, 1, 7, 5, 4]))