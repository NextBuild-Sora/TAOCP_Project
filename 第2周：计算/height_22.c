
#include <stdio.h>

int main(){
	printf("输入身高的英尺和英寸：");
	
	int foot;
	int inch;
	
	scanf("%d %d", &foot, &inch);
	
	printf("身高：%f\n",
		((foot + inch / 12.0) * 0.3048));
		
	return 0;
	
} 
