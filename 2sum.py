from typing import List


class Solution:
    
    def twoSum(nums, target): # def twoSum(self, nums: List[int], target: int) -> List[int]: for leetcode
        nums_with_indices = [(num, i) for i, num in enumerate(nums)]
        nums_with_indices.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            sum = nums_with_indices[left][0] + nums_with_indices[right][0]
            if sum == target:
                return [nums_with_indices[left][1], nums_with_indices[right][1]]
            elif sum < target:
                left += 1
            else:
                right -= 1
    # Example usage
    print(twoSum([2,7,11,15], 18))
    

# The twoSum function takes two arguments: nums, 
# which is a list of integers, and target, which is also an integer. 
# The function returns a list of two integers,
# which are the indices of the two numbers in the nums list that add up to the target value.

# This solution uses a technique called the "two-pointer approach" to find the solution. 
# We first create a new list called nums_with_indices that contains tuples of the form (num, index) for each number num and its index in the original nums list. 
# We then sort this list by the values of the numbers.

# Next, we create two pointers left and right. 
# The left pointer starts at the beginning of the sorted list, and the right pointer starts at the end of the sorted list. 
# We then check if the sum of the numbers at the left and right pointers is equal to the target value. 
# If it is, we have found the solution, and we return the indices of these numbers.

# If the sum is less than the target value, we know that we need a larger sum, so we move the left pointer to the right, 
# which increases the sum. If the sum is greater than the target value, we know that we need a smaller sum, 
# so we move the right pointer to the left, which decreases the sum.

# We repeat this process until we find the solution or the left pointer is greater than or equal to the right pointer.
# By moving the pointers in this way, we are able to narrow down the search space and find the solution in linear time (i.e., O(n)), 
# where n is the length of the nums list.

