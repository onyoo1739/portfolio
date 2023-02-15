#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <limits.h>
//#include <stdlib.h>
int main()
{

	unsigned int i_max = INT_MAX ;
	unsigned int i_min = INT_MIN;

	unsigned int u_max = UINT_MAX+1;
	unsigned int u_min = 0;

	char buffer[33];
	_itoa(u_max, buffer, 2);

	/*printf("max of unit = %u\n", u_max);
	printf("min of int = %d\n", i_min);
	printf("max of unit = %u\n", u_max);
	printf("min of unit = %d\n", u_min);*/
	printf("decimal: %u\n", u_max);
	printf("binary: %s\n", buffer);

	return 0;
}