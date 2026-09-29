class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq_map = collections.defaultdict()
        for num in nums:
            freq_map[num] = freq_map.get(num,0)+1
        res = sorted(freq_map.keys(), key=lambda num:freq_map[num], reverse=True)
        return res[:k]
