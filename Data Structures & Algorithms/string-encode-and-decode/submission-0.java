class Solution {

    public static String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();

        for (String str : strs) {
            sb.append(str.length()).append('#').append(str);
        }

        return sb.toString();
    }

    public static List<String> decode(String str) {
        List<String> strs = new ArrayList<>();

        int i = 0;
        while (i < str.length()) {
            int j = i;
            while (str.charAt(j) != '#') j++;

            int length = Integer.parseInt(str.substring(i, j));

            i = j + 1 + length;

            strs.add(str.substring(j + 1, i));
        }

        return strs;
    }
}
