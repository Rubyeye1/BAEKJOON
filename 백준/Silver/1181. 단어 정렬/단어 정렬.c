#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

typedef struct compaare {
	char moonja[51];
	int count;
}d;

int compare(const void* a, const void* b)
{
	d temp1 = *(d*)a;
	d temp2 = *(d*)b;
	if (temp1.count < temp2.count)
	{
		return -1;
	}
	else if (temp1.count > temp2.count)
	{
		return 1;
	}
	else if (temp1.count == temp2.count)
	{
		if (strcmp(temp1.moonja, temp2.moonja) == 0)
		{
			return 0;
		}
		else if (strcmp(temp1.moonja, temp2.moonja) > 0)
		{
			return 1;
		}
		else if (strcmp(temp1.moonja, temp2.moonja) < 0)
		{
			return -1;
		}
	}
}


d a[20000];

int main(void){

	int N;
	scanf("%d", &N);

	int i;
	int temp;
	for (i = 0; i < N; i++)
	{
		scanf("%s", &a[i].moonja);
		temp = strlen(a[i].moonja);
		a[i].count = temp;
	}

	qsort(a, N, sizeof(d), compare);

	for (i = 0; i < N; i++)
	{
		if (strcmp(a[i].moonja, a[i + 1].moonja) != 0)
		{
			printf("%s\n", a[i].moonja);
		}
	}

	return 0;
}