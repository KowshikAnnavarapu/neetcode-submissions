class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        seen  = set()
        max_len = 0
        while j < len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)
            j += 1
        return max_len
        