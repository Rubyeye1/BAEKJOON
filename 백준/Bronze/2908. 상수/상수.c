#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
	char a[8];
	char repo[8];
	char repo2[4];
	char repo3[4];
	
	scanf("%[^\n]", a);

	int i;
	for (i = 0; i < 8; i++)
	{
		repo[i] = a[i];
	}

	a[0] = repo[2];
	a[2] = repo[0];
	a[4] = repo[6];
	a[6] = repo[4];
 
	for (i = 0; i < 3; i++)
	{
		repo2[i] = a[i];
	}
	for (i = 4; i < 7; i++)
	{
		repo3[i-4] = a[i];
	}

	int num1;
	int num2;
	num1 = atoi(repo2);
	num2 = atoi(repo3);

	if (num1 > num2)
	{
		printf("%d", num1);
	}
	else
	{
		printf("%d", num2);
	}


	
	return 0;
}