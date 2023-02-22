#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <math.h>


int main() {

    int N;
    int M;
    scanf("%d %d", &N, &M);
    int a[101] ;
    int i;
    for (i = 0; i < 101; i++)
    {
        a[i] = i;
    }
   
    int q;
    int w;
    int j;
    int temp1;
    int temp2;
    int temp3;
    for (i = 0; i < M; i++)
    {
        scanf("%d %d", &q, &w);
        temp1 = q;
        temp2 = w;
        for (j = 0; j < (w - q + 1) / 2; j++)
        {
            temp3 = a[temp1];
            a[temp1] = a[temp2];
            a[temp2] = temp3;
            temp1++;
            temp2--;
        }
    }
  

    for (i = 1; i <= N; i++)
    {
        printf("%d ", a[i]);
    }
        

    return 0;
}