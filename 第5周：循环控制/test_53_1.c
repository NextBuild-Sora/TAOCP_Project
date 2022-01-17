
/******************************
 *
 *	第5周 循环控制
 *
 *	--3 循环应用 --
 *	--- 1 前N项求和 ---
 *
 *******************************/


#include <stdio.h>

int main()
{
	int n;
	int i;
	double sum = 0.0;
	
	scanf("%d", &n);
	n = 100;
	for( i = 1; i<=n; i++ ){
		sum += 1.0/i;
	}
	
	printf("f(%d)=%f\n", n, sum);
	
	return 0;
	
}


