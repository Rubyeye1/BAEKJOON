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
   
    int ii =0;
    int jj =0;
    int temp=0;
    for (i = 0; i < M; i++)
    {
        scanf("%d %d", &ii, &jj);
        temp = a[ii];
        a[ii] = a[jj];       
        a[jj] = temp;        
    }
    
    for (i = 1; i < N+1; i++)
    {
        printf("%d ", a[i]);
    }

    return 0;
}