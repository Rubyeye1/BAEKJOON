#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <math.h>

int main() {
   
    int a, b;

    while (1)
    {
        scanf("%d %d", &a, &b);

        if (a == 0 && b == 0)
        {
            break;
        }

        if ((b % a) == 0)
        {
            printf("factor\n");

        }
        else if ((a % b) == 0)
        {
            printf("multiple\n");

        }
        else if ((a % b) != 0 && (b % a) != 0)
        {
            printf("neither\n");

        }
    }


    return 0;
}