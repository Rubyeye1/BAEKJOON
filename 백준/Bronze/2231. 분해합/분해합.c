#include <stdio.h>
#include <limits.h>
#include <math.h>
#include <string.h>

int main(void)
{
	int n;
	scanf("%d", &n);

	int i;
	if (n == 1)
	{
		printf("0");
	}
	for (i = 1; i < n; i++)
	{                           
		int sum = 0;
		int temp2 = i;
		int temp3 = 0;
		while (temp2>0)
		{
			sum = sum + (temp2 % 10);
			temp2 = temp2 / 10;
		}
		temp3 = i + sum;
		if (temp3 == n)
		{
			printf("%d",i);
			break;
		}
		if (i == n - 1)
		{
			printf("0");
		}

	}


	return 0;
}	