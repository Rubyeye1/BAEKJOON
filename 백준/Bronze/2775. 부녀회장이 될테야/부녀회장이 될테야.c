#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void)
{
	int arr[15][14] = { 0, }; // 0~14 1~14

	int i;
	int j;
	for (i = 0; i < 14; i++)
	{
		arr[0][i] = i+1;
	}

	for (i = 0; i < 15; i++)
	{
		arr[i][0] = 1;
	}


	for (i = 1; i <= 14; i++)
	{
		for (j = 1; j < 14; j++)
		{
			arr[i][j] = arr[i - 1][j] + arr[i][j - 1];
		}
	}

	int T;
	scanf("%d", &T);

	int k, n;
	for (i = 0; i < T; i++)
	{
		scanf("%d\n", &k);
		scanf("%d", &n);

		printf("%d\n", arr[k][n-1]);
	}

	return 0;
}