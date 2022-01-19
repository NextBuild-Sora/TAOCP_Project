/*
	7.2.3 位运算

 */


#include <stdio.h>

int main(int argc, char const *argv[])
{
	int number;
	scanf("%d", &number);
	number = 0xaaaaaaa; 
	unsigned mask = 1u<<31;
	for ( ; mask; mask >>=1 ) {
		printf("%d", number & mask?1:0);
	}
	printf("\n");
	
	return 0;
}



