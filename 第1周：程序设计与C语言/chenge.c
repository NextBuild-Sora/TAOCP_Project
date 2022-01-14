#include <stdio.h> 
// 第1周：程序设计与C语言
// 3 第一个程序
// 富文本：change.c
 
int main(){
	int price = 0;
	
	printf("请输入金额（元）：");
	scanf("%d", &price);
	
	int change = 100 - price;
	
	printf("找您 %d 元.\n", change);
	
	return 0;
	
}
