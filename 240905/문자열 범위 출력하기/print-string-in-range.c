#include <stdio.h>
#include <string.h>
int main() {
    // 여기에 코드를 작성해주세요.
    char str[101];
    fgets(str, 100, stdin);
    scanf("%s", str);
    int count = 2;
    while(count < 10){
        printf("%c", str[count]);
        count++;
    }
    return 0;
}