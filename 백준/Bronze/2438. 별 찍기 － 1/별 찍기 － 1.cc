#include <stdio.h>

int main(void)
{
	int t;
	int i;
	int j;

	scanf("%d", &t);

	for (i = 0; i < t; i++)
	{
		printf("*");
		for (j = 0 ; j < i; j++)
		{
			printf("*");
		}
		printf("\n");
	}

	return 0;
}