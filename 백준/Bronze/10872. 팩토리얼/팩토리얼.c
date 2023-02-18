#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

int factorial(int a)
{
	if (a <= 1)
	{
		return 1;
	}
	return a * factorial(a-1);
}

int main(void){
	int N;
	scanf("%d", &N);
	int a = factorial(N);
	printf("%d", a);

	return 0;
}