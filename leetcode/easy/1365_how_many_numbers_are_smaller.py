'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
'''

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        seen = {}

        for i, num in enumerate(sorted_nums):
            if num not in seen:
                seen[num] = i
        return [seen[num] for num in nums]