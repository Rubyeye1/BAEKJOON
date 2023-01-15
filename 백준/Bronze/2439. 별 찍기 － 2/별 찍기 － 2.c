#include <stdio.h>

int main(void)
{
	int t;
	int i;
	int j;
	int a;

	scanf("%d", &t);

	for (i = 0; i < t; i++)
	{
		for (a = 0; a <t-i-1 ; a++)
		{
			printf(" ");
		}
		for (j = 0 ; j < i+1; j++)
		{
			printf("*");
		}
		printf("\n");
	}

	return 0;
}