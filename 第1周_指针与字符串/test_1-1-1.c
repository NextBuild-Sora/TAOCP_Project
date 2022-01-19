/******************************
 *
 *	第1周：指针与字符串
 *
 *	-1 指针的使用 --
 *	--- 1 指针有什么用呢---
 *
 ******************************/


#include <stdio.h>

void swap(int *pa, int *pb);

int main(void)
{
	int a = 5;
	int b = 6;
	swap(&a, &b);
	printf("a=%d, b=%d\n", a,b);
	
	return 0;
}

void swap(int *pa, int *pb)
{
	int t = *pa;
	*pa = *pb;
	*pb = t;
}


