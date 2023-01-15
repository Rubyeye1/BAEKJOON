#include <stdio.h>

int main(void)
{
	int A = 0;
	int B = 0;
	int C = 0;

	scanf("%d %d %d", &A, &B, &C);

	printf("%d\n", (A + B) % C);
	printf("%d\n", ((A%C)+(B%C))%C);
	printf("%d\n", (A * B) % C);
	printf("%d", ((A%C)*(B%C))%C);
	


	return 0;
}