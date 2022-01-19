/*
	第1周：指针与字符串
	-2 指针运算-
	-1指针运算-
*/


#include <stdio.h>

int main(void)
{
	char ac[] = {0,1,2,3,4,5,6,7,8,9};
	char *p = ac;
	char *p1 = &ac[5];
	printf("p =%p\n", p);
	printf("p+1=%p\n", p+1);
	printf("*(p+1)=%d\n", *(p+1));
	printf("p1-p=%d\n", p1-p);
	
	int ai[] = {0,1,2,3,4,5,6,7,8,9};
	int *q = ai;
	int *q1 = &ai[6];
	printf("q =%p\n", q);
	printf("q+1=%p\n", q+1);
	printf("*(q+1)=%d\n", *(q+1));
	printf("q1-q=%d\n", q1-q);
	
	return 0;
}



