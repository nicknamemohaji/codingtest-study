#include <stdio.h>

int main(void)
{
    int n;
    scanf("%d", &n);
    int arr[n];

    for (int i=0; i<n; i++)
    {
        int temp;
        scanf("%d", &temp);
        for (int j = 0; j < temp; j++)
            arr[i - j] = arr[i - j - 1];
        arr[i - temp] = i + 1;
    }    

    for (int i=0; i<n; i++)
        printf("%d ", arr[i]);
    printf("\n");
    return 0;
}