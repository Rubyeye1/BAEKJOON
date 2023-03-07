#include <stdio.h>
#include <limits.h>
#include <math.h>
#include <string.h>

int main(void)
{
	long long n;
	scanf("%lld", &n);
	long long result = 0;
	int i;
	for (i = 0; i < n - 1; i++)
	{
		result = result + i + 1;
	}
	printf("%lld\n2", result);



	return 0;
}