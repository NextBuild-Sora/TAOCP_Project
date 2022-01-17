
/******************************
 *
 *	第6周：数组与函数
 *
 *	--2 函数的定义与使用 --
 *	--- 1 初见函数 ---
 *
 *******************************/


#include <stdio.h>

// 求和函数
void sum(int begin, int end)	//函数头
{
//	函数体
	int i;
	int sum =0;
	for ( i=begin; i<=end; i++ ) {
		sum += 1;
	}
	printf("%d到%d的和是：%d\n", begin, end, sum);
}

int main()
{
	sum(1,10);
	sum(20,30);
	sum(35,45);

	return 0;
}


