class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        leftMax = height[i]
        rightMax = height[j]
        water = 0
        while i < j:
            if leftMax < rightMax:
                water += leftMax - height[i]
                i += 1
                leftMax = max(leftMax, height[i])
            else:
                water += rightMax - height[j]
                j -= 1
                rightMax = max(rightMax, height[j])
        return water
        