#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

int fibonacci(int a)
{
	if (a == 1)
	{
		return 1;
	}
	else if (a == 0)
	{
		return 0;
	}
	return fibonacci(a-1) + fibonacci(a - 2);
}

int main(void){
	int n;
	scanf("%d", &n);
	int a = fibonacci(n);
	printf("%d", a);

	return 0;
}