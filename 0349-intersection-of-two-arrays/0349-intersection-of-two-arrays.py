class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        nums3 = []

        for i in nums1:
            if i not in seen:
                seen[i] = True
        

        for i in nums2:
            if i in seen:
                nums3.append(i)
                del seen[i]
        
        return nums3

        