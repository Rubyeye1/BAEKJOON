#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

typedef struct compaare {
	char name[101];
	int old;
	int count;
}d;

int compare(const void* a, const void* b)
{
	d temp1 = *(d*)a;
	d temp2 = *(d*)b;
	if (temp1.old < temp2.old)
	{
		return -1;
	}
	else if (temp1.old > temp2.old)
	{
		return 1;
	}
	else if (temp1.old == temp2.old)
	{
		if (temp1.count < temp2.count)
		{
			return -1;
		}
		else if (temp1.count > temp2.count)
		{
			return 1;
		}
		return 0;
	}
}


d a[100000];

int main(void){

	int N;
	scanf("%d", &N);

	int i;

	for (i = 0; i < N; i++)
	{
		scanf("%d %s", &a[i].old, &a[i].name);
		a[i].count = i;
	}

	qsort(a, N, sizeof(d), compare);

	for (i = 0; i < N; i++)
	{
		
		printf("%d %s\n", a[i].old, a[i].name);

	}

	return 0;
}