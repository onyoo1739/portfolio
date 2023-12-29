#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
int main() {
    int T;
    scanf("%d", &T);
    char c[1000];
    char ch='a';
    for (int i = 0; i < T; i++) {
        scanf("%s", c);
        printf("%c", c[0]);
        for (int j = 0,ch='a'; ch != '\0'; j++) {
            ch = c[j];
            if (ch == '\0')
                printf("%c", c[j - 1]);
        }
        printf("\n");
    }
}