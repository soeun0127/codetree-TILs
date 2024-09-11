#include <stdio.h>
#include <string.h>
int main() {
    // 여기에 코드를 작성해주세요.
    char str[101];
    fgets(str, 101, stdin);
    char alp;
    scanf(" %c", &alp);
    int len = strlen(str);
    int count = 0;
    for(int i=0; i<len; i++){
        if(str[i] == alp){
            count++;
        }
    }
    printf("%d", count);
    return 0;
}