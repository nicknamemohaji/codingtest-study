#include <stdio.h>

int main(void)
{
    int arr[9] = {0};
    for (int i=0; i<9; i++)
        scanf("%d", &arr[i]);

    // 정렬    
    for (int i=0; i<9; i++)
    {
        for (int j=0; j<9; j++)
        {
            if (arr[i] < arr[j])
            {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }

    // 합을 구한다
    int sum = 0;
    for (int i=0; i<9; i++)
        sum += arr[i];

    // 9C2를 시도...
    for (int i=0; i<9; i++)
    {
        for (int j=i+1; j<9; j++)
        {
            // 해를 찾았으면 출력하고 종료
            if (sum - (arr[i] + arr[j]) == 100)
            {
                for (int k=0; k<9; k++)
                {
                    if (k == i || k == j)
                        continue;
                    printf("%d\n", arr[k]);
                }
                return 0;
            }
        }
    }
}