class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = {}
        for num in nums:
            if num not in counted:
                counted[num] = 1
            else:
                counted[num] += 1
            pairs = sorted(counted.items(), key = lambda x:x[1], reverse = True)
            answer = []
            for pair in pairs[:k]:
                answer.append(pair[0])
        return answer