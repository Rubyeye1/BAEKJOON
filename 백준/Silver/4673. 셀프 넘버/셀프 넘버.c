#include <stdio.h>

int dn(int n)
{
	int sum=0;

	if (n < 10)
	{
		sum = 2 * n;
	}
	else if (n >= 10 && n < 100)
	{
		sum = n + (n / 10) + (n % 10);
	}
	else if (n >= 100 && n < 1000)
	{
		sum = n + (n / 100) + (n % 10) + ((n - (n % 10) - ((n / 100) * 100))/10);
	}
	else if (n >= 1000 && n < 10000)
	{
		sum = n + (n % 10) + (n / 1000) + ((n / 100) - ((n / 1000) * 10)) + ((n/10)-((n/100)*10));
	}
	else if (n == 10000)
	{
		sum = 10001;
	}

	return sum;
}




int main(void)
{
	int a[11000] = { 0 ,};
	int lastsum;
	int i;

	for (i = 1; i <= 10000; i++)
	{
		lastsum = dn(i);
		a[lastsum] = lastsum;
	}

	for (i = 1; i <= 10000; i++)
	{
		if (a[i] == 0)
		{
			printf("%d\n", i);
		}
	}



	return 0;
}