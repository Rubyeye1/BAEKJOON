#include <stdio.h>

int main(void)
{
	int a[10];
	int i;
	int j;
	int num;
	int b[42] = { 0 };
	int x = 0;

	for (i = 0; i < 10; i++)
	{
		scanf("%d", &num);
		a[i] = num;
		a[i] = a[i] % 42;
	}

	for (i = 0; i < 10; i++)
	{
		for (j = 0; j < 42; j++)
		{
			if (a[i] == j)
			{
				b[j] = b[j] + 1;
			}
		}
	}

	for (i = 0; i < 42; i++)
	{
		if (b[i] != 0)
		{
			x = x + 1;
		}
	}

	printf("%d", x);


	return 0;
}