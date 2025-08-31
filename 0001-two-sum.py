class Solution:
    def twoSum(self, nums, target):
        num_map = {}  # Dictionary to store the difference and index
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_map:
                return [num_map[diff], i]
            num_map[num] = i
