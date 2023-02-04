#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void)
{
	int N;
		
	scanf("%d", &N);

	int a = 2;

	if (N != 1)
	{
		while (1)
		{
			if (N == 1)
			{
				break;
			}
			if ((N % a) == 0)
			{
				N = N / a;
				printf("%d\n", a);
			}
			else
			{
				a = a + 1;
			}
			
		}
	}

	return 0;
}
