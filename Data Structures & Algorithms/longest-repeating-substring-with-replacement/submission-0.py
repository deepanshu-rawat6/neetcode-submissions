class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_f, i, res = 0, 0, 0
        freq = [0] * 26

        for j, char_j in enumerate(s):
            indx = ord(char_j) - 65
            freq[indx] += 1
            if max_f  < freq[indx]:
                max_f = freq[indx]

            if j - i + 1 - max_f > k:
                indx_i = ord(s[i]) - 65
                freq[indx_i] -= 1
                i += 1
        
        return len(s) - i