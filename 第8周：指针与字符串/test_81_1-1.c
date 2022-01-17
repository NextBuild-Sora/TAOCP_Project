
/******************************
 *
 *	第8周：指针与字符串
 *
 *	--1  --
 *	--- 1.1 取地址运算 ---
 *
 *******************************/


#include <stdio.h>

int main()
{
	int i = 0;
	int p;
	p = (int)&i;
	printf("0x%x\n", p);
//	printf("0x%x\n", &i);
	printf("%p\n", &i);
	printf("%lu\n", sizeof(int));
	printf("%lu\n", sizeof(&i));
	

	return 0;

}


