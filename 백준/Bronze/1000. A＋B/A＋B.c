#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int a=0, b=0;
	scanf("%d  %d", & a, &b);
	printf("%d ", a + b);
	return 0;
//범위 int 는 안됨 ->  long long %lld
}
