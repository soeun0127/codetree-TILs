#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.
    int n=0, m=0;
    scanf("%d %d", &n, &m);
    int arr[10][10] = {0,};
    for(int i=0; i<m; i++){
        int r=9, c=0;
        scanf("%d %d", &r, &c);
        arr[r][c] = r*c;
    }
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
    return 0;
}