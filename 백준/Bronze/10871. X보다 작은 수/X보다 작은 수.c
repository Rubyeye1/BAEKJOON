#include <stdio.h>

int main(void)
{
	int N;
	int X;
	int i;
	int plus;

	scanf("%d %d", &N, &X);

	int a[10000];

	for (i = 0; i < N; i++)
	{
		scanf("%d", &plus);
		a[i] = plus;
	}

	for (i = 0; i < N; i++)
	{
		if (a[i] < X)
		{
			printf("%d ", a[i]);
		}
	}




	return 0;
}