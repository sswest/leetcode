int reverse(int x) {
    int result = 0;
    char flag = x > 0 ? 1 : -1;
    if (x <= -pow(2, 31)) {
        return 0;
    }
    x = x > 0 ? x : -x;
    while (x > 0 || x % 10 > 0) {
        if ((flag == 1 && result > (pow(2, 31) - 1 - x % 10) / 10 )  ||
            (flag == -1 && result > (pow(2, 31)- x % 10) / 10)) {
            return 0;
        }
        result = result * 10 + x % 10;
        x = x / 10;
    }
    return result * flag;
}