class Solution {
    public int clumsy(int N) {
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(N--);
        int position = 0;
        while (N > 0) {
            switch (position % 4) {
                case 0:
                    stack.push(stack.pop() * N);
                    break;
                case 1:
                    stack.push(stack.pop() / N);
                    break;
                case 2:
                    stack.push(N);
                    break;
                case 3:
                    stack.push(-N);
                    break;
            }
            N--;
            position++;
        }
        int ans = 0;
        while (!stack.isEmpty()) {
            ans += stack.pop();
        }
        return ans;
    }
}