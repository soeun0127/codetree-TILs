#include <stdio.h>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    int arr[100][100];
    int count = 0;
    for(int i=0; i<m; i++){
        if(i != 0){
            count = count + n - 1;
        }
        for(int j=0; j<n; j++){
            if(i % 2 == 0){
                arr[j][i] = count;
                count++;
            }
            else{
                arr[j][i] = count;
                count--;
            }
        }
    }

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
    return 0;
}