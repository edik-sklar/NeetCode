import heapq
from collections import Counter, defaultdict


class Solution:

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        sol = defaultdict(int)
        for n in nums:
            sol[n] = sol.get(n, 0) + 1
        # nlargest(k, iterable, key) — sort sol's keys by their frequency value
        return heapq.nlargest(k, sol.keys(), key=lambda x: sol[x])

    # def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    #     sol = defaultdict(int)
    #     for n in nums:
    #         sol[n] = sol.get(n,0) + 1
    #     to_heap = {v:k for k, v in sol.items()}
    #     print(f"sol is {sol}")
    #     print(f"to heap is {to_heap}")
    #     h = heapq.nlargest(k,to_heap.keys())
    #     print(f"h is {h}")
    #     return [to_heap[i] for i in h]




s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], k = 2))
# Output: [1,2]
print(s.topKFrequent( [1, 2, 1, 2, 1, 2, 3, 1, 3, 2], k = 2))
# Output: [1,2]

