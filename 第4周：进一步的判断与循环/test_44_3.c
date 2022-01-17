
/******************************
 *	第4周
 *
 *	--4 循环的例子--
 *	--- 3 猜数---
 *
 *******************************/



#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
	srand(time(0));
	int number = rand()%100+1;
	int count = 0;
	int a = 0;
	printf("一个1到100之间数. ");
	do{
		printf("猜1--100之间：");
		scanf("%d", &a);
		count ++;
		if ( a>number ){
			printf("猜大了.");
		} else if ( a<number ) {
			printf("猜小了.");
		}
	}while(a != number);
	printf("猜对，用了%d次猜到答案。\n", count);
	
	return 0;
	
}



