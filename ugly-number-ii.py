import heapq

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        seen = set()
        seen.add(1)
        heap = []
        heapq.heappush(heap, 1)
        count = 1
        while count < n:
            cur = heapq.heappop(heap)
            for num in (2,3,5):
                if cur * num not in seen:
                    seen.add(cur*num)
                    heapq.heappush(heap, cur*num)
            count += 1
        return heapq.heappop(heap)
