#include <stdio.h>
#include <stdlib.h>

void mergingSortedArrays(int *a, int m, int *b, int n, int *c)
{
    int na, nb, nc;
    na = nb = nc = 0;
    while ((na < m) && (nb < n))
    {
        if (a[na] < b[nb]) 
        {
            c[nc] = a[na++];
        } else 
        {
            c[nc] = b[nb++];
        }
        nc++;
    }

    
    if (na == m)                    // list `a` is exhausted
    {
        while (nb < n) 
        {
            c[nc++] = b[nb++];
        }
    } else if (nb == n)             // list `b` is exhausted
    {
        while (na < m)
        {
            c[nc++] = a[na++];
        }
    }

}

int main() {
    int a[] = {1, 4, 12, 34, 123};
    int b[] = {-1, 34, 91, 121};
    int c[9];
    mergingSortedArrays(a, 5, b, 4, c);
    for (int i=0; i<9; i++) {
        printf("%d\n", *(c+i));
    }
    return 0;
}