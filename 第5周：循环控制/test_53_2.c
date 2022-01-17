
/******************************
 *
 *	第5周 循环控制
 *
 *	--3 循环应用 --
 *	--- 2 最大公约数，使用辗转相除法计算 ---
 *
	 a	b	t
	 12	18	12
	 18	12	6
	 12	6	0
	 6	0
	 
 *******************************/


#include <stdio.h>

int main()
{
	int a,b;
	int t;
	scanf("%d %d", &a, &b);
	a=12; b=18;
	while( b!=0 ) {
		t = a%b;
		a=b;
		b=t;
		printf("a=%d, b=%d, t=%d\n", a, b, t);
	}
	printf("gcd=%d\n", a);
	
	return 0;
}



