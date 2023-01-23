#include <stdio.h>
#include <string.h>

int main(void)
{
	int T;
	int i;
	int j;
	int k;
	int R;

	scanf("%d", &T);

	for (i = 0; i < T; i++)
	{
		char a[161];
		scanf("%d", &R);
		scanf("%s", a);

		for (j = 0; j < strlen(a); j++)
		{
			for (k = 0; k < R; k++)
			{
				printf("%c", a[j]);
			}
		}
		printf("\n");
	}

	return 0;
}