#include <stdio.h>

int main(void)
{
	int a[31] = { 0 };
	int i;
	int x;
	int t;

	for (i = 1; i < 29; i++)
	{
		scanf("%d", &x);
		a[x] = x;
	}

	for (i = 1; i < 31; i++)
	{
		if (a[i] == 0)
		{
			printf("%d\n", i);
		}
	}



	return 0;
}