#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void)
{
	int N;
	int M;

	scanf("%d %d\n", &N, &M);

	int a[100][100] = { 0, };
	int b[100][100] = { 0, };

	int i;
	int j;
	for (i = 0; i < N; i++)
	{
		for (j = 0; j < M; j++)
		{
			scanf("%d", &a[i][j]);
		}
	}

	for (i = 0; i < N; i++)
	{
		for (j = 0; j < M; j++)
		{
			scanf("%d", &b[i][j]);
		}
	}

	for (i = 0; i < N; i++)
	{
		for (j = 0; j < M; j++)
		{
			printf("%d ", a[i][j] + b[i][j]);
		}
		printf("\n");
	}

	return 0;
}