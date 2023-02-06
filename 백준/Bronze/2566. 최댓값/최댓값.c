#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void)
{
	int a[9][9] = { 0, };

	int i;
	int j;
	for (i = 0; i < 9; i++)
	{
		for (j = 0; j < 9; j++)
		{
			scanf("%d", &a[i][j]);
		}
	}
	
	int max = a[0][0];
	int h=0;
	int y=0;

	for (i = 0; i < 9; i++)
	{
		for (j = 0; j < 9; j++)
		{
			if (a[i][j] >= max)
			{
				max = a[i][j];
				h = i+1;
				y = j+1;
			}
		}
	}

	printf("%d\n", max);
	printf("%d %d", h, y);

	return 0;
}