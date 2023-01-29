#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
	char a[10001];
	int count;
	int finalcount=0;

	scanf("%d", &count);
	int i,j,k; // 반복문 변수 k는 j+1부터 시작해서 계속 검사하는변수
	int len; // 문자열길이
	int tof=0; // true or false 이게 그룹단어면 1 아니면 0 
	for (i = 0; i < count; i++)
	{	
		scanf("%s", a);
		len = strlen(a);
		for (j = 0; j < len; j++)
		{
			if (len == 1)
			{
				tof = 1;
				break;
			}
			for (k = j + 1; k < len; k++) // j의 하나 뒤부터 계속 검사.
			{
				if (a[j] != a[k]) // 다르면 그룹단어
				{
					tof = 1;
				}
				else if (a[j] == a[k] && k-j != 1) // 같은 소문자가 나왔는데 만약 붙어있는게 아니면 그룹단어가 아니므로 tof는 0
				{
					tof = 0;
					break;
				}
				else if (a[j] == a[k] && k - j == 1) // 같은 소문자가 나왔는데 붙어있는거면 그룹단어
				{
					tof = 1;
					break;
				}
			}
			if (tof == 0)
			{
				break;
			}
		}
		if (tof == 1) // 최종적으로 tof가 1이면 그룹단어이므로 finalcount를 1씩 증가
		{
			finalcount = finalcount + 1;
		}

	}

	printf("%d", finalcount);
	
	return 0;
}