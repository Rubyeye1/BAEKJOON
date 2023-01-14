#include <stdio.h>

int main(void)
{
	int H = 0; 
	int M = 0; 
	int C = 0; 

	scanf("%d %d", &H, &M);
	scanf("%d", &C);

	int P = C / 60;
	int S = C % 60;

	if (C <= 59)
	{
		if (M + C >= 60)
		{
			if (H == 23)
			{
				H = 0;
			}
			else
			{
				H = H + 1;
			}
			M = M + C - 60;
			printf("%d %d", H, M);
		}
		else
		{
			M = M + C;
			printf("%d %d", H, M);
		}
	}

	if (C >= 60) 
	{
		if (H + P > 23 && M+S <60)
		{
			H = H + P - 24;
			M = M + S;
			printf("%d %d", H, M);
		}
		else if (H + P > 23 && M + S >= 60)
		{
			H = H + P - 24 + 1;
			M = M + S - 60;
			printf("%d %d", H, M);
		}
		else if (H + P <= 23 && M + S < 60)
		{
			H = H + P;
			M = M + S;
			printf("%d %d", H, M);
		}
		else if (H + P <= 23 && M + S >=60)
		{
			if (H + P == 23)
			{
				H = 0;
			}
			else 
			{
				H = H + P + 1;
			}
			M = M + S - 60;
			printf("%d %d", H, M);
		}
	}

	
	

	return 0;
}