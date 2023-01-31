#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
	int N;
	scanf("%d", &N);

	int i;
	int a = 1;
	for (i = 0; i < 1000000000; i++)
	{
		a = a + 6 * i;
		if (N == 1)
		{
			printf("1");
			break;
		}
		else if (N <= a)
		{
			printf("%d", i+1);
			break;
		}
	}
	
	
	return 0;
}