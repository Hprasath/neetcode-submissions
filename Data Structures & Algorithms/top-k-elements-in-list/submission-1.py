class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq_map = collections.defaultdict()
        for num in nums:
            freq_map[num] = freq_map.get(num,0)+1
        # res = sorted(freq_map.keys(), key=lambda num:freq_map[num], reverse=True)
        # return res[:k]

        buckets = [[] for i in range(len(nums)+1)]

        for item in freq_map.items():
            buckets[item[1]].append(item[0])
        
        for freq in range(len(buckets)-1,0,-1):
            for num in buckets[freq]:
                res.append(num)
            if len(res) >= k:
                return res
