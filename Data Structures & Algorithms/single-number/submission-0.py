class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        # XOR of whole array
        # a XOR a = 0
        # a XOR 0 = a
        for j in range(len(nums)):
            ans ^= nums[j]
        
        return ans
        