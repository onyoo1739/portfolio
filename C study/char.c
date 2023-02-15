
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	char c = 'A';
	char d = 65;
	char a = '\a';
	printf("%c %hhd\n", c, c);
	printf("%c %hhd\n", d, d);
	printf("%c \n", c + 1);
	printf("%c", a);
	printf("\07");
	printf("\x23");
	float salary;
	printf("$______\b\b\b\b\b\b");
	scanf("%f",  &salary);
	printf(" \\ \'HA+\' \"hello\" \?\n");
	return 0;

}
