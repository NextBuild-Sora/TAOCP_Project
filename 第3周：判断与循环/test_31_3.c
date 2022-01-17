#include <stdio.h>

/*
	第3周：判断与循环
	--1判断--
	---3 找零计算器---

*/


int main() {
	//初始化
	int price = 0;
	int bill = 0;
	//读入
	printf("请输入金额：");
	scanf("%d", &price);
	printf("请输入票面：");
	scanf("%d", &bill);
	//计算
	printf("应该找您：%d\n", bill - price);

}