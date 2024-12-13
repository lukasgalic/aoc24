#include <stdio.h>

int main(void)
{
    int arr1[1000];
    int arr2[1000];

    int total = 0;

    FILE *file = fopen("input1.txt", "r");

    int n = 0;
    for (int i = 0; i < sizeof(arr1) / sizeof(arr1[0]); i++)
    {
        fscanf(file, "%d %d", &arr1[i], &arr2[i]);
        n++;
    }

    for (int i = 0; i < n; i++)
    {
        int count = 0;
        for (int j = 0; j < n; j++)
        {
            if (arr1[i] == arr2[j])
            {
                count += 1;
            }
        }
        total += count * arr1[i];
    }
    printf("Total: %d ", total);

    return 0;
}