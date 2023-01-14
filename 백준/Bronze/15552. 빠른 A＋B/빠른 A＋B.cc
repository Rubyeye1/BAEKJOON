#include <stdio.h>

int main(void)
{
	int T;
	int A;
	int B;
	int total;
	int i;

	scanf("%d", &T);
	for (i = 0; i < T; i++)
	{
		scanf("%d %d", &A, &B);
		total = A + B;
		printf("%d\n", total);
	}



	return 0;
}