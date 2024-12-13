#include <stdio.h>

typedef struct Neighbor
{
    int x;
    int y;
} Neighbor;

int main(void)
{

    char c;
    int rows = 0;
    int cols = 0;
    FILE *file = fopen("input.txt", "r");

    Neighbor neighbors[2] = {
        {-1, -1},
        {-1, 1}};

    int first_row_done = 0;
    while ((c = fgetc(file)) != EOF)
    {
        if (!first_row_done)
        {
            cols++;
        }
        if (c == '\n')
        {
            rows++;
            first_row_done = 1;
        }
    }
    rewind(file);

    char matrix[rows][cols];

    int i = 0;
    int j = 0;
    while ((c = fgetc(file)) != EOF)
    {
        matrix[i][j] = (char)c;
        j++;
        if (c == '\n')
        {
            i++;
            j = 0;
        }
    }

    int nr;
    int nc;
    char ltr;
    int total_xmas = 0;
    for (int r = 0; r < rows; r++)
    {
        for (int c = 0; c < cols; c++)
        {
            if (matrix[r][c] == 'A')
            {
                nr = r + neighbors[0].x;
                nc = c + neighbors[0].y;
                if (0 <= nr < rows && 0 <= nc < cols && ((ltr = matrix[nr][nc]) == 'M' || (ltr = matrix[nr][nc]) == 'S'))
                {
                    nr = r - neighbors[0].x;
                    nc = c - neighbors[0].y;
                    if (ltr == 'M')
                    {
                        if (0 <= nr < rows && 0 <= nc < cols && matrix[nr][nc] == 'S')
                        {
                            goto next_diagonal;
                        }
                    }
                    if (ltr == 'S')
                    {
                        if (0 <= nr < rows && 0 <= nc < cols && matrix[nr][nc] == 'M')
                        {
                            goto next_diagonal;
                        }
                    }
                    continue;
                }
                else
                {
                    continue;
                }
            next_diagonal:
                nr = r + neighbors[1].x;
                nc = c + neighbors[1].y;
                if (0 <= nr < rows && 0 <= nc < cols && ((ltr = matrix[nr][nc]) == 'M' || (ltr = matrix[nr][nc]) == 'S'))
                {
                    nr = r - neighbors[1].x;
                    nc = c - neighbors[1].y;
                    if (ltr == 'M')
                    {
                        if (0 <= nr < rows && 0 <= nc < cols && matrix[nr][nc] == 'S')
                        {
                            total_xmas++;
                        }
                    }
                    if (ltr == 'S')
                    {
                        if (0 <= nr < rows && 0 <= nc < cols && matrix[nr][nc] == 'M')
                        {
                            total_xmas++;
                        }
                    }
                    continue;
                }
                else
                {
                    continue;
                }
            }
        }
    }
    printf("Total: %d\n", total_xmas);
    return 0;
}