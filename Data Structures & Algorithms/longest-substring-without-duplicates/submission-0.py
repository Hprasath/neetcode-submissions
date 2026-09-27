class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        # for i in range(len(s)):
        #     seen = set()
        #     for j in range(i,len(s)):
        #         if s[j] in seen:
        #             break
        #         seen.add(s[j])
        #         max_len = max(max_len, j-i+1)
        # return max_len

        left = 0
        char_map = {} # stores char and index
        for right, char in enumerate(s):
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            char_map[char] = right
            max_len = max(max_len, right-left+1)
        return max_len




        