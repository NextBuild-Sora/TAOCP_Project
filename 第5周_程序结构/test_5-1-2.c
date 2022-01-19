/*******************************
*	-第五周：程序结构-
*	-1 全局变量-
*	-2 本地变量-
*
*********************************/


#include <stdio.h>

int f(void);

int gAll = 12;

int main(int argc, char const *argv[])
{
	f();
 
	return 0;
}

int f(void)
{
	int k = 0;
	static int all = 1;
	printf("&gAll=%p\n", &gAll);
	printf("&all =%p\n", &all);
	printf("&k   =%p\n", &k);
	printf("in %s all=%d\n", __func__, all);
	all += 2;
	printf("agn in %s all=%d\n", __func__, all);
	
	return gAll;
}



