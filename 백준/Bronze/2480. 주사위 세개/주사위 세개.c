#include <stdio.h>

int main(void)
{
	int a;
	int b;
	int c;
	int d;

	scanf("%d %d %d", &a, &b, &c);

	if (a == b && b == c & c == a)
	{
		d = 10000 + (a * 1000);
		printf("%d", d);
	}

	if (a != b && a != c && b != c)
	{
		if (a > b && a > c)
		{
			d = a * 100;
			printf("%d", d);
		}

		if (b > c && b > a)
		{
			d = b * 100;
			printf("%d", d);
		}
		if (c > a && c > b)
		{
			d = c * 100;
			printf("%d", d);
		}
	}

	if (a == b && a != c && b != c)
	{
		d = 1000 + (a * 100);
		printf("%d", d);
	}

	if (a != b && a == c && b != c)
	{
		d = 1000 + (a * 100);
		printf("%d", d);
	}
	if (a != b && a != c && b == c)
	{
		d = 1000 + (b * 100);
		printf("%d", d);
	}
	return 0;
}