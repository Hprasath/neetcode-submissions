class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        freq_map = collections.defaultdict(list)
        for str in strs:
            char_map = [0] * 26
            for s in str:
                char_map[ord(s) - ord('a')] += 1
            freq_map[tuple(char_map)].append(str)
        return list(freq_map.values())