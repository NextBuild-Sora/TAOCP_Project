/*******************************
*	-第五周：程序结构-
*	-1 全局变量-
*	-1 全局变量-
*
*********************************/


#include <stdio.h>

int f(void);

int gAll = 12;

//const int gAll = 12;
//int g2 = gAll;

int main(int argc, char const *argv[])
{
	printf("in %s gAll=%d\n", __func__, gAll);
	f();
	printf("agn in %s gAll=%d\n", __func__, gAll);
	return 0;
}

int f(void)
{
	int gAll = 1; 
	{
		int gAll = 2; 
		printf("in %s gAll=%d\n", __func__, gAll);
		gAll += 2;
		printf("agn in %s gAll=%d\n", __func__, gAll);
	}
	return gAll;
}



