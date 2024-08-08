#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int arr[10][10] = {0};
    int count = 1;
    for(int j = n-1; j>=0; j--){
        if((n-1) % 2 == 0){
            if(j % 2 == 0){
                for(int i=n-1; i>=0; i--){
                    arr[i][j] = count;
                    count++;
                }
            }
            else{
                for(int i=0; i<n; i++){
                    arr[i][j] = count;
                    count++;
                }
            }
        }
        else{
            if(j % 2 != 0){
                for(int i=n-1; i>=0; i--){
                    arr[i][j] = count;
                    count++;
                }
            }
            else{
                for(int i=0; i<n; i++){
                    arr[i][j] = count;
                    count++;
                }
            }
        }
    }

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
    return 0;
}