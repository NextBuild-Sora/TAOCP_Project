//第2周：计算 
//2 数据类型 

#include <stdio.h>

int main(){
	printf("输入身高的英尺和英寸：");
	
	double foot;
	double inch;
	
	scanf("%lf %lf", &foot, &inch);
	
	printf("身高：%f\n",
		((foot + inch / 12) * 0.3048));
		
	return 0;
	
} 
