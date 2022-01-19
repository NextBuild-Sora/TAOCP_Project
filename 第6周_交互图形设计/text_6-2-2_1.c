/*
	--第6周--
	--2 函数指针及其应用--
	--2 函数指针的使用--
*/


#include <stdio.h>

int plus(int a, int b)
{
	return a+b;
}

int minus(int a, int b)
{
	return a-b;
}

void cal(int (*f)(int, int))
{
	printf("%d", (*f)(2,3));
}

int main(void)
{
	cal(plus);
	cal(minus);
	
	return 0;
}


