/*
	第1周：指针与字符串
	-3 字符串操作-
	-2 字符串数组-

 */


#include <stdio.h>

// 程序参数
int main(int argc, char const *argv[])
{
	int i;
	for ( i=0; i<argc; i++){
		printf("%d:%s\n", i, argv[i]);
	}
	
	return 0;
}



