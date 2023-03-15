#include <stdio.h>
#include <limits.h>
#include <math.h>
#include <string.h>



int main(void)
{
	int T;
	scanf("%d", &T);
	int i;
	int temp=0;
	int zegop = 0;
	int repo = 0;
	for (i = 0; i < T; i++)
	{
		scanf("%d", &temp);
		zegop = temp * temp;
		if (temp < 10)
		{
			repo = zegop % 10;
			if (repo == temp)
			{
				printf("YES\n");
			}
			else
			{
				printf("NO\n");
			}
		}
		else if (temp >= 10 && temp < 100)
		{
			repo = zegop % 100;
			if (repo == temp)
			{
				printf("YES\n");
			}
			else
			{
				printf("NO\n");
			}
		}
		else if (temp >= 100 && temp < 1000)
		{
			repo = zegop % 1000;
			if (repo == temp)
			{
				printf("YES\n");
			}
			else
			{
				printf("NO\n");
			}
		}
		else
		{
			printf("NO\n");
		}
	
	}

	return 0;
}	