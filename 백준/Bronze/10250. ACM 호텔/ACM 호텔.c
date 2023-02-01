#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
	int T;
	scanf("%d", &T);

	int i;
	int H;
	int W;
	int N;
	int cmd;
	int gh;
	for (i = 0; i < T; i++)
	{
		scanf("%d %d %d", &H, &W, &N);
		cmd = N % H;
		gh = N / H +1;
		if (cmd == 0)
		{
			cmd = H;
			gh = N / H;
		}


	    printf("%d%02d \n", cmd, gh);

	}

	return 0;
}