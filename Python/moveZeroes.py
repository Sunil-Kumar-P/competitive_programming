# 283. Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
def moveZeroes(nums):
    # time is 56ms
    # for i in range(len(nums)):
    #     if(nums[i]==0):
    #         nums.append(0)
    #         nums.remove(nums[i])

    # time is 49ms
    # a = nums.count(0)
    # for i in  range(a):
    #     nums.remove(0)
    #     nums.append(0)
        
    # Two-pointer
    i, j = 0, 0
    while j < len(nums):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
    return nums

print(moveZeroes([0,1,0,3,12]))