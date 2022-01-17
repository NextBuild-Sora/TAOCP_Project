

/******************************
 *
 *	第5周 循环控制
 *
 *	--1 循环控制 --
 *	--- ---
 *
 *******************************/



#include <stdio.h>

int main()
{
	int x;
	
//	方法1
//	scanf("%d", &x);
//	x = 13;
//	int i;
//	int isPrime = 1;	// x是素数
//	for ( i=2; i<x; i++ ) {
//		if ( x%i == 0 ) {
//			isPrime = 0;
////			break;
//			continue;
//		}
////		printf("%d\n", i);
//	}
//	if ( isPrime == 1 ) {
//		printf("是素数\n");
//	} else {
//		printf("不是素数\n");
//	}
	
//	方法2
	scanf("%d", &x);
	int i;
	for ( i=2; i<x; i++ ) {
		if ( x%i == 0 ) { 
			break;
		}
	}
	if ( i<x ) {
		printf("不是素数\n");
	} else {
		printf("是素数\n");
	}
	
	
	return 0;
	
}



