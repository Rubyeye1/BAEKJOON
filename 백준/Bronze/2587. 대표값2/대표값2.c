#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
	int a[5] = { 0, };

	int i;
	int temp=0;
	for (i = 0; i < 5; i++)
	{
		scanf("%d", &temp);
		a[i] = temp;
	}

	int x=0;
	int middle=0;

	for (i = 0; i < 5; i++)
	{
		x = x + a[i];
	}

	x = x / 5;

	int j;
	int temp2=0;
	for (i = 0; i < 5; i++)
	{
		for (j = i + 1; j < 5; j++)
		{
			if (a[i] > a[j])
			{
				temp2 = a[i];
				a[i] = a[j];
				a[j] = temp2;
			}
		}
	}
	middle = a[2];
	printf("%d\n%d", x,middle);


	return 0;
}