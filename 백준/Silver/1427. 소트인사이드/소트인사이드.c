#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int compare(const void* a, const void* b)
{
	int temp1 = *(int*)a;
	int temp2 = *(int*)b;
	if (temp1 < temp2)
	{
		return 1;
	}
	else if (temp1 > temp2)
	{
		return -1;
	}
	else
	{
		return 0;
	}
}




int main(void){

	char repo[11];
	int irepo[11] = { 0, };
	scanf("%s", &repo);
	int length = strlen(repo);
	int temp = 0;
	int i;
	for (i = 0; i < length; i++)
	{
		temp = repo[i] - '0';
		irepo[i] = temp; 
	}

	qsort(irepo, length, sizeof(int), compare);


	for (i = 0; i < length; i++)
	{
		printf("%d", irepo[i]);
	}

	return 0;
}