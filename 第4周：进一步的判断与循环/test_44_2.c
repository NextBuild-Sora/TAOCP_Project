
/******************************
 *	第4周
 *
 *	--4 循环的例子--
 *	--- 2 算平均数---
 *
 *******************************/


#include <stdio.h>

int main()
{
	int number;
	int sum = 0;
	int count = 0;
	
//	第一种方法
//	do { 
//		scanf("%d", &number);
//		if ( number != -1 ) {
//			sum += number;
//			count ++;
//		}
//	}  while ( number != -1 );
//	printf("%f\n", 1.0*sum/count);

//	第二种方法
	scanf("%d", &number);
	while( number != -1){
		sum += number;
		count ++;
		scanf("%d", &number);
	}
	printf("%f\n", 1.0*sum/count);
	
	return 0;
	
}



