// 217. Contains Duplicate
// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

// Input: nums = [1,2,3,1]
// Output: true

var containsDuplicate = (nums, numsSet = new Set()) => {
    for (const num of nums) {
        if (numsSet.has(num)) return true;
        numsSet.add(num);       
    }

    return false;
};
console.log(containsDuplicate([1,2,3,1]))