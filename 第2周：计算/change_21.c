
/*

	第2周：计算
	1 变量
	--变量定义--
	 
*/


#include <stdio.h>

int main()
{
	int price = 0;
	printf("输入金额（元）");
	scanf("%d", &price);
	
	int change = 100 - price;
	
	printf("找您 %d 元"), change; 

	return 0;
}

