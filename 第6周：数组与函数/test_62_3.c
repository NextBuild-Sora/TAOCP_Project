
/******************************
 *
 *	第6周：数组与函数
 *
 *	--2 函数的定义与使用 --
 *	--- 3 从函数中返回 ---
 * 
 *******************************/


#include <stdio.h>

int max(int a, int b)
{
	int ret;
	if ( a>b ) {
		ret = a;
//		return a;
	} else {
		ret = b;
//		return b;	
	}
	
	return ret;		//单一出口
}

int main()
{
	int a,b,c;
	a = 5;
	b = 6;
	c = max(10,12);
	c = max(a,b);
	c = max(c, 23);
	printf("%d\n", max(a,b));
	
	return 0;
}



