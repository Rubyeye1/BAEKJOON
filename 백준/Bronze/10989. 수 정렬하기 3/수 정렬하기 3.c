#include <stdio.h>
#include <string.h>
#include <stdlib.h>



int count[10001] = { 0, };
int main(void)
{
	int N;
	scanf("%d", &N);

	int a;
	int i;
	for (i = 0; i < N; i++)
	{
		scanf("%d", &a);
		count[a] = count[a] + 1;
	}

	int j;
	for (i = 0; i < 10001; i++)
	{
		if (count[i] != 0)
		{
			for (j = 0; j < count[i]; j++)
			{
				printf("%d\n", i);
			}
		}
	}

	return 0;
}
