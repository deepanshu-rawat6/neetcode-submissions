class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans, i, req_sum = float("inf"), 0, 0

        for j, num_j in enumerate(nums):
            req_sum += num_j

            while req_sum >= target:
                temp = j - i + 1
                if ans > temp:
                    ans = temp
                req_sum -= nums[i]
                i += 1

        return 0 if ans == float("inf") else ans