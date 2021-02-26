
import java.util.ArrayList;

class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1) return s;
        String result = "";
        ArrayList<String> arr = new ArrayList<String>();
        for (int i = 0; i < numRows; i++) {
            arr.add("");
        }
        int r = 0, flag = -1;
        for (char c : s.toCharArray()) {
            arr.set(r, arr.get(r) + c);
            if (r == 0 || r == numRows - 1)
                flag = -flag;
            r += flag;
        }
        for (int i = 0; i < arr.size(); i++) {
            result += arr.get(i);
        }
        return result;
    }
}