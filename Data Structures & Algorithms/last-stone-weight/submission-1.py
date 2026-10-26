class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            largest_1 = heapq.heappop_max(stones)
            largest_2 = heapq.heappop_max(stones)
            difference = largest_1 - largest_2
            if difference != 0:
                heapq.heappush_max(stones, difference)
        if len(stones) == 1:
            return heapq.heappop_max(stones)
        else:
            return 0