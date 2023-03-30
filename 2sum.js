function twoSum(nums, target) {
    let hashTable = {};
    for (let i = 0; i < nums.length; i++) {
        let complement = target - nums[i];
        if (hashTable.hasOwnProperty(complement)) {
            return [hashTable[complement], i];
        }
        hashTable[nums[i]] = i;
    }
    return [];
}

// Example usage
let nums = [2, 7, 11, 15];
let target = 9;
console.log(twoSum(nums, target)); // Output: [0, 1]