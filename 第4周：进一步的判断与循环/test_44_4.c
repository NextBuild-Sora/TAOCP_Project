
/******************************
 *	第4周
 *
 *	--4 循环的例子--
 *	--- 4 整数求逆---
 *
 *******************************/



#include <stdio.h>

int main()
{
	int x;
	
//	例子1
//	scanf("%d", &x);
	x = 700;
	int digit;
	int ret = 0;
	
	while ( x>0 ) {
		digit = x%10;
		printf("%d", digit);
		ret = ret*10 + digit;
		x /= 10;
	}

	
	//	例子2;
//	x = 12345;
//	int digit;
//	int ret = 0;
//	
//	while ( x>0 ) {
//		digit = x%10;
//		printf("%d\n", digit);
//		ret = ret*10 + digit;
//		printf("x=%d, digit=%d, ret=%d\n", x, digit, ret);
//		x /= 10;
//	}
//		printf("%d", ret);

	return 0;
	
}



