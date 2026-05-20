class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        len_nums = len(nums)

        def helper(indx, currXOR):
            if indx == len_nums:
                return currXOR
            
            withOutEle = helper(indx + 1, currXOR)

            withEle = helper(indx + 1, currXOR ^ nums[indx])

            return withEle + withOutEle
        
        return helper(0, 0)
        