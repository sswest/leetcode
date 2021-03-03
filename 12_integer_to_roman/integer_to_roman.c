char * intToRoman(int num){
    // 使用两个数组模拟哈希表
    int keys[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    char values[13][3] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    char *p = (char *)calloc(16, sizeof(char));  // 由于num < 3999 因此16个字符长度已经足够
    for (int i = 0; i < 13; i++) {
        while (num >= keys[i]) {
            strcat(p, values[i]);
            num -= keys[i];
        }
    }
    return p;
}