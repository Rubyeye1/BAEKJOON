#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <math.h>


int main() {

    char a[1001];
    int T;
    scanf("%d", &T);

    int i;
    int temp;
    for (i = 0; i < T; i++)
    {
        scanf("%s", &a);
        temp = strlen(a);
        printf("%c%c\n", a[0], a[temp - 1]);
    }

    return 0;
}
