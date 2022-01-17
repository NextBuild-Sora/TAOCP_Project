/******************************
 *
 *	第6周：数组与函数
 *
 *	--3 函数的参数和变量 --
 *	--- 4 杂事 ---
 * 		函数庶事  
 *******************************/



#include <stdio.h>

//void swap(int a, int b);
void swap();

int main()
{
	int a = 5;
	int b = 6;
	
	swap(a, b);		//传值
	
	{
		int a = 0;
//		int a = 10;
		printf("a=%d\n", a);
	}
	
	printf("a=%d b=%d\n", a, b);
	
	return 0;
	
}

void swap(double x, double y)
{
	int t = x;
	printf("in swap, x=%f, y=%f\n", x, y);
	x = y;
	y = t;
}


