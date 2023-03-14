#include <stdio.h>
#include <limits.h>
#include <math.h>
#include <string.h>

int main(void)
{
	int kg[50] = { 0, };
	int cm[50] = { 0, };
	int N;
	scanf("%d", &N);

	int i;
	for (i = 0; i < N; i++)
	{
		scanf("%d %d", &kg[i], &cm[i]);
	}


	int j;
	for (i = 0; i < N; i++)
	{
		int count = 0;
		if (i == 0)
		{
			for (j = 1; j < N; j++)
			{
				if (kg[i] < kg[j] && cm[i] < cm[j])
				{
					count = count + 1;
				}
			}
			printf("%d ", count+1);
		}
		else
		{
			for (j = 0; j < i; j++)
			{
				if (kg[i] < kg[j] && cm[i] < cm[j])
				{
					count = count + 1;
				}
			}
			for (j = i; j < N; j++)
			{
				if (kg[i] < kg[j] && cm[i] < cm[j])
				{
					count = count + 1;
				}
			}
			printf("%d ", count+1);
		}
	}


	return 0;
}	