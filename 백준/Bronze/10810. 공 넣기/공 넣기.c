#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int n, m, i, j, k;
    scanf("%d %d", &n, &m);
    int arr[100] = { 0 };
    for (int x = 0; x < n; x++) {
        arr[x] = 0;
    }
    for (int x = 0; x < m; x++) {
        scanf("%d %d %d", &i, &j, &k);
        for (i; i < j+1; i++) {
            arr[i] = k;
        }
    }
    for (int i = 1; i < n+1; i++) {
        printf("%d ",arr[i]);
    }


    return 0;
}