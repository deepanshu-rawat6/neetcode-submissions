class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i, j = 0, len(arr) - 1

        while j - i >= k:
            if x - arr[i] > arr[j] - x:
                i += 1
            else:
                j -= 1
        
        return arr[i : j + 1]
        