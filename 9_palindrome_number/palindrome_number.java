import java.util.Stack;

class Solution {
    // 借助栈判断回文字符串
    public boolean isPalindrome(int x) {
        if (x < 0) return false;
        String a = String.valueOf(x);
        Stack<String> stack = new Stack<String>();
        for (int i = 0; i < a.length() ; i++) {
            stack.push(a.substring(i, i + 1));
        }
        for (int i = 0; i < a.length() ; i++) {
            String tmp = stack.pop();
            if (!tmp.equals(a.substring(i, i + 1))) return false;
        }
        return true;
    }
}