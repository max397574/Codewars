/* https://www.codewars.com/kata/59377c53e66267c8f6000027/train/c */
#include <stdio.h>
#include <string.h>
char *alphabet_war(const char *fight){
    int right_points = 0;
    int left_points = 0;
    for (int i = 0; i < strlen(fight); i++) {
        if (fight[i] == 'w') {
            left_points += 4;
        }
        else if (fight[i] == 'p') {
            left_points += 3;
        }
        else if (fight[i] == 'b') {
            left_points += 2;
        }
        else if (fight[i] == 's') {
            left_points += 1;
        }
        else if (fight[i] == 'm') {
            right_points += 4;
        }
        else if (fight[i] == 'q') {
            right_points += 3;
        }
        else if (fight[i] == 'd') {
            right_points += 2;
        }
        else if (fight[i] == 'z') {
            right_points += 1;
        }
    }
    if (right_points > left_points) {
        return "Right side wins!";
    }
    else if ( left_points > right_points) {
        return "Left side wins!";
    }
    return "Let's fight again!";
}
