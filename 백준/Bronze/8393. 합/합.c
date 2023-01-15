#include <stdio.h>

int main(void)
{
	int a;
	int i;
	int b = 0;

	scanf("%d", &a);
	
	for (i = 0; i < a; i++)
	{
		b = b + i + 1;
	}
	printf("%d", b);

	return 0;
}