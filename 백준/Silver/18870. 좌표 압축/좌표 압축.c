#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

typedef struct compaare {
	int x;
	int repo;
}d;

int compare(const void* a, const void* b)
{
	d temp1 = *(d*)a;
	d temp2 = *(d*)b;
	if (temp1.x < temp2.x)
	{
		return -1;
	}
	else if (temp1.x > temp2.x)
	{
		return 1;
	}
	else 
	{
		return 0;
	}
}
	

d a[1000000];
d b[1000000];
int main(void){

	int N;
	scanf("%d", &N);

	int i;

	for (i = 0; i < N; i++)
	{
		scanf("%d", &a[i].x);
		a[i].repo = i;
	}

	qsort(a, N, sizeof(d), compare);
	
	int temp=-1;
	int minimum = INT_MIN;

	for (i = 0; i < N; i++)
	{
		if (a[i].x > minimum)
		{
			minimum = a[i].x;
			temp = temp + 1;
		}
		b[a[i].repo].x = temp;
	}

	for (i = 0; i < N; i++)
	{
		printf("%d ", b[i].x);
	}
	
	
	return 0;
}