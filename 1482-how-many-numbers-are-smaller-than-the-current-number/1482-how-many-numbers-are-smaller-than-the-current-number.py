class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        seen = {}

        for i, num in enumerate(sorted_nums):
            if num not in seen:
                seen[num] = i
        return [seen[num] for num in nums]