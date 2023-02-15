#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	const int pw=337;
	int en=0.0;
	/*printf("Enter secret code : ");
	scanf("%d\n", &en);
	while (en != pw)
	{
		printf("Enter secret code : ");
		scanf("%d\n", &en);
	}*/

	do
	{
		printf("Enter secret code :");
		scanf("%d", &en);
	}
	while (en != pw);


	printf("Good!");
	return 0;
}