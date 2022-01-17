/******************************
 *
 *	第6周：数组与函数
 *
 *	--3 函数的参数和变量 --
 *	--- 2.1 参数传递 ---
 * 
 *******************************/



#include <stdio.h>

void swap(int a, int b);

int main()
{
	int a = 5;
	int b = 6;
	
	swap(a, b);		//传值
	
	printf("a=%d b=%d\n", a, b);
	
	return 0;
	
}

void swap(int x, int y)
{
	int t = x;
	x = y;
	y = t;
}


