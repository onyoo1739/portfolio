#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h> //strlen()
#include <stdbool.h>

#define NAME  "Jeong_Mo Hong"
#define ADRESS  "Seoul, Korea"
#define WIDTH 25

char print_chars(char c, int num,bool endl);
void print_centered_str(char str[]);
int main()
{
	print_chars('*', WIDTH,true);
	print_centered_str(NAME);
	print_centered_str(ADRESS);
	print_chars('*', WIDTH,false);

	return 0;

}
void print_centered_str(char str[])
{
	int n_blank = 0;

	n_blank = (WIDTH - strlen(str)) / 2;
	print_chars(' ', n_blank,false);
	printf("%s\n", str);
}
char print_chars(char c, int num, bool endl)
{
	for (int i = 0; i < num; i++)
		printf("%c", c);

	if (endl == true)
		printf("\n");
}