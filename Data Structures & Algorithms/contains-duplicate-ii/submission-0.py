class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i, j = 0, 0
        num_set = set()

        for j in range(len(nums)):
            if j - i > k:
                num_set.remove(nums[i])
                i += 1

            if nums[j] in num_set: return True

            num_set.add(nums[j])
        
        return False