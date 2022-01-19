/*******************************
 *	-第五周：程序结构-
 *	-2 编译预处理和宏-
 *	-2 带宏定义-
 *
 *********************************/



#include <stdio.h>

#define cube(x) ((x)*(x)*(x))
#define RADTODEG1(x) (x * 57.29578)
#define RADTODEG2(x) (x) * 57.29578

int main(int argc, char const *argv[])
{
	printf("%d\n", cube(5));
	printf("%f\n", RADTODEG1(5+2));
	printf("%f\n", 180/RADTODEG2(1));
	
	return 0;
}



