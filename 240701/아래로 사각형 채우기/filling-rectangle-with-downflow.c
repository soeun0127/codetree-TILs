#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.
    int n = 0;
    scanf("%d", &n);
    int arr[10][10] = {0};

    for(int i = 0; i<n; i++){
        int count = i+1;
        for(int j=0; j<n; j++){
            printf("%d ", count);
            count += n;
        }
        printf("\n");
    }
    return 0;
}