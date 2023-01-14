#include <stdio.h>

int main(void)
{
	int total;
	int one;
	int price;
	int many;
	int value=0;
	int i;

	scanf("%d\n%d", &total, &one);

	for (i = 0; i < one; i++)
	{
		scanf("%d %d", &price, &many);
		value = value + price * many;

	}
	if (total == value)
	{
		printf("Yes");
	}
	else
	{
		printf("No");
	}


	return 0;
}