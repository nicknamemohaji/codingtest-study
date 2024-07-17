#include <stdio.h>
#include <stdlib.h>

# define WIDTH 100

int compare(const void* n1, const void* n2)
{
	return *(int*)n1 > *(int*)n2 ? 1 : -1;
}

int main(void)
{
	for (int run = 1; run <= 10; run++)
	{
		int dumps;
		scanf("%d", &dumps);
		int datas[WIDTH];
		for (int i = 0; i < WIDTH; i++)
			scanf("%d", &datas[i]);
		for (int i = 0; i < dumps; i++)
		{
			qsort(datas, sizeof(datas) / sizeof(int), sizeof(int), compare);
			datas[0] += 1;
			datas[WIDTH - 1] -= 1;
		}
		qsort(datas, sizeof(datas) / sizeof(int), sizeof(int), compare);

		printf("#%d %d\n", run, datas[WIDTH - 1] - datas[0]);
	}
}