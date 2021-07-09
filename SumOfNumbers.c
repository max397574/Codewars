/**https://www.codewars.com/kata/55f2b110f61eb01779000053/train/c*/
int get_sum(int a, int b) {
    int sum = 0;
    if (a==b) {
	return a;
    }
    else {
	if (a<b) {
	    for (int i=a; i<=b; i++) {
		sum += i;
	    }
	}
	else if (a>b) {
	    for (int i=b; i<=a; i++) {
		sum += i;
	    }
	}
	return sum;
    }
}
