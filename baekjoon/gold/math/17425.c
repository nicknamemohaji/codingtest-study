#include <stdio.h>

#define MAX 1000000

int main(void)
{
    long long int cache[MAX + 1] = {0};
    for (int i=1; i<=MAX; i++)
    {
        for (int j=1; i*j<=MAX; j++)
            cache[i*j] += i;
        cache[i] += cache[i-1];
    }

    int n;
    scanf("%d", &n);

    for (int i=0; i<n; i++)
    {
        int testcase;
        scanf("%d", &testcase);
        printf("%lld\n", cache[testcase]);
    }
}