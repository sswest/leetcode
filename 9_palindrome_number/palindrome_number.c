bool isPalindrome(int x){
    if (x < 0) return false;
    int MAX_INTER = 214748364;
    int remainder = 0;
    int tmp = x;
    while (x != 0) {
        if ((remainder > MAX_INTER) || (remainder == MAX_INTER && x % 10 > 7)) return false;
        remainder = remainder * 10 + x % 10;
        x /= 10;
    }
    return remainder == tmp;
}
