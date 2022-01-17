
/******************************
 *
 *	第8周：指针与字符串
 *
 *	--1  指针 --
 *	--- 2 指针 ---
 * 
 ******************************/


#include <stdio.h>

void f(int *p);
void g(int k);

int main(void)
{
	
	int i =6;
	printf("&i=%p\n", &i);
	f(&i);
	g(i);
	
	return 0;
	
}

void f(int *p)
{
	printf(" p=%p\n", p);
	printf("*p=%d\n", *p);
	*p = 26;
}

void g(int k)
{
	printf("k=%d\n", k);
}


