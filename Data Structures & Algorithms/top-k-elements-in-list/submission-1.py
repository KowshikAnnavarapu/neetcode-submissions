class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if not num in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        pairs = sorted(counts.items(), key = lambda x:x[1], reverse = True)
        answer = []
        for pair in pairs[:k]:
            answer.append(pair[0])
        return answer  
        