#include <stdio.h>
#include <string.h>

int main(void)
{
	char a[100];
	scanf("%s", &a);

	int i;
	int j;
	int b[26] = {-1 ,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};

	for (i = 0; i < strlen(a); i++)
	{
			if (a[i] == 'a')
			{
				if (b[0] == -1)
				{
					b[0] = i;
				}
			}
			else if (a[i] == 'b')
			{
				if (b[1] == -1)
				{
					b[1] = i;
				}
			}
			else if (a[i] == 'c')
			{
				if (b[2] == -1)
				{
					b[2] = i;
				}
			}
			else if (a[i] == 'd')
			{
				if (b[3] == -1)
				{
					b[3] = i;
				}
			}
			else if (a[i] == 'e')
			{
				if (b[4] == -1)
				{
					b[4] = i;
				}
			}
			else if (a[i] == 'f')
			{
				if (b[5] == -1)
				{
					b[5] = i;
				}
			}
			else if (a[i] == 'g')
			{
				if (b[6] == -1)
				{
					b[6] = i;
				}
			}
			else if (a[i] == 'h')
			{
				if (b[7] == -1)
				{
					b[7] = i;
				}
			}
			else if (a[i] == 'i')
			{
				if (b[8] == -1)
				{
					b[8] = i;
				}
			}
			else if (a[i] == 'j')
			{
				if (b[9] == -1)
				{
					b[9] = i;
				}
			}
			else if (a[i] == 'k')
			{
				if (b[10] == -1)
				{
					b[10] = i;
				}
			}
			else if (a[i] == 'l')
			{
				if (b[11] == -1)
				{
					b[11] = i;
				}
			}
			else if (a[i] == 'm')
			{
				if (b[12] == -1)
				{
					b[12] = i;
				}
			}
			else if (a[i] == 'n')
			{
				if (b[13] == -1)
				{
					b[13] = i;
				}
			}
			else if (a[i] == 'o')
			{
				if (b[14] == -1)
				{
					b[14] = i;
				}
			}
			else if (a[i] == 'p')
			{
			if (b[15] == -1)
			{
				b[15] = i;
			}
			}
			else if (a[i] == 'q')
			{
			if (b[16] == -1)
			{
				b[16] = i;
			}
			}
			else if (a[i] == 'r')
			{
			if (b[17] == -1)
			{
				b[17] = i;
			}
			}
			else if (a[i] == 's')
			{
			if (b[18] == -1)
			{
				b[18] = i;
			}
			}
			else if (a[i] == 't')
			{
			if (b[19] == -1)
			{
				b[19] = i;
			}
			}
			else if (a[i] == 'u')
			{
			if (b[20] == -1)
			{
				b[20] = i;
			}
			}
			else if (a[i] == 'v')
			{
			if (b[21] == -1)
			{
				b[21] = i;
			}
			}
			else if (a[i] == 'w')
			{
			if (b[22] == -1)
			{
				b[22] = i;
			}
			}
			else if (a[i] == 'x')
			{
			if (b[23] == -1)
			{
				b[23] = i;
			}
			}
			else if (a[i] == 'y')
			{
			if (b[24] == -1)
			{
				b[24] = i;
			}
			}
			else if (a[i] == 'z')
			{
			if (b[25] == -1)
			{
				b[25] = i;
			}
			}
		}
	
	for (i = 0; i < 26; i++)
	{
		printf("%d ", b[i]);
	}
	return 0;
}