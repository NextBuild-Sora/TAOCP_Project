
/******************************
 *
 *	第6周：数组与函数
 *
 *	--1 数组 --
 *	--- 3 用数组做散列计算 ---
 * 		数组例子：统计计算
 *******************************/


#include <stdio.h>

int main()
{
	const int number = 10;		//数组的大小
	int x;
	int count[number];		//定义数组
	int i;
	
	for ( i=0; i<number; i++ ){		//初始化数组
		count[i] = 0;
	}
	scanf("%d", &x);
	while( x!= -1) {
		if ( x>=0 && x<=9 ) {
			count[x] ++;		//数组参与运算
		}
		scanf("%d", &x);
	}
	for ( i=0; i<number; i++) {		//遍历数组输出
		printf("%d:%d\n", i, count[i]);
	}
	return 0;
	
}


