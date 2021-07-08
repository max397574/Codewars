/**https://www.codewars.com/kata/5601409514fc93442500010b/train/c*/
#include <stdbool.h>
int better_than_average(int class_points[], int class_size, int your_points) {
    int sum = 0;
    for (int i = 0; i < class_size; i++) {
	sum += class_points[i];
    }
    int average = sum / class_size;
    if (your_points < average) {
	return false;
    }
    else {
	return true;
    }
}
