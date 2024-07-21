#include <stdio.h>
#include <stdint.h>

# define r 31
# define M 1234567891

int main(void)
{
	int L;
	scanf("%d", &L);

	char str[L + 1];
	scanf("%s", str);

	uint64_t hash = 0;
	for (int i = L - 1; i >= 0; i--)
		hash = ((hash * r) % M) + (str[i] - 'a' + 1);

	printf("%lu\n", hash % M);
}

// def hash(s: str) -> int:
// 	ret = 0
// 	for i in range(len(s) - 1, -1, -1):
// 		ret += (ord(s[i]) - ord('a') + 1) * r ** i
// 	return ret % 1234567891