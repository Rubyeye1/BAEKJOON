#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <math.h>


int main() {
    int N;
    int M;
    scanf("%d %d", &N,&M);

    int a[101] = { 0, };
    int b[101] = { 0, };
    int i=0;
    for (i = 0; i < 101; i++)
    {
        a[i] = i;
    }

    int j=0;
    int k=0;
    int ii = 0;
    int jj = 0;
    int kk = 0;
    for (i = 0; i < M; i++)
    {
        scanf("%d %d %d", &ii, &jj, &kk);
        for (j = ii; j <= jj; j++)
        {
            b[j] = a[j];
        }
        int temp = jj - kk+1;
        for (j = ii; j < kk; j++)
        {
            a[j + temp] = b[j];
        }
        int temp2 = kk;
        for (j = ii; j < ii+temp; j++)
        {
            a[j] = b[temp2];
            temp2++;
        }
    }

    for (i = 1; i <= N; i++) 
    {
        printf("%d ", a[i]);
    }
    

    return 0;
}
