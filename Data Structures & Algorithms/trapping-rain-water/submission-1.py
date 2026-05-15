class Solution:
    def trap(self, height: List[int]) -> int:
        lmax , rmax = 0, 0
        i, j = 0, len(height) - 1
        area = 0

        while i < j:
            if height[i] < height[j]:
                if lmax < height[i]:
                    lmax = height[i]
                area += lmax - height[i]
                i += 1
            else:
                if rmax < height[j]:
                    rmax = height[j]
                area += rmax - height[j]
                j -= 1
        
        return area