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

    Neighbor neighbors[8] = {};
    int index = 0;
    for (int i = -1; i < 2; i++)
    {
        for (int j = -1; j < 2; j++)
        {
            if (i == 0 && j == 0)
            {
                continue;
            }
            Neighbor n = {i, j};
            neighbors[index] = n;
            index++;
        }
    }

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
    int total_xmas = 0;

    for (int r = 0; r < rows; r++)
    {
        for (int c = 0; c < cols; c++)
        {
            if (matrix[r][c] == 'X')
            {
                for (int n = 0; n < sizeof(neighbors) / sizeof(neighbors[0]); n++)
                {
                    nr = r + neighbors[n].x;
                    nc = c + neighbors[n].y;
                    if (0 <= nr < rows && 0 <= nc < cols && matrix[nr][nc] == 'M')
                    {
                        nr = nr + neighbors[n].x;
                        nc = nc + neighbors[n].y;

                        if (0 <= nr < rows && 0 <= nc < cols && matrix[nr][nc] == 'A')
                        {
                            nr = nr + neighbors[n].x;
                            nc = nc + neighbors[n].y;

                            if (0 <= nr < rows && 0 <= nc < cols && matrix[nr][nc] == 'S')
                            {
                                total_xmas++;
                                continue;
                            }
                            else
                            {
                                continue;
                            }
                        }
                        else
                        {
                            continue;
                        }
                    }
                }
            }
        }
    }

    printf("Total: %d\n", total_xmas);
    return 0;
}