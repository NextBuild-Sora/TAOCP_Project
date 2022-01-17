
/******************************
 *
 *	第6周：数组与函数
 *
 *	--3 函数的参数和变量 --
 *	--- 1 函数原型 ---
 *
 *******************************/

 
#include <stdio.h>

void sum(int begin, int end);	//声明；函数原型
//void sum(int , int );	//可以不写参数名。
int main()
{
	sum(1,10);
	sum(20,30);
	sum(35,45);
	
	return 0;
}

void sum(int begin, int end)	//定义
{
	
	int i;
	int sum =0;
	for ( i=begin; i<=end; i++ ) {
		sum += 1;
	}
	printf("%d到%d的和是：%d\n", begin, end, sum);
}

