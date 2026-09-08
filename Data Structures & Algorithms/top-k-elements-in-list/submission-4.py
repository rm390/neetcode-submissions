import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = defaultdict(int)

        for n in nums:
            ans[n] +=1

        h = []
        for num in ans.keys():
            heapq.heappush(h, (ans[num], num))
            if len(h) > k:
                heapq.heappop(h)

        res = []
        for i in range(k):
            res.append(heapq.heappop(h)[1])

        return res


           
                   