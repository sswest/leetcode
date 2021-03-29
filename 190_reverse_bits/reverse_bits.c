uint32_t reverseBits(uint32_t n) {
    int ans = 0, p = 0;
    uint32_t o = 1;
    while (p < 32) {
        int t = (n >> p) & 1;
        if (t == 1) {
            ans |= (o << (31 - p));
        }
        p++;
    }
    return ans;
}