#include <stdio.h>

int hansu(int n)
{
	int o= 0;
	if (n < 100)
	{
		o = n;
	}
	else if (n >= 100 && n < 1000)
	{
		if (((n / 100) - ((n / 10) - ((n / 100) * 10)))   == (((n / 10) - ((n / 100) * 10)) - (n%10)))
		{
			o = n;
		}
	}
	else
	{
		o = 0;
	}
	return o;



}

int main(void)
{
	int N;
	int i;
	int a[1001] = { 0, };
	int b = 0;
	int repo = 0;

	scanf("%d", &N);

	for (i = 1; i <= N; i++)
	{
		repo = hansu(i);
		a[i] = repo;
	}

	for (i = 1; i <= N; i++)
	{
		if (a[i] != 0)
		{
			b = b + 1;
		}
	}

	printf("%d", b);


	return 0;
}