#include <stdio.h>
#include <string.h>

int temp;
int recursion(const char* s, int l, int r) {
    temp++;
    if (l >= r) return 1;
    else if (s[l] != s[r]) return 0;
    else return recursion(s, l + 1, r - 1);
}

int isPalindrome(const char* s) {
    return recursion(s, 0, strlen(s) - 1);
}


int main() {
    int T;
    scanf("%d", &T);
    
    int i;
    for (i = 0; i < T; i++)
    {
        char a[1001];
        temp = 0;
        scanf("%s", &a);
        int temp2 = isPalindrome(a);
        printf("%d %d\n", temp2, temp);
    }

}
