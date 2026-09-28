class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        char_map = {}
        left = 0
        for idx,chr in enumerate(s):
            if chr in char_map and char_map[chr] >= left:
                left = char_map[chr] + 1
            char_map[chr] = idx
            max_len = max(max_len, idx-left+1)
        return max_len
        