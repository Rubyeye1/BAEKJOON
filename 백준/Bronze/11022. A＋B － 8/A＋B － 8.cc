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
		printf("Case #%d: %d + %d = %d\n", i + 1,A,B, total);
	}


	return 0;
}