class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2: return False
        freq_map = Counter(s1)
        i = 0
        count = len(freq_map)

        for j, char_j in enumerate(s2):
            if char_j in freq_map:
                freq_map[char_j] -= 1
                if freq_map[char_j] == 0:
                    count -= 1
            
            if j - i + 1 == len_s1:
                if count == 0:
                    return True
                if s2[i] in freq_map:
                    if freq_map[s2[i]] == 0:
                        count += 1
                    freq_map[s2[i]] += 1
                i += 1
            
        return False