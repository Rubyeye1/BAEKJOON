#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void)
{
	int M;
	int N;
	int repo[10001] = { 0, };

	scanf("%d", &M);
	scanf("%d", &N);

	int i = 0;
	int j = 0;                 
	
	for (i = M; i <= N; i++)
	{
		repo[i] = i;
		for (j = 2; j <= (i/2); j++)
		{
			if ((i % j) == 0)
			{
				repo[i] = 0;
				break;
			}
		}
	}
	if (repo[1] == 1)
	{
		repo[1] = 0;
	}
	int firstmim=0;
	int sum=0;

	for (i = 0; i < 10001; i++)
	{
		if (repo[i] != 0)
		{
			sum = sum + repo[i];
		}
	}
	for (i = 0; i < 10001; i++)
	{
		if (repo[i] != 0)
		{
			firstmim = repo[i];
			break;
		}
	}

	if (sum == 0 & firstmim == 0)
	{
		printf("-1");
	}
	else
	{
		printf("%d\n%d", sum, firstmim);
	}

	return 0;
}
