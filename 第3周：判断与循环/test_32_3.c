
/*
	第3周
	--2循环--
	---3 do-while循环---

*/


#include <stdio.h>

int main() {

	int x;
	scanf("%d", &x);
	int n = 0;

	do {
		x /= 10;
		n ++;
	} while (x > 0);
	printf("%d\n", n);

	return 0;

}

