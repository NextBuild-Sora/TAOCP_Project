/*******************************
 *	-第五周：程序结构-
 *	-2 编译预处理和宏-
 *	-1 宏定义-
 *
 *********************************/



#include <stdio.h>

//const double PI = 3.14159;
#define PI 3.14159
#define FORMAT "%f\n"
#define PI2 2*PI // pi * 2
#define PRI printf("%f", PI); \
			printf("%f\n", PI2)

int main(int argc, char cosnt *argv[])  
{
//	printf(FORMAT, PI2*3.0); 
	PRI;  
	
	printf("%s:%d\n", __FILE__, __LINE__);
	printf("%s,%s\n", __DATE__, __TIME__); 
	
	return 0;
}


