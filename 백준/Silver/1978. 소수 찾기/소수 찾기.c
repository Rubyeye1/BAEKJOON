#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void)
{
	int N;
	scanf("%d", &N);

	int i;
	int j;
	int count = N;
	for (i = 0; i < N; i++)
	{
		int a;
		scanf("%d", &a);
		if (a == 1)
		{
			count = count - 1;
		}

		for (int j = 0; j < a; j++)
		{
			if (a != (j+1)  && (a % (j + 1)) == 0 && (j+1 != 1))
			{
				count = count - 1;
				break;
			}
		}
		
	}
	printf("%d", count);


	return 0;
}
