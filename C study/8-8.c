#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

char get_choice(void);
char get_first_char(void);
int get_integer(void);
void count(void);

int main()
{
	int user_choice;
	
	while ((user_choice = get_choice()) != 'q')
	{
		switch (user_choice)
		{
		case 'a':
			printf("Avengers assemble!\n");
			break;
		case 'b':
			printf('\a');
			break;
		case 'c':
			printf("Enter an integer");
			count();
			break;
		default :
			printf("Error with %d.\n", user_choice);
			exit(1);
			break;
		}
	}
	
	return 0;
}

char get_choice(void)
{
	int user_input;

	printf("Enter the letter of you choice:\n");
	printf("a. avengers\tb. beep\n");
	printf("c. count\tq. quit\n");

	user_input = get_first_char();

	while ((user_input < 'a' || user_input>'c') && user_input != 'q')
	{
		printf("Please try againg.\n");
		user_input = get_first_char();
	}
	return user_input;
}
char get_first_char(void)
{
	int ch;
	ch = getchar();
	while (getchar() != '\n') continue;

	return ch;
}
int get_integer(void)
{
	int input;
	char c;
	while (scanf("%d", &input) != 1)
	{
		while ((c = getchar()) != '\n')
			putchar(c);
		printf(" is not an integer.\nPlease try again.");
	}
	return input;
}
void count(void)
{
	int a, num;
	printf("Enter an integer:");
	num = get_integer();
	for (a=1; a < num; a++)
		printf("%d\n", a);
	while (getchar() != '\n') continue;
}



