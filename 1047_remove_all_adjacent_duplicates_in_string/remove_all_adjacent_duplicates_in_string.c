char * removeDuplicates(char * S){
    int size = strlen(S);
    char *ans = malloc(sizeof(char) * (size + 1));
    int position = 0;
    for (int i = 0; i < size; i++) {
        if (position > 0 && ans[position-1] == S[i])
            position--;
        else
            ans[position++] = S[i];
    }
    ans[position] = '\0';
    return ans;
}