#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int repo[1000001] = { 0, };

int main(void)
{
	int M;
	int N;
	scanf("%d %d", &M, &N);

	repo[1] = 1;

	int i;
	int j;
	for (i = 2; i <= N; i++)
	{
		for (j = 2; j <= N; j++)
		{
			if ((i * j) > N)
			{
				break;
			}
			repo[i * j] = 1;
		}
	}
	for (i = M; i <= N; i++)
	{
		if (repo[i] == 0)
		{
			printf("%d\n", i);
		}
	}
	
	return 0;
}