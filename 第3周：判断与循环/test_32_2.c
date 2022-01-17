
/*
	第3周
	--2循环--
	---2 while循环---

*/


#include <stdio.h>

int main() {
	int x;
	int n = 0;

//	scanf("%d", &x);
	x = 352;

	while (x > 0) {
		printf("hr/n");
		n++;
		x /= 10;
		printf("x=%d, n=%d\n", x, n);	//打印循环进展
	}

	printf("%d\n", n);

	return 0;

}

