#include <stdio.h>

int main(void)
{
	int N;
	int i;
	int x=0;
	char a[100];
	int b[100];

	scanf("%d", &N);

    scanf("%s", &a);

	for (i = 0; i < N; i++)
	{
		b[i] = a[i] - '0';
	}
	for (i = 0; i < N; i++)
	{
		x = x + b[i];
	}

	printf("%d", x);

	return 0;
}