#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <math.h>

int main() {
   
    while (1)
    {
        int a[100001] = { 0, };
        int N;
        scanf("%d", &N);
        if (N == -1)
        {
            break;
        }

        int i;
        int temp = N;
        int count = 0;
        int temp2 = 0;
        for (i = 1; i <= (N/2); i++)
        {
            if ((temp % i) == 0)
            {
                a[i] = i;
                count = count + 1;      
                temp2 = temp2 + i;
            }
        }


        int count2 = 0;                           
        int count3 = count - 1;

        if (temp2 == N)                    
        {
            printf("%d = ", N);
            for (i = 1; i <= (N/2); i++)
            {
                if (a[i] != 0 && count2 != count3)
                {
                    printf("%d + ", a[i]);
                    count2 = count2 + 1;
                }
                else if (a[i] != 0 && count2 == count3)
                {
                    printf("%d\n", a[i]);
                    break;
                }
            }
        }
        else
        {
            printf("%d is NOT perfect.\n", N);
        }
    }
    
    return 0;
}