#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
	int A;
	int B;
	int V;
	
	scanf("%d %d %d", &A, &B, &V);
	int result = 1;
	
	if (A >= V)
	{
		printf("1");
	}

	else
	{
		if ((V - A) % (A - B) == 0)
		{
			result = (V - A) / (A - B) + result;
			printf("%d", result);
		}
		else
		{
			result = (V - A) / (A - B) + result + 1;
			printf("%d", result);
		}
	}

	
	
	return 0;
}