class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums_sort = sorted(nums)
        i = 0
        for i in range(len(nums_sort) - 2):
            if i > 0 and nums_sort[i] == nums_sort[i-1]:
                continue
            j = i + 1
            k = len(nums_sort) - 1
            while j < k:
                add = nums_sort[i] + nums_sort[j] + nums_sort[k]
                if add > 0:
                    k -= 1
                elif add < 0:
                    j += 1
                else:
                    result.append([nums_sort[i], nums_sort[j], nums_sort[k]])
                    j += 1
                    k -= 1
                    while j<k and nums_sort[j] == nums_sort[j-1]:
                        j += 1
                    while j<k and nums_sort[k] == nums_sort[k + 1]:
                        k -= 1
        return result


