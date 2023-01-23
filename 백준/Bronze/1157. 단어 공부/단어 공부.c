#include <stdio.h>
#include <string.h>

int main(void)
{
	char a[1000001];
	int count[26] = { 0, };
	int count2[26] = { 0, };
	scanf("%s", a);
	int count3=0;
	int i;
	int len = 0;
	int repo;
	int repo2;
	int max=0;


	len = strlen(a);
	for (i = 0; i < len; i++)
	{
		if (a[i] <= 96)
		{
			count[a[i] - 65] += 1;
		}
		else
		{
			count[a[i]- 97] += 1;
		}

	}

	for (i = 0; i < 26; i++)
	{
			if (count[i] > max)
			{
				max = count[i];
			}
	}

	for (i = 0; i < 26; i++)
	{
		if (max == count[i])
		{
			count2[i] = count2[i] + 1;
			repo2 = i;
		}
	}
	for (i = 0; i < 26; i++)
	{
		if (count2[i] != 0)
		{
			count3 = count3 + 1;
		}
	}

	if (count3 >= 2)
	{
		printf("?");
	}
	else
	{
		printf("%c", repo2 + 65);
	}
	
	return 0;
}