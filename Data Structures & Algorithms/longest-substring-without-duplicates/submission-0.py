class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1. Expanded to 128 to handle spaces, numbers, and symbols
        freq = [0] * 128 
        i, counter, res = 0, 0, 0
        
        for j, char_j in enumerate(s):
            # should be between 97 to 122
            indx_j = ord(char_j) 
            if freq[indx_j] == 0:
                counter += 1
            freq[indx_j] += 1

            # So why are we doing this?
            # basically counter represents unique elements in scope of the window, so if some duplicates is there that means counter would be always less than the window size
            # start removing the elements from the start of the window and check for the unqiue elements as well
            while counter < j - i + 1:
                indx_i = ord(s[i]) 
                freq[indx_i] -= 1

                if freq[indx_i] == 0:
                    counter -= 1
                i += 1


            # So, there are all unique elements in the window
            # Essence of question is : finding the all unique i.e. freq[<all elements>] in the window should be 1.
            if counter == j - i + 1:
                if res < j - i + 1:
                    res = j - i + 1
        
        return res