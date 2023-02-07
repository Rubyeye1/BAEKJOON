#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
	int N;
	scanf("%d", &N);
	int i;
	int a[1000] = { 0, };
	int temp;
	for (i = 0; i < N; i++)
	{
		scanf("%d", &temp);
		a[i] = temp;
	}
	int j;
	int temp2=0;
	for (i = 0; i < N; i++)
	{
		for (j = i+1; j < N; j++)
		{
			if (a[i] > a[j])
			{
				temp2 = a[i];
				a[i] = a[j];
				a[j] = temp2;
			}
		}
	}
	for (i = 0; i < N; i++)
	{
		printf("%d\n", a[i]);
	}
	
	return 0;
}
