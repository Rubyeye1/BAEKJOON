#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int a[500000] = { 0, };
int b[8001] = { 0, };
int compare(const void* a, const void* b)
{
	int temp1 = *(int*)a;
	int temp2 = *(int*)b;

	if (temp1 < temp2)
	{
		return -1;
	}
	else if (temp1 > temp2)
	{
		return 1;
	}
	else 
	{
		return 0;
	}
}

int main(void)
{
	int N;
	scanf("%d", &N);

	int i;
	int temp=0;
	for (i = 0; i < N; i++)
	{
		scanf("%d", &temp);
		a[i] = temp;
		b[temp + 4000] = b[temp + 4000] + 1;
	}

	int average=0;
	int middle = 0;
	int range = 0;

	for (i = 0; i < N; i++)
	{
		average = average + a[i];
	}

	qsort(a, N, sizeof(int), compare);

	middle = a[(N / 2)];

	range = a[N - 1] - a[0];

	if ((double)average / N > -1 && (double)average / N < 0)
	{
		printf(("0\n%d\n"), middle);
	}
	else
	{
		printf("%.0f\n%d\n", (double)average / N, middle);
	}

	int maxcount = 0;
	int tempp = 0;
	for (i = 0; i < 8001; i++)
	{
		if (b[i] > maxcount)
		{
			maxcount = b[i];
			tempp = i;
		}
	}
	int tempcount = 0;
	for (i = 0; i < 8001; i++)
	{
		if (b[i] == maxcount)
		{
			tempcount = tempcount + 1;
		}
	}
	int max = 0;
	int final = 0;
	int finalcount = 0;
	if (tempcount == 1)
	{
		max = tempp - 4000;
		printf("%d\n", max);
	}
	else
	{
		for (i = 0; i < 8001; i++)
	 	{
			if (b[i] == maxcount)
			{
				final = i - 4000;
				finalcount = finalcount + 1;
		    }
			if (finalcount == 2)
			{
				break;
			}
		}
		printf("%d\n", final);
	}

	printf("%d", range);



	return 0;
}