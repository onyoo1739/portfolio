#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int word=0, characters = 0, words = 0, lines = 1;
	bool line_flag = false;
	bool word_flag = false;

	printf("Enter text :")
	while ((word=getchar()) != '.')
	{
		if (!isspace(word))
			characters++;
		if (!isspace(word) && line_flag)
		{
			lines++;
			line_flag = true;
		}
		if (word == '\n')
			line_flag = false;
		if (isspace(word) && !word_flag)
		{
			words++;
			word_flag = true;
		}
		if (isspace(word))
			word_flag = false;
	/*	characters += 1;
		if (word == ' ')
		{
			words += 1;
			characters -= 1;
		}
		else if (word == '\n')
		{
			lines += 1;
			characters -= 1;
		}*/
	}
	printf("Characters = %d, Words = %d, Lines = %d", characters, words + 1, lines);
	return 0;
}