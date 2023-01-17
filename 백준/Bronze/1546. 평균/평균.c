#include <stdio.h>

int main(void)
{
	int N;
	int i;
	float score;
	float num[1000];
	float max;
	float a=0;
	
	scanf("%d", &N);

	for (i = 0; i < N; i++)
	{
		scanf("%d", &score);
		num[i] = score;
	}

	max = num[0];

	for (i = 1; i < N; i++)
	{
		if (num[i] > max)
		{
			max = num[i];
	    }
	}

	for (i = 0; i < N; i++)
	{
		num[i] = (num[i] / max) * 100;
	}

	for (i = 0; i < N; i++)
	{
		a = a + num[i];
	}

	a = a / N;


	printf("%f", a);


	return 0;
}