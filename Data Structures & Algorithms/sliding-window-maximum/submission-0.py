class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        len_nums = len(nums)
        res = [0] * (len_nums - k + 1)
        d = deque()
        i, j = 0, 0
        for j, num_j in enumerate(nums):
            while d and d[-1] < num_j:
                d.pop()
            d.append(num_j)

            if j - i + 1 == k:
                res[i] = d[0]
                if nums[i] == d[0]:
                    d.popleft()
                i += 1
        
        return res