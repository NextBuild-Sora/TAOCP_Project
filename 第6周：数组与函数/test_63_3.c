/******************************
 *
 *	第6周：数组与函数
 *
 *	--3 函数的参数和变量 --
 *	--- 3 本地变量 ---
 * 
 *******************************/



#include <stdio.h>

void swap(int a, int b);

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

void swap(int x, int y)
{
	int t = x;
	x = y;
	y = t;
}


