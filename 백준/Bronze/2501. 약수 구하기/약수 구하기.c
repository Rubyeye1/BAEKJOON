#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <math.h>

int main() {
   
    int N, K;
    scanf("%d %d", &N, &K);

    int i;
    int temp = N;
    int count = 0;
    int temp2 = 0;
    for (i = 1; i <= N; i++)
    {
        if ((temp) % i == 0)
        {
            temp2 = i;
            count = count + 1;
            if (count == K)
            {
                printf("%d", temp2);
                break;
            }
        }
    }
    if (count < K)
    {
        printf("0");
    }


    return 0;
}
