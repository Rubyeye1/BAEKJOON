#include <stdio.h>
#include <limits.h>
#include <math.h>
#include <string.h>

int main(void)
{
	int a1;
	int a0;
	int c;
	int n0;

	scanf("%d %d", &a1, &a0);
	scanf("%d", &c);
	scanf("%d", &n0);


	if (a1 <= c)
	{
		if (((a1 * n0) + a0) <= (n0 * c))
		{
			printf("1");
		}
		else
		{
			printf("0");
		}
	}
	else
	{
		printf("0");
	}
	

	
	



	return 0;
}	