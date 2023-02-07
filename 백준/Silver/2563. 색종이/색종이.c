#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void)
{
	int T;
	scanf("%d", &T);

	int repo[100][100] = { 0, };
	int i;
	int j;
	int k;
	int left=0;
	int height=0;
	for (i = 0; i < T; i++)
	{
		scanf("%d %d", &left, &height);
		for (j = left; j < left+10; j++)
		{
			for (k = height; k < height + 10; k++)
			{
				repo[j][k] = 1;
			}
		}
	}

	int count=0;

	for (i = 0; i < 100; i++)
	{
		for (j = 0; j < 100; j++)
		{
			if (repo[i][j] == 1)
			{
				count = count + 1;
			}
		}
	}

	printf("%d", count);
	return 0;
}