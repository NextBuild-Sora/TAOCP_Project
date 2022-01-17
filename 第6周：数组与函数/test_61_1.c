
/******************************
 *
 *	第6周：数组与函数
 *
 *	--1 数组 --
 *	--- 1 初试数组 ---
 * 这个程序是危险的，因为输入的数据超过100个。
 *******************************/



#include <stdio.h>

int main()
{
	int x;
	double sum = 0;
	int cnt =0;
	int number[100];	//定义数组。
	scanf("%d", &x);
	while ( x!= -1) {
		number[cnt] = x;	//对数组中的元素赋值。
		//
		{
			int i;
			printf("%d\t", cnt);
			for ( i=0; i<=cnt; i++ ){	//遍历数组
				printf("%d\t", number[i]);
			}
			printf("\n");
		}
		//
		sum += x;
		cnt ++;
	scanf("%d", &x);
	}
	if ( cnt > 0) {
		printf("%f\n", sum/cnt);
		int i;
		for ( i=0; i<cnt; i++){		//遍历数组
			if( number[i] > sum/cnt ){		//使用数组中的元素。
				printf("%d\n", number[i]);
			}
		}
	}

	return 0;

}



