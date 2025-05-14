class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = set(nums)
        longest = 0

        for i in sequence:
            if i - 1 not in sequence:
                streak = 1
                current = i

                while current + 1 in sequence:
                    current += 1
                    streak += 1
                longest = max(longest, streak)
        
        return longest