/*
	第4周
	
	--1 逻辑类型和运算--
	---1_3 条件运算和逗号运算 ---
	
*/
	
	
	
#include <stdio.h>


int main()
{
	//条件运算
	int count;
	count = (count>20) ? count-10 : count+10; 
	
	//逗号运算
	int i;
	i = (3+4, 5+6);
	printf("%d\n", i);
	
//	for(i=0,j=10; i<j; i++,j--)		//在for中使用
	
	return 0;
	
}


