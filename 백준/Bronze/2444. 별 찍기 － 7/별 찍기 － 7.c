#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <math.h>


int main() {
    int N;
    scanf("%d", &N);

    int i;
    int j;
    int temp = (N * 2) - 1;
    int temp2 = N;
    for (i = 1; i <= N * 2 - 1; i++)
    {   
        
        if (i <= N)
        {
            for (j = i; j < N; j++)
            {
                printf(" ");
            }
            printf("*");
            for (j = 0; j < i - 1; j++)
            {
                printf("**");
            }
        }
        else
        {
            for (j = i; j > N; j--)
            {
                printf(" ");
            }
            printf("*");
            for (j = temp; j > i; j--)
            {
                printf("**");
            }
        }
        printf("\n");
    }


    return 0;
}
