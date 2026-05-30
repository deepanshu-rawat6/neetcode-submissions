class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, root = 0, x, 0 
        while l <= r:
            mid = l + (r - l) // 2
            temp = mid * mid
            if temp == x:
                return int(mid)
            elif temp < x:
                l = mid + 1
                root = mid
            else:
                r = mid - 1
        
        return int(root)
        