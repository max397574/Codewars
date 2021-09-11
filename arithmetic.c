/* https://www.codewars.com/kata/583f158ea20cfcbeb400000a/train/c */
double arithmetic(double a, double b, const char* operator) {
    if (operator == "add"){
        return (a+b);
    }
    else if (operator == "subtract"){
        return (a-b);
    }
    else if (operator == "multiply"){
        return (a*b);
    }
    else if (operator == "divide"){
        return (a/b);
    }
}
