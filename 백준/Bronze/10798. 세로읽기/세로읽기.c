#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <math.h>

int main() {
   
    char a[5][16] = {"!!!!!!!!!!!!!!!","!!!!!!!!!!!!!!!" ,"!!!!!!!!!!!!!!!" ,"!!!!!!!!!!!!!!!" ,"!!!!!!!!!!!!!!!" };
    int i;
    int j;
   
    for (i = 0; i < 5; i++)
    {
        scanf("%s", a[i]);
    }
    for (i = 0; i < 15; i++)
    {
        for (j = 0; j < 5; j++)
        {
            if (a[j][i] != '\0' && a[j][i] != '!')
            {
                printf("%c", a[j][i]);
            }
        }
    }


    return 0;
}