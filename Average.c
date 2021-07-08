/**https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/c*/
double find_average(double* array, int lenght) {
    if (lenght == 0) {
	return 0;
    }
    double sum = 0;
    for (int i = 0; i < lenght; i++) {
	sum += array[i];
    }
    double average = sum / lenght;
    return average;
}
