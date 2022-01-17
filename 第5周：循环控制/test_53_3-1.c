
/******************************
 *
 *	第5周 循环控制
 *
 *	--3 循环应用 --
 *	--- 3.1 正序分解整数 ---
 *
 *******************************/


#include <stdio.h>

int main()
{
	int x;
	
//	scanf("%d", &x);
	x = 12345;
	int mask = 1;
	int t = x;
	while ( t>9 ) {
		t /= 10;
		mask *= 10;
	}
	printf("x=%d, mask=%d\n", x, mask);
	do{
		int d = x / mask;
		printf("%d", d);
		if( mask>9 ){
			printf(" ");
		}
		x %= mask;
		mask /= 10;
//		printf("x=%d, mask=%d, d=%d\n", x, mask, d);
	}while( mask>0 );
	
	printf("\n");
	
	return 0;
	
}


