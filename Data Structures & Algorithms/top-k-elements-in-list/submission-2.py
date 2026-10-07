class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)

        for n in nums:
            hm[n] += 1
        
        res = list(sorted(hm.items(), key=lambda item: item[1], reverse=True))

        return [i[0] for i in res[:k]]
        