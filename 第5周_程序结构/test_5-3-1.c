/*
	-第5周：程序结构-
	-3 大程序结构-
	-1 多个源代码文件-

*/


#include <stdio.h>

int max(int a, int b);

int main(void)
{
	int a= 5;
	int b=6;
	printf("%d\n", max(a,b));
	
	return 0;
	
}

int max(int a, int b)
{
	return a>b?a:b;
}


