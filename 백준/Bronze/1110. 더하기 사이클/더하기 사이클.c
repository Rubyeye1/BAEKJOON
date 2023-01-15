#include <stdio.h>

int main(void)
{
	int a;
	int b=0;
	int c=0;
	int d=0;
	int e=0;
	int i;
	int f;

	
	scanf("%d", &a);

	if (a >= 10)
	{
		c = a / 10;
		d = a % 10;
		e = c + d;
		f = e % 10;
		b = d * 10 + f;
	}
	else
	{
		c = 0;
		d = a % 10;
		e = c + d;
		f = e % 10;
		b = d * 10 + f;
	}
	i = 1;

	while (a != b)
	{
		if (b >= 10)
		{
			c = b / 10;
			d = b % 10;
			e = c + d;
			f = e % 10;
			b = d*10 + f;
			
		}
		else
		{
			c = 0;
			d = b % 10;
			e = c + d;
			f = e % 10;
			b = d*10 + f;
		}
		i = i + 1;
	}
	printf("%d", i);
	
	return 0;
}