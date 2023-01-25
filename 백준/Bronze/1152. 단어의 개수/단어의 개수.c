#include <stdio.h>
#include <string.h>

int main(void)
{
	char a[1000001];

	scanf("%[^\n]", a);

	int len = 0;
	len = strlen(a);

	int i;
	int count = 0;

	for (i = 0; i < len; i++)
	{

		if (a[i] == ' ')
		{
			count = count + 1;
		}
	}
	if (a[0] != ' ' && a[len - 1] != ' ')
	{
		count = count + 1;
	}
	if (a[0] != ' ' && a[len - 1] == ' ')
	{
		count = count;
	}
	if (a[0] == ' ' && a[len - 1] == ' ')
	{
		count = count - 1;
	}
	if (a[0] == ' ' && a[len - 1] != ' ')
	{
		count = count;
	}

	


	printf("%d", count);

	
	return 0;
}