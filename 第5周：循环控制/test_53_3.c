
/******************************
 *
 *	第5周 循环控制
 *
 *	--3 循环应用 --
 *	--- 3 正序分解整数 ---
 *
 *******************************/


#include <stdio.h>

int main()
{
	int x;
	
	scanf("%d", &x);
	x = 12345;
	int t=0;
	do {
		int d = x%10;
		t = t*10+d;
		x /=10;
	} while ( x>0 );
	printf("s=%d, t=%d\n", x, t);
	x = t;
	do {
		int d = x%10;
		printf("%d", d);
		if( x>9){
			printf(" ");
		}
		x /= 10;
	} while ( x>0 );
	printf("\n");
	
	return 0;
	
}


