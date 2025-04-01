class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        heap = []

        for i in nums:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
        
        for j in result:
            count = result[j]
            heap.append((-count, j))
        
        heapq.heapify(heap)

        output = []
        for elements in range(k):
            popped = heapq.heappop(heap)
            val = popped[1]
            output.append(val)
        
        return output