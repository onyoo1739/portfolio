#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int num=0, sum=0 ;
	int status;		
	status = scanf("%d", &num); //(변수의 갯수가 status에 저장됨)

	while (status ==1)
	{
		sum += num;
		printf("Enter an integer (q to quit) : " );
		status = scanf("%d", &num);

	}

	printf("Sum = %d\n", sum);

	return 0;

}