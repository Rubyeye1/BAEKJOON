#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
	char a[16];

	scanf("%s", a);

	int len;
	len = strlen(a);
	int i;

	int sum=0;

	for (i = 0; i < len; i++)
	{
		if (a[i] == 'A' || a[i] == 'B' || a[i] == 'C')
		{
			sum = sum + 3;
		}
		else if (a[i] == 'D' || a[i] == 'E' || a[i] == 'F')
		{
			sum = sum + 4;
		}
		else if (a[i] == 'G' || a[i] == 'H' || a[i] == 'I')
		{
			sum = sum + 5;
		}
		else if (a[i] == 'J' || a[i] == 'K' || a[i] == 'L')
		{
			sum = sum + 6;
		}
		else if (a[i] == 'M' || a[i] == 'N' || a[i] == 'O')
		{
			sum = sum + 7;
		}
		else if (a[i] == 'P' || a[i] == 'Q' || a[i] == 'R' || a[i] == 'S')
		{
			sum = sum + 8;
		}
		else if (a[i] == 'T' || a[i] == 'U' || a[i] == 'V')
		{
			sum = sum + 9;
		}
		else if (a[i] == 'W' || a[i] == 'X' || a[i] == 'Y' || a[i] == 'Z')
		{
			sum = sum + 10;
		}

	}
	printf("%d", sum);


	
	return 0;
}