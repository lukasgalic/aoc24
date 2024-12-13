#include <stdio.h>
#include <stdlib.h>

// Comparison function
int compare(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}

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

    qsort(arr1, n, sizeof(int), compare);
    qsort(arr2, n, sizeof(int), compare);

    for (int i = 0; i < n; i++)
    {
        total += abs(arr1[i] - arr2[i]);
    }

    printf("Total: %d ", total);
    return 0;
}