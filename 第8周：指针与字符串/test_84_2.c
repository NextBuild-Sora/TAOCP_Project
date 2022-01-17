
/******************************
 *
 *	第8周：指针与字符串
 *
 *	-4 字符计算 --
 *	--- 2 字符串函数---
 * 
 ******************************/


#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
	char line[] = "Hello";
	printf("strlen=%lu\n", strlen(line));	//长度
	printf("sizeof=%lu\n", sizeof(line));	//大小
	
//	比较
	char s1[] = "abc";
	char s2[] = "Abc";
	printf("%d\n", strcmp(s1, s2));
	printf("%d\n", 'a'-'A');
	
	return 0;
	
}


