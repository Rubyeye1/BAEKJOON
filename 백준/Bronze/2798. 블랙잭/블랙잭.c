#include <stdio.h>
#include <limits.h>
#include <math.h>
#include <string.h>

int main(void)
{
	int a[100] = { 0, };
	int N, M;
	scanf("%d %d", &N, &M);

	int i;
	for (i = 0; i < N; i++)
	{
		scanf("%d", &a[i]);
	}

	int j;
	int k;
	int sum = 0;
	int temp = 0;
	for (i = 0; i < N - 2; i++)
	{
		for (j = i+1; j < N - 1; j++)
		{
			for (k = j+1; k < N ; k++)
			{
				sum= sum+ a[i] + a[j] + a[k];
				if (sum <= M &&temp<=sum)
				{
					temp = sum;
				}
				sum = 0;
			}
		}
	}

	printf("%d", temp);

	return 0;
}	