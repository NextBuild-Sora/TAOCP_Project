
/******************************
 *
 *	第5周 循环控制
 *
 *	--3 循环应用 --
 *	--- 1.1 前N项求：减、加（计算） ---
 *
 *******************************/


#include <stdio.h>

int main()
{
	int n;
	int i;
	double sum = 0.0;
//	int sign = 1;
	int sign = 1.0;
	
//	scanf("%d", &n);
	n = 100;
	for( i = 1; i<=n; i++ ){
//		sum += sign*1.0/i;
		sum += sign/i;
		sign = -sign;
	}
	
	printf("f(%d)=%f\n", n, sum);
	
	return 0;
	
}


