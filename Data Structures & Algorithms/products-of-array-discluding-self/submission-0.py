class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def multiply(arr):
            product = 1
            for n in arr:
                product *= n
            return product

        out = []
        for n in range(len(nums)):
            left = multiply(nums[:n])
            right = multiply(nums[n+1:])
            out.append(left*right)
        return out
