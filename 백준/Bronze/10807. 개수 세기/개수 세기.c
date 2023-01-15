#include <stdio.h>

int main(void)
{
	int N;
	int num;
	int num2;
	int i;
	int j;
	int k=0;

	scanf("%d", &N);
	int a[100];

	for (i = 0; i < N; i++)
	{
		scanf("%d", &num);
		a[i] = num;
	}

	scanf("%d", &num2);
	for (j = 0; j < N; j++)
	{
		if (num2 == a[j])
		{
			k = k + 1;
		}
	}
	printf("%d", k);

	return 0;
}