#include <stdio.h>

int main(void)
{
	int a;
	int b;
	int total;
	int i;

	for (i = 0; i < i+1; i++)
	{
		scanf("%d %d", &a, &b);
		if (a == 0 && b == 0)
		{
			break;
		}
		total = a + b;
		printf("%d\n", total);
    }

	return 0;
}