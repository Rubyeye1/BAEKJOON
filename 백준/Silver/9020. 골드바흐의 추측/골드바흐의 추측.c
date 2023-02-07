#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int repo[10001] = { 0, };
int main(void)
{
	repo[0] = 1;
	repo[1] = 1;
	int i;
	int j;
	for (i = 2; i < 10001; i++)
	{
		for (j = 2; j < 10001; j++)
		{
			if ((i * j) > 10000)
			{
				break;
			}
			repo[i * j] = 1;
		}
	}

	int T;
	scanf("%d", &T);

	int n;

	for (i = 0; i < T; i++)
	{      
		scanf("%d", &n);
		for (j = (n / 2); j > 0; j--)
		{
			if (repo[j] != 1 && repo[n - j] != 1)
			{
				printf("%d %d\n", j, n - j);
				break;
			}
		}
	}
	
	return 0;
}