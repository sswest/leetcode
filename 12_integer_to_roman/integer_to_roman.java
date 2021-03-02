import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.Map;

class Solution {
    public String intToRoman(int num) {
        Map<Integer, String> table = new LinkedHashMap<Integer, String>();
        table.put(1000, "M");
        table.put(900, "CM");
        table.put(500, "D");
        table.put(400, "CD");
        table.put(100, "C");
        table.put(90, "XC");
        table.put(50, "L");
        table.put(40, "XL");
        table.put(10, "X");
        table.put(9, "IX");
        table.put(5, "V");
        table.put(4, "IV");
        table.put(1, "I");
        String result = "";
        while (num > 0) {
            for (Map.Entry<Integer, String> entry: table.entrySet()) {
                Integer key =entry.getKey();
                if (num >= key) {
                    num -= key;
                    result += entry.getValue();
                    break;
                }
            }
        }
        return result;
    }
}