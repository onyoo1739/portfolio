#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

//int main()
//{
//	char fruit_name[40];
//
//	printf("What is your farovate fruit?\n");
//	scanf("%s", fruit_name);
//	printf("You like %s!\n", fruit_name);
//
//	return 0;
//	//배열이 되는 순간 &이 없어짐 배열[ ] ->&x
//}


int main()
{
	int int_arr[30];
	int *int_ptr = NULL;
	int_ptr = (int*)malloc(sizeof(int) * 30);

	printf("Size of array = %zu bytes\n", sizeof(int_arr));
	printf("Size of pointer = %zu byters\n", sizeof(int_ptr));
	return 0;


}