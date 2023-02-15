#include <stdio.h>
void draw(int n);

int main()
{
	int i = 5;
	char c = '#';
	float f = 7.1f;

	draw(i);
	draw(c);
	draw(f);

	return 0;
}
void draw(int n)
{
	while (n-- > 0)
		printf("*");
	printf("\n");


}
