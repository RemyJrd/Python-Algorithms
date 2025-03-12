class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = pos = 0

        for i in nums:
            if i > 0:
                pos += 1
            if i < 0:
                neg += 1
        if pos > neg:
            return pos
        else:
            return neg