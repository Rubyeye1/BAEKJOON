#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <math.h>


int main() {
    char a[101];
    scanf("%s", &a);

    int len;
    int len2;

    len = (strlen(a)/2) ;
    len2 = strlen(a)-1;

    int i;
    int temp = 0;
    for (i = 0; i <= len; i++)
    {
        temp = i;
        if (temp == len)
        {
            printf("1");
            break;
        }
        if (a[i] != a[len2 - i])
        {
            printf("0");
            break;
        }
    }
    return 0;
}