#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int money, target, annual, cnt;
	float present;
	cnt = 0;
	printf("Input seed money : ");
	scanf("%d", & money);
	printf("Input target money :");
	scanf("%d", &target);
	printf("Input annual interest(%%): ");
	scanf("%d", &annual);
	present = money;
	while (present < target)
	{
		present = present + (present * annual / 100);
		printf("%lf\n", present);
		cnt = cnt + 1;
	}

	printf("It takes %d years", cnt);
	return 0; 




}