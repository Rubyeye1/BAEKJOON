#include <stdio.h>
#include <string.h>
int main(void)
{
	int N;
	int i;
	int j;
	int a ;
	int b ;

	scanf("%d", &N);

	for (i = 0; i < N; i++)
	{
		char str[80];
		scanf("%s", &str);	
		a = 0;		
		b = 0;
		for (j = 0; j < strlen(str); j++)
		{
			if (str[j] == 'O')
			{
				a = a + 1;
				b = b+ a;
			}
			else
			{
				a = 0;
			}
		}
		printf("%d\n", b);
	}



	return 0;
}