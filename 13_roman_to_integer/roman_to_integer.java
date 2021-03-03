import java.util.HashMap;
import java.util.Map;

class Solution {
    public int romanToInt(String s) {
        int result = 0;
        Map<String, Integer> table = new HashMap<String, Integer>();
        table.put("M", 1000);
        table.put("CM", 900);
        table.put("D", 500);
        table.put("CD", 400);
        table.put("C", 100);
        table.put("XC", 90);
        table.put("L", 50);
        table.put("XL", 40);
        table.put("X", 10);
        table.put("IX", 9);
        table.put("V", 5);
        table.put("IV", 4);
        table.put("I", 1);
        int i = 0;
        while (i < s.length()) {
            if (i+2 <= s.length() && table.containsKey(s.substring(i, i+2))) {
                result += table.get(s.substring(i, i+2));
                i += 2;
            } else if (table.containsKey(s.substring(i, i+1))) {
                result += table.get(s.substring(i, i+1));
                i += 1;
            }
        }
        return result;
    }
}