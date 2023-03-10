#include <stdio.h>
#include <limits.h>
#include <math.h>
#include <string.h>

int main(void)
{
	long long n;
	scanf("%lld", &n);

	long long  sum=0;
	long long  i;
	int count = n - 2;
	long long  temp = n - 2;
	for (i = 0; i < count; i++)
	{
		sum = sum + (temp * (i + 1));
		temp--;
	}

	
	printf("%lld\n3", sum);





	return 0;
}	