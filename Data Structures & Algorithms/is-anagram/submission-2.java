class Solution {
    public boolean isAnagram(String s, String t) {
        int n = s.length();
        int m = t.length();

        if (n != m) {
            return false;
        } else {
            int[] freqArr = new int[26];
            Arrays.fill(freqArr, 0);

            for (int i = 0; i < n; i++) {
                char ch = Character.toLowerCase(s.charAt(i));
                char chr = Character.toLowerCase(t.charAt(i));
                freqArr[ch - 'a']++;
                freqArr[chr - 'a']--;
            }

            for (int val : freqArr) {
                if (val != 0){
                    return false;
                }
            }

            return true;
        }
    }
}
