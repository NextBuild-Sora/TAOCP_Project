

/******************************
 *
 *	第7周：数组运算
 *
 *	--1 数组运算 --
 *	--- 2 数组例子：素数 ---
 *
 *******************************/



//	判断是否能被已知的且<x的素数整除
#include <stdio.h>
int isPrime(int x, int knownPrimes[], int numberOfKnownPrimes);

int main(void)
{
	const int number = 10;
	int prime[number] = {2};
	int count = 1;
	int i = 3;
	
	{
		int i;
		printf("\t\t\t\t");
		for ( i=0; i<number; i++ ) {
			printf("%d\t", i);
		}
		printf("\n");
	}
	while ( count < number) {
		if ( isPrime(i, prime, count)) {
			prime[count++] = i;
		}
		{
			printf("i=%d \tcnt=%d\t", i, count);
			int i;
			for ( i=0; i<number; i++ ){
				printf("%d\t", prime[i]);
			}
			printf("\n");
		}
		i++;
	}
	for ( i=0; i<number; i++) {
		printf("%d", prime[i]);
		if ( (i+1)%5 ) printf("\t");
		else printf("\n");
	}
	return 0;
}

int isPrime(int x, int knownPrimes[], int numberOfKnownPrimes)
{
	int ret = 1;
	int i;
	for ( i=0; i<numberOfKnownPrimes; i++){
		if ( x % knownPrimes[i] == 0){
			ret = 0;
			break;
		}
	}
	return ret;
			
}


