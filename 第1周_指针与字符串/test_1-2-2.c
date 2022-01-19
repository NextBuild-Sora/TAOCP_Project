/*
	第1周：指针与字符串
	-2 指针运算-
	-2 动态内存分配-
	
*/


#include <stdio.h>
#include <stdlib.h>

// 例子1
/*
int main(void)
{
	int number;
	int* a;
	int i;
	printf("输入数量：");
	scanf("%d", &number);
//	int a[number];
	a = (int*)malloc(number*sizeof(int));
	for (i=0; i<number; i++) {
		scanf("%d", &a[i]);
	}
	for ( i=number-1; i>=o; i--) {
		printf("%d ", a[i]);
	}
	free(a);
	
	return 0;
}
*/

// 例子2
int main(void)
{
	void *p;
	int cnt = 0;
	while((p=malloc(100*1024*1024))) {
		cnt++;
	}
	printf("分配了%d00MB的空间\n", cnt);
	
	return 0;
}



