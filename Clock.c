int past(int h, int m, int s) {
    int resultsec=0;
    while(h>0) {
	resultsec+=3600;
	h--;
    }
    while(m>0) {
	resultsec+=60;
	m--;
    }
    while(s>0) {
	resultsec+=1;
	s--;
    }
    int resultms=1000*resultsec;
    return resultms;

}
