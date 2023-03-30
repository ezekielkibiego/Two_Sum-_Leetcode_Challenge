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
    print(twoSum([2,7,11,15], 26))