#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <math.h>

int main() {
   
    double hakjum=0.0;
    int i;
    int j;
    double temp = 0.0;
    double result = 0.0;
    double count = 0.0;
    double temp2 = 0.0;
    for (i = 0; i < 20; i++)
    {
        char grade[1001];
        char name[1001];
        scanf("%s %lf %s", &name, &hakjum, &grade);
        if (strcmp(grade,"A+") == 0)
        {
            temp = 4.5;
        }
        else if (strcmp(grade,"A0")==0)
        {
            temp = 4.0;
        }
        else if (strcmp(grade, "B+") == 0)
        {
            temp = 3.5;
        }
        else if (strcmp(grade, "B0") == 0)
        {
            temp = 3.0;
        }
        else if (strcmp(grade, "C+") == 0)
        {
            temp = 2.5;
        }
        else if (strcmp(grade, "C0") == 0)
        {
            temp = 2.0;
        }
        else if (strcmp(grade, "D+") == 0)
        {
            temp = 1.5;
        }
        else if (strcmp(grade, "D0") == 0)
        {
            temp = 1.0;
        }
        else if (strcmp(grade, "F") == 0)
        {
            temp = 0.0;
        }
        else if (strcmp(grade, "P") == 0)
        {
            temp = 0.0;
            count = count + 1;
        }
        result = result + (temp * hakjum);
        if (strcmp(grade, "P") != 0)
        {
            temp2 = temp2 + hakjum;
        }
    }
    result = result / temp2;

    printf("%.6lf", result);

    return 0;
}
