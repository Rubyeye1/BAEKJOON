#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void)
{
	int N;
	scanf("%d", &N);

	if (N == 4)
	{
		printf("-1");
    }
	else if (N == 3)
	{
		printf("1");
	}
	else if (N == 5)
	{
		printf("1");
	}
	else if (N == 7)
	{
		printf("-1");
	}
	else if(N>5)
	{
		int count = 0;
		while (1)
		{
			N = N - 5;
			if (N < 0)
			{
				break;
			}
			else if (N == 0)
			{
				printf("%d", count+1);
				break;
			}
			count = count + 1;
		}

		if (N != 0)
		{
			
				N = N + 5;
				if ((N % 3) == 0)
				{
					count = count + 1;
					printf("%d", count);
				}
				else
				{
					while (count >= 0)
					{
						if (count < 0)
						{
							printf("-1");
							break;
						}
						N = N + 5;
						if (N % 3 == 0)
						{
							count = count + (N / 3) - 1;
							printf("%d", count);
							break;
						}
						count = count - 1;
					}
				}
			
		}
		
	}

	return 0;
}