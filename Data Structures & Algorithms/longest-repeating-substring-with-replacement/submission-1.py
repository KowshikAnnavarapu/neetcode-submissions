class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        count = {}
        max_freq = 0
        answer = 0
        for j in range(len(s)):
            count[s[j]] = count.get(s[j], 0) + 1

            while (j - i + 1) - max(count.values()) > k:
                count[s[i]] -= 1
                i += 1
            answer = max(answer, j - i + 1)
        return answer        