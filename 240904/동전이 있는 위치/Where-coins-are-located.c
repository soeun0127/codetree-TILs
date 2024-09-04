#include <stdio.h>

int main() {
    int n = 0, m = 0;
    scanf("%d %d", &n, &m);
    int arr[81][81] = {0,};

    for(int i=0; i<m; i++){
        int r = 0, c = 0;
        scanf("%d %d", &r, &c);
        arr[r-1][c-1] = 1;
    }
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
    return 0;
}