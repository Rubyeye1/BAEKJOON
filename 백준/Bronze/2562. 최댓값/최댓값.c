#include <stdio.h>

int main(void)
{
	int a[9];
	int i;
	int plus=0;
	int maximum=0;
	int g=0;

	for (i = 0; i < 9; i++)
	{
		scanf("%d", &plus);
		a[i] = plus;
	}

	if (a[0] > a[1])
	{
		maximum = a[0];
		g = 1;
	}
	else
	{
		maximum = a[1];
		g = 2;
	}
	

	for (i = 2; i < 9; i++)
	{
		if (a[i] > maximum)
		{
			maximum = a[i];
			g = i+1;
		}
	}

	printf("%d\n%d", maximum,g);

	return 0;
}