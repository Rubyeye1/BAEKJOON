#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    int  A;
	int  B;
	int  C;

	int count;

	scanf("%d %d %d",&A,&B,&C);

	if (B >= C)
	{
		printf("-1");
	}
	else
	{
		count = (A / (C - B)) +1;
		printf("%d", count);
	}




	return 0;
}