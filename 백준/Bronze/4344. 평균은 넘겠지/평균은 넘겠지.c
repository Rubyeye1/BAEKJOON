#include <stdio.h>
#include <string.h>
int main(void)
{
	int C;
	int i;
	int j;

	scanf("%d", &C);

	for (i = 0; i < C; i++)
	{
		int num[1000];
		int stnum;
		scanf("%d", &stnum);
		int repo ;
		int avrepo=0;
		int goodstudent=0;
		double avgoodst = 0;
		for (j = 0; j < stnum; j++)
		{
			scanf("%d", &repo);
			num[j] = repo;
		}
		for (j = 0; j < stnum; j++)
		{
			avrepo = avrepo + num[j];
		}

		avrepo = avrepo / stnum;

		for (j = 0; j < stnum; j++)
		{
			if (avrepo < num[j])
			{
				goodstudent = goodstudent + 1;
			}
		}

		avgoodst = (double)goodstudent / (double)stnum;
		avgoodst = avgoodst * 100;
		printf("%.3lf%%\n", avgoodst);

	}


	return 0;
}