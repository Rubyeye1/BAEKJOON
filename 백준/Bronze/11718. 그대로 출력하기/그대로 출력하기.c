#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <math.h>


int main() {
    char a[101];
    int i;
    while (scanf("%[^\n]%*c", &a)!=EOF)
    {
        int temp = strlen(a);
        for (i = 0; i < temp; i++)
        {
            printf("%c", a[i]);
        }
        printf("\n");
    }
   
    return 0;
}