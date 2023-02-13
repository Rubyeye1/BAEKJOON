#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

typedef struct compaare {
	int x;
	int y;
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
	else if(temp1.x == temp2.x)
	{
		if (temp1.y > temp2.y)
		{
			return 1;
		}
		else
		{
			return -1;
		}
	}
}




int main(void){

	int N;
	scanf("%d", &N);

	d a[100000];

	int i;
	for (i = 0; i < N; i++)
	{
		scanf("%d %d", &a[i].x, &a[i].y);
	}

	qsort(a, N, sizeof(d), compare);

	for (i = 0; i < N; i++)
	{
		printf("%d %d\n", a[i].x, a[i].y);
	}


	return 0;
}