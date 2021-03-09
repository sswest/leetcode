class Solution {
    public String removeDuplicates(String S) {
        StringBuffer stack = new StringBuffer();
        int top = -1;
        for (int i = 0; i < S.length(); ++i) {
            char ch = S.charAt(i);
            if (top >= 0 && stack.charAt(top) == ch) {
                stack.deleteCharAt(top);
                --top;
            } else {
                stack.append(ch);
                ++top;
            }
        }
        return stack.toString();
    }
}

char* removeDuplicates(char* S) {
    int n = strlen(S);
    char* stk = malloc(sizeof(char) * (n + 1));
    int retSize = 0;
    for (int i = 0; i < n; i++) {
        if (retSize > 0 && stk[retSize - 1] == S[i]) {
            retSize--;
        } else {
            stk[retSize++] = S[i];
        }
    }
    stk[retSize] = '\0';
    return stk;
}

