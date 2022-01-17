
/******************************
 *
 *	第5周 循环控制
 *
 *	--2 多重循环 --
 *	---1 嵌套的循环 ---
 *
 *******************************/


#include <stdio.h>

int main()
{
	int x;

////	例子1：100内的素数
//	x = 6;
//	for ( x=2; x<100; x++) 
//	{
//		int i;
//		int isPrime = 1;	// x是素数
//		for ( i=2; i<x; i++ ) {
//			if ( x%i == 0 ) {
//				isPrime = 0;
//				break;
//			}
//		}
//		if ( isPrime == 1 ) {
//			printf("%d ", x);
//		} 
//	}
//	printf("\n");
	
//	 例子2：前50个的素数
	x = 2;
	int cnt = 0;	//计数器
//	while ( cnt <50 ) 
	for ( x=2; cnt<50; x++)
	{
		int i;
		int isPrime = 1;	// x是素数
		for ( i=2; i<x; i++ ) {
			if ( x%i == 0 ) {
				isPrime = 0;
				break;
			}
		}
		if ( isPrime == 1 ) {
			printf("%d ", x);
			cnt ++;
		} 
//		x++;
	}
	printf("\n");
	
	
	return 0;
}
