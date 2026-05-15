class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        i, temp, res_i, res_j = 0, float('inf'), 0, 0
        map = Counter(t)
        count = len(map)

        for j, char in enumerate(s):
            if char in map:
                map[char] -= 1
                if map[char] == 0:
                    count -= 1
            
            while i <= j and s[i] not in map:
                i += 1
            
            while count == 0:
                if temp > j - i + 1:
                    temp = j - i + 1
                    res_i = i
                    res_j = j
                
                if s[i] in map:
                    map[s[i]] += 1
                    if map[s[i]] == 1:
                        count += 1
                i += 1
        
        return "" if temp == float('inf') else s[res_i : res_j + 1]