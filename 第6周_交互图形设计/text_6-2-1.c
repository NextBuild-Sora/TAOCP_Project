/*
	--第6周--
	--2 函数指针及其应用--
	--1 函数指针--
*/


#include <stdio.h>

void f(void)
{
	printf("in f()\n");
}

int main(void)
{
	int i = 0;
	int *p = &i;
	* p = 20;
	int a[] = {1,2};
	void (*pf)(void) = f;
	f();
	(*pf)(); 
	printf("%p\n", main);
	printf("%p\n", pf); 
	printf("%p\n", a); 
	
	return 0;
}


