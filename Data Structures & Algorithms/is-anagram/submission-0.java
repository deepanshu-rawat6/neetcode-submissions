class Solution {
    public boolean isAnagram(String s, String t) {
        int n = s.length();
        int m = t.length();

        if (n != m) {
            return false;
        }

        Map<Character, Integer> map = new HashMap<>();

        for (char ch : s.toCharArray()) {
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }

        for (char ch : t.toCharArray()) {
            map.put(ch, map.getOrDefault(ch, 0) - 1);
        }

        for (Integer val : map.values()) {
            if (val != 0) {
                return false;
            }
        }

        return true;
    }
}
