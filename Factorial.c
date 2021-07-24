int factorial(int n) {
    if (n>12 || n<0) {
        return -1;
    }
    if(n==0) {
        return 1;
    }
    int factor=1;
    for(int i=1; i<=n; i++) {
        factor *= i;
    }
    return factor;
}
