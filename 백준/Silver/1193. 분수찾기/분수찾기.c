#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void)
{
	int X;

	scanf("%d", &X);

	int i;
	int a;
	for (i = 1; i < 10000000; i++)
	{
		if (( i* (i - 1)) / 2 < X && (i * (i + 1)) / 2 >= X)
		{
			a = i;
			break;
		}
	}

	int s = ((a+1)*a) / 2;
	int minus = s - X ;

	int up;
	int down;
	if ((a % 2) == 1)
	{
		up = a-(a-1) + minus;
		down = a - minus;
		printf("%d/%d", up, down);

	}
	else
	{
		up = a - minus;
		down = a - (a - 1) + minus;
		printf("%d/%d", up, down);
	}

	return 0;
}