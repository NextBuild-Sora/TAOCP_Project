#include <stdio.h>

// 3 表达式
// --4 复合赋值和递增递减--


int main() {
	int a;
	a = 10;

	printf("a++= %d\n", a++);
	printf("a=%d\n", a);

	printf("++a= %d\n", ++a);
	printf("a= %d\n", a);

	return 0;
}