class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        if nums is None or not nums:
            return res
        
        def helper(subset, indx):
            if indx >= len(nums):
                # Append a copy of the subset, not the reference
                res.append(subset[:]) 
                return
            
            subset.append(nums[indx])
            helper(subset, indx + 1)

            subset.pop() 
            helper(subset, indx + 1)

        helper([], 0)
        return res