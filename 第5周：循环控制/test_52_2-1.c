/******************************
 *
 *	第5周 循环控制
 *
 *	--2 多重循环 --
 *	---2.1 从嵌套的循环中跳出 ---
 *
 *******************************/


#include <stdio.h>

int main()
{
//	接力break
	int x;
	int one, two, five;
	
	scanf("%d", &x);
	for ( one = 1; one < x*10; one++) {
		for (two = 1; two < x*10/2; two++ ) {
			for(five=1; five < x*10/5; five++){
				if ( one + two*2 + five*5 == x*10) {
					printf("可以用%d个1角，加%d个2角，加%d个5角得到：%d元\n", one, two, five, x);
					goto out;	//跳出多重循环可以使用goto.
				}
			}
		}
	}
out:
	return 0;
	
}



