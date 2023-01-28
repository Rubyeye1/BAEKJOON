#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
	char a[101];

	scanf("%s", a);
	
	int len;
	len = strlen(a);
	int i;
	int count = len;

	for (i = 0; i < len; i++)
	{
		if (a[i] == 'c' && a[i + 1] == '=')
		{
			count = count - 1;
		}
		else if (a[i] == 'c' && a[i + 1] == '-')
		{
			count = count - 1;
		}
		else if (a[i] == 'd' && a[i + 1] == 'z' && a[i+2] == '=')
		{
			count = count - 1;
		}
		else if (a[i] == 'd' && a[i + 1] == '-')
		{
			count = count - 1;
		}
		else if (a[i] == 'l' && a[i + 1] == 'j')
		{
			count = count - 1;
		}
		else if (a[i] == 'n' && a[i + 1] == 'j')
		{
			count = count - 1;
		}
		else if (a[i] == 's' && a[i + 1] == '=')
		{
			count = count - 1;
		}
		else if (a[i] == 'z' && a[i + 1] == '=')
		{
			count = count - 1;
		}
	}

	printf("%d", count);

	return 0;
}