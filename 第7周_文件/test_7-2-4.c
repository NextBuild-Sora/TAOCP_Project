
/*	7-2-4 位移*/


#include <stdio.h>

void prtBin(unsigned int number);

struct U0 {
	unsigned int leading : 3;
	unsigned int FLAG1: 1;
	unsigned int FLAG2: 1;
	int trailing : 27;
};

int main(int argc, char const *argv[])
{
	struct U0 uu;
	uu.leading = 2;
	uu.FLAG1 = 0;
	uu.FLAG2 = 1;
	uu.trailing = 0;
	printf("sizeof(uu)=%lu\n", sizeof(uu));
	prtBin(*(int*)&uu);
	
	return 0;
}


void prtBin(unsigned int number)
{
	unsigned mask = 1u<<31;
	for( ; mask; mask >>=1 ) {
		printf("%d", number & mask?1:0);
	}
	printf("\n");
}


