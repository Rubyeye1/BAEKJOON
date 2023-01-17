#include <stdio.h>

int main(void)
{
	int N;
	int a[1000000];
	int i;
	int plus;
	int maximum;
	int minimum;

	scanf("%d", &N);

	for (i = 0; i < N; i++)
	{
		scanf("%d", &plus);
		a[i] = plus;
	}

	if (a[0] > a[1])
	{
		maximum = a[0];
	}

	if (a[0] < a[1])
	{
		minimum = a[0];
	}
	for (i = 1; i < N; i++)
	{
		if (maximum < a[i])
		{
			maximum = a[i];
		}
		
	}

	for (i = 1; i < N; i++)
	{
		if (minimum > a[i])
		{
			minimum = a[i];
		}
	}

	printf("%d %d", minimum, maximum);

	return 0;
}