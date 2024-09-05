#include <stdio.h>
#include <string.h>
int main() {
    // 여기에 코드를 작성해주세요.
    char str1[21];
    char str2[21];
    char str3[21];

    scanf("%s", str1);
    scanf("%s", str2);
    scanf("%s", str3);

    int len1 = strlen(str1);
    int len2 = strlen(str2);
    int len3 = strlen(str3);

    if(len1 > len2){
        if(len2 > len3){
            printf("%d", len1 - len3);
        }
        else if(len1 > len3){
            printf("%d", len1 - len2);
        }
        else{
            printf("%d", len3 - len2);
        }
    }
    else{
        if(len3 > len2){
            printf("%d", len3 - len1);
        }
        else if(len1 > len3){
            printf("%d", len2 - len3);
        }
        else{
            printf("%d", len2 - len1);
        }
    }
    return 0;
}