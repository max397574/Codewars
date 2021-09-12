/* https://www.codewars.com/kata/57cc981a58da9e302a000214/train/c */
#include <stdbool.h>
#include <stddef.h>

bool small_enough(int *arr, size_t length, int limit){
    for (int i=0; i<length; i++) {
        if (arr[i]>limit) {
            return false;
        }
    }
    return true;
}
