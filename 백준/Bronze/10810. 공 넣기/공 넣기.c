#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <math.h>


int main() {

    int N;
    int M;
    scanf("%d %d", &N,&M);
    int a[100] = { 0, };
    int i;
    int j;
    int ii;
    int jj;
    int kk;
    for (i = 0; i < M; i++)
    {
        scanf("%d %d %d", &ii, &jj, &kk);
        for (j = ii - 1; j < jj; j++)
        {
            a[j] = kk;
        }
    }
    for (i = 0; i < N; i++)
    {
        printf("%d ", a[i]);
    }

   

    return 0;
}
