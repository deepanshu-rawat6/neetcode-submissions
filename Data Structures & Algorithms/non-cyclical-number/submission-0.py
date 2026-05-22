class Solution:
    def isHappy(self, n: int) -> bool:
        def findAndSumSquare(num):
            ans = 0
            while num > 0:
                rem = num % 10
                ans += rem ** 2
                num //= 10
            return ans
        
        slow, fast = n, n

        while True:
            slow = findAndSumSquare(slow)
            fast = findAndSumSquare(findAndSumSquare(fast))
            
            if slow == fast:
                break
        
        return slow == 1



        