#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int compare(const void* a, const void* b)
{
	int temp1 = *(int*)a;
	int temp2 = *(int*)b;
	if (temp1 < temp2)
	{
		return -1;
	}
	else if (temp1 > temp2)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

int a[1000000] = { 0, };
int main(void)
{
	int N;
	scanf("%d", &N);
	int i;
	int temp = 0;
	for (i = 0; i < N; i++)
	{
		scanf("%d", &temp);
		a[i] = temp;
	}

	qsort(a, N, sizeof(int), compare);

	for (i = 0; i < N; i++)
	{
		printf("%d\n", a[i]);
	}

	return 0;
}