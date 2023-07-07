# 350. Intersection of Two Arrays II

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
from collections import Counter

def intersect(nums1, nums2):
    counter1 = Counter(nums1)
    counter2 = Counter(nums2)

    common = counter1 & counter2

    result = []
    for num, freq in common.items():
        result.extend([num] * freq)

    return result

print(intersect([1,2,2,1], [2,2]))