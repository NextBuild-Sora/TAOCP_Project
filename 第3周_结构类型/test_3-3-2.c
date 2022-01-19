/*******************************
 *	---第3周：结构类型---
 *	--3 联合--
 *	-2 联合-
 *
 *******************************/



#include <stdio.h>

typedef union {
	int i;
	char ch[sizeof(int)];
} CHI;

int main(int argc, char const *argv[])
{
	CHI chi;
	int i;
	chi.i = 1234;
	for ( i=0; i<sizeof(int); i++ ) {
		printf("%02hhX", chi.ch[i]);
	}
	printf("\n");
	
	return 0;
}



