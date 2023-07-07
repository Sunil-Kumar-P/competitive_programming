# 1480. Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

def runningSum(nums):
    output = []
    for i in range(0, len(nums)):
        if(i==0):
            output.append(nums[i])
        else:
            temp = 0
            for j in range(0,i+1):
                temp = nums[j] + temp
            output.append(temp)
        
    return output

print(runningSum([1,2,3,4]))