#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int repo[1000001] = { 0, };

int main(void)
{
	while (1)
	{
		int n;
		scanf("%d", &n);
	
		if (n == 0)
		{
			break;
		}

		repo[1] = 1;

		int i;
		int j;
		for (i = 2; i <= (2*n) ; i++)
		{
			for (j = 2; j <= (2*n) ; j++)
			{
				if ((i * j) > (2*n))
				{
					break;
				}
				repo[i * j] = 1;
			}
		}

		int count = 0;
		for (i = (n+1); i <= (2*n); i++)
		{
			if (repo[i] == 0)
			{
				count = count + 1;
			}
		}

		printf("%d\n", count);

	}
	
	
	return 0;
}
